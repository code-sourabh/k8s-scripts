from kubernetes import client, config
import sys
import os
from code_logger import logger

if len(sys.argv) != 3:
    print("Usage: python scale.py <deployment-name> <scale>")
    sys.exit(1)

SERVICE_ACCOUNT = "/var/run/secrets/kubernetes.io/serviceaccount/"

try:
    config.load_kube_config()
    namespace = "default"
    api_instance = client.AppsV1Api()

    logger.info("Successfully connected to the cluster")
    logger.info("loaded kube config")

except config.config_exception.ConfigException:
    configuration = client.Configuration()
    try:
        with open(os.path.join(SERVICE_ACCOUNT, "token")) as f:
            token = f.read()
    except FileNotFoundError:
        logger.error("Neither found kube config file nor the token")
        sys.exit(1)

    configuration.api_key["authorization"] = token
    configuration.api_key_prefix['authorization'] = 'Bearer'

    with open(os.path.join(SERVICE_ACCOUNT, "namespace")) as f:
        namespace = f.read()

    configuration.ssl_ca_cert = os.path.join(SERVICE_ACCOUNT, "ca.crt")
    configuration.host = "https://kubernetes.default.svc"

    api_instance = client.AppsV1Api(client.ApiClient(configuration))

    logger.info("Successfully connected to the cluster")
    logger.info("loaded service account token and namespace %s", namespace)

except:
    logger.error("Failed to connect to the cluster")
    raise "Failed to connect to the cluster"

DEPLOYMENT_NAME = sys.argv[1]
SCALE = int(sys.argv[2])


def scale_deployment():
    try:
        deployment = api_instance.read_namespaced_deployment(name=DEPLOYMENT_NAME, namespace=namespace)
    except:
        logger.error("Failed to read the deployment")
        raise "Failed to read the deployment"

    if deployment.spec.replicas > SCALE:
        logger.info("Scaling down the deployment to the desired scale {}".format(SCALE))
    else:
        logger.info("Scaling up the deployment to the desired scale {}".format(SCALE))

    deployment.spec.replicas = SCALE
    api_instance.replace_namespaced_deployment(name=DEPLOYMENT_NAME, namespace=namespace, body=deployment)

    return deployment.spec.replicas


if __name__ == '__main__':
    print(scale_deployment())
