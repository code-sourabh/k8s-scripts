# Repo to scale up and scale down the deployment(corn)

## Clone the repository

```sh
git clone
```

### Note - There is no need to run the Dockerfile for creating the docker image. The image is already there in hub.docker.doc

Docker image Link -

## Note - Use Default namespace for deploying the resources to the kubernetes cluster...

### Run the Kustomisation.yaml file to deploy all the resources in the kubernetes cluster.

This kustomisation will setup nginx deployment, service account, cron job for scaling up and scaling down and a testing pod.

And Voila..!! You are done creating everything needed to setup the pod...

## Instructions for Testing

After deploying the resources to the k8s cluster, you will find that a testing pod is created for the testing...

```sh
kubectl exec -it testing /bin/bash
```

Now inside the Pod You will the python script top run. You can run the python script like :-

```sh
python3 scale.py <deployment_name> <scale_value>
```
