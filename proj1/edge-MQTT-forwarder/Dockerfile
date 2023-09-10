FROM ubuntu
#Update
RUN apt-get update && apt-get install -y python3 python3-pip
#SETUP FOLDER AND FILES
#Install Packages
RUN pip3 install numpy 	
WORKDIR /root
RUN pip3 install google-cloud-bigquery
RUN pip3 install google-cloud
#RUN python3 -m ensurepip
RUN apt-get install -y python3-paho-mqtt
WORKDIR /root
COPY *.py ./
COPY *.json ./
RUN chmod 700 *.*
CMD bash