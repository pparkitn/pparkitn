FROM nvcr.io/nvidia/l4t-ml:r32.4.4-py3
ENV DEBIAN_FRONTEND noninteractive
#Update
RUN apt-get update && apt-get install -y python3 python3-pip python3-opencv libopencv-dev python3-dev python3-tk
#Install Packages
RUN pip3 install boto3 Image
RUN pip3 install numpy paho-mqtt	
RUN apt-get install mosquitto-clients -y
#SETUP FOLDER AND FILES
WORKDIR /workspace
COPY *.py ./
COPY *.xml ./
RUN chmod 700 *.*
#CMD python3 emotion_detect.py
CMD bash
