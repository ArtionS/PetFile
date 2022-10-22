#!/usr/bin/env bash

#env
export DBNAME=PetFile
export DBUSER=petfile
export DBPASS=PetFile.SOCA.2022
export DBHOST=petfile.chkkb7hsmygj.us-east-1.rds.amazonaws.com

export AWS_STORAGE_BUCKET_NAME=petfile-static-data
export USE_S3=TRUE


docker compose up
#python manage.py runserver 0.0.0.0:80