#!/bin/bash

docker build -t myimage .
docker tag myimage pparkitn/mosquitto
sudo docker run -it --rm -p 1883:1883 -v $(pwd):/workspace pparkitn/mosquitto