#!/bin/bash

docker build -t myimage .
docker tag myimage pparkitn/emotion_detect:v1
sudo docker run --privileged -it --rm --device /dev/video0 --runtime nvidia  -e DISPLAY=$DISPLAY -v /tmp/.X11-unix/:/tmp/.X11-unix -v $(pwd):/workspace pparkitn/emotion_detect:v1