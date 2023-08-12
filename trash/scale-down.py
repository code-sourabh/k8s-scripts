from kubernetes import client, config
import sys

if len(sys.argv) != 3:
    print("Usage: python script.py <deployment-name> <scale>")
    sys.exit(1)

NAMESPACE = "default"
DEPLOYMENT_NAME = sys.argv[1]
SCALE = sys.argv[2]


def scale_down():
    config.load_kube_config()

    api_instance = client.AppsV1Api()
    deployment = api_instance.read_namespaced_deployment(name=DEPLOYMENT_NAME, namespace=NAMESPACE)

    if deployment.spec.replicas < SCALE:
        print("Scale is already less than the desired scale")
        return deployment.spec.replicas

    deployment.spec.replicas = SCALE
    api_instance.replace_namespaced_deployment(name=DEPLOYMENT_NAME, namespace=NAMESPACE, body=deployment)

    return deployment.spec.replicas


if __name__ == '__main__':
    scale_down()
