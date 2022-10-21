#!/usr/bin/env bash

account=$1
aws ecr get-login-password --region us-east-1 | docker login --username AWS --password-stdin $account.dkr.ecr.us-east-1.amazonaws.com

docker tag petfile-petfile-web:latest $account.dkr.ecr.us-east-1.amazonaws.com/petmedic:latest
docker push $account.dkr.ecr.us-east-1.amazonaws.com/petmedic:latest


