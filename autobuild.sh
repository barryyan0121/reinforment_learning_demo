#!/bin/bash

# Define variables
DOCKER_USERNAME="hy1299"
IMAGE_NAME="docker-conda"
DOCKER_REPO="$DOCKER_USERNAME/$IMAGE_NAME"

# Build the Docker image with the 'latest' tag
docker build -t $DOCKER_REPO:latest .

# Tag the image with the current date and time
IMAGE_TAG=$(date +"%Y%m%d%H%M%S")
docker tag $DOCKER_REPO:latest $DOCKER_REPO:$IMAGE_TAG

# Push the images to Docker Hub
docker push $DOCKER_REPO:$IMAGE_TAG
docker push $DOCKER_REPO:latest
