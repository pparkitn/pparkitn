#!/bin/bash

docker build -t myimage .
docker tag myimage pparkitn/forwarder:v1
sudo docker run -it --rm -v $(pwd):/workspace pparkitn/forwarder:v1