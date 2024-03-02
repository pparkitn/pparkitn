# Mount Ephemeral Storage
```
sudo fdisk --list
mkdir storage
sudo mkfs.ext4 /dev/nvme1n1
sudo mount -t ext4 /dev/nvme1n1 storage
sudo chmod 777 storage/ -R
```


# Amazon EC2
- https://aws.amazon.com/ec2/pricing/on-demand/
- https://aws.amazon.com/ec2/instance-types/

- Nvidia Instance user = ubuntu  
- Amazon Instance user = ec2-user for 

- x2gd.xlarge	$0.334	4	64 GiB	1 x 237 SSD	Up to 10 Gigabit
- High Memory x2gd/r6g -arm processor | Best Price
- GPU G4dn | Best Price one T4
- High CPU C6G/C7G - arm processor



```
ssh -i us-east-1-jetson.pem -L 8888:localhost:8888 ubuntu@ec2-35-170-68-218.compute-1.amazonaws.com
ssh -i us-east-1-jetson.pem ubuntu@ec2-35-170-68-218.compute-1.amazonaws.com

ssh -i us-east-1-jetson.pem -L 8888:localhost:8888 ec2-user@ec2-35-170-68-218.compute-1.amazonaws.com
ssh -i us-east-1-jetson.pem ec2-user@ec2-35-170-68-218.compute-1.amazonaws.com

```

- Mount Ephemeral Storage
```
sudo fdisk --list
mkdir storage
sudo mkfs.ext4 /dev/nvme1n1
sudo mount -t ext4 /dev/nvme1n1 storage
sudo chmod 777 storage/ -R
```

```
zip -r storage.zip storage/
```

-Fedora
```
sudo yum update -y
sudo yum install git docker -y
sudo systemctl start docker
pip3 install kaggle
ssh-keygen
cat /home/ec2-user/.ssh/id_rsa.pub
git clone git@github.com:pparkitn/docker.git
git clone git@github.com:pparkitn/kaggle-crypto.git
```


-Debian
https://docs.docker.com/engine/install/debian/
```
sudo apt-get update

sudo apt-get install \
    ca-certificates \
    curl \
    gnupg \
    lsb-release

curl -fsSL https://download.docker.com/linux/debian/gpg | sudo gpg --dearmor -o /usr/share/keyrings/docker-archive-keyring.gpg
 echo \
  "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/docker-archive-keyring.gpg] https://download.docker.com/linux/debian \
  $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null

sudo apt-get update -y
sudo apt-get install docker-ce docker-ce-cli containerd.io -y
sudo docker run hello-world
sudo apt-get install python3-pip -y
sudo apt install -y python-pip -y
pip3 install kaggle 
ssh-keygen
cat  /home/pparkitny/.ssh/id_rsa.pub
cat  /home/ubuntu/.ssh/id_rsa.pub
git clone git@github.com:pparkitn/docker.git
git clone git@github.com:pparkitn/kaggle-crypto.git
sudo apt-get update && sudo apt-get upgrade -y
```



```
kaggle competitions download -c g-research-crypto-forecasting
mkdir data
cd kaggle-crypto
cp kaggle.json /root/.kaggle/kaggle.json
cp kaggle.json /home/ec2-user/.kaggle/kaggle.json
cd ..
cd data

kaggle competitions download -c ubiquant-market-prediction
kaggle datasets download -d dsptlp/ubqparquet-window0
kaggle datasets download -d dsptlp/ubq-bw2
kaggle datasets download -d dsptlp/ubq-data-v1
kaggle datasets download -d dsptlp/ubq-models-v1
kaggle datasets download -d dsptlp/89723473

kaggle datasets download -d dsptlp/grc-models-gpu
apt-get install zip
unzip g-research-crypto-forecasting.zip
cd ..
sudo docker/jupyterlab-python/start.sh
```


Create a New Dataset
Here are the steps you can follow to create a new dataset on Kaggle:
Create a folder containing the files you want to upload
Run 
```
kaggle datasets init -p /path/to/dataset to generate a metadata file
```
Add your dataset’s metadata to the generated file, datapackage.json
Run
```
kaggle datasets create -p /path/to/dataset to create the dataset
```

```
jupyter-lab --ip=0.0.0.0 --port 8888 --allow-root --no-browser --NotebookApp.token=''
```


# Quick Start NEW
1. Start Amazon AWSDeep Learning AMI GPU PyTorch 1.10.0 (Ubuntu 20.04) 20220526 | ami-022a0907f8da479a8 | 
- g5.2xlarge $1.212/hour 
- p3.2xlarge $3.06/hour 
- g4dn.2xlarge $0.752/hour
3. ```docker run --privileged --shm-size=1g --ulimit memlock=-1 --ipc=host --net=host --gpus all -it -v $(pwd):/workspace nvcr.io/nvidia/pytorch:22.02-py3```
4. ```jupyter-lab --ip=0.0.0.0 --port 8888 --allow-root --no-browser --NotebookApp.token=''```

# Kaggle Docker:
```
docker run --runtime nvidia  --privileged --shm-size=1g --ulimit memlock=-1 --ipc=host --net=host --gpus all -it kaggle/python-gpu-build /bin/bash
docker run --runtime nvidia  --privileged --shm-size=1g --ulimit memlock=-1 --ipc=host --net=host --gpus all -it gcr.io/kaggle-gpu-images/python /bin/bash
```

# Mount Ephemeral Storage
```
sudo fdisk --list
mkdir storage
sudo mkfs.ext4 /dev/nvme1n1
sudo mount -t ext4 /dev/nvme1n1 storage
sudo chmod 777 storage/ -R
ls
```

# GET SSH-KEY for GITHUB
```
ssh-keygen



cat /home/ubuntu/.ssh/id_rsa.pub

```

# Quick Start OLD
1. Start Amazon AWS Deep Learning AMI (Ubuntu 18.04) Version 45.0 | ami-0cc995a23da39b9ba | g4DN
2. Start Amazon AWSDeep Learning AMI GPU PyTorch 1.10.0 (Ubuntu 20.04) 20220526 | ami-022a0907f8da479a8 | g4DN
3. ```docker run --privileged --shm-size=1g --ulimit memlock=-1 --ipc=host --net=host --gpus all -it -v $(pwd):/workspace nvcr.io/nvidia/pytorch:21.06-py3```
4. ```docker run --privileged --shm-size=1g --ulimit memlock=-1 --ipc=host --net=host --gpus all -it -v $(pwd):/workspace nvcr.io/nvidia/pytorch:22.12-py3```
5. ```jupyter-lab --ip=0.0.0.0 --port 8888 --allow-root --no-browser --NotebookApp.token=''```
6. ```kaggle datasets download -d dsptlp/rsna-dataset-512-png-bal-dup```

# Pytorch Transformations
https://pytorch.org/vision/stable/auto_examples/plot_transforms.html#sphx-glr-auto-examples-plot-transforms-py

# Models Summary
https://github.com/rwightman/pytorch-image-models/blob/main/results/results-imagenet.csv
https://pytorch.org/vision/0.13/models.html

# Nvidia Code
https://github.com/NVIDIA/DALI/blob/5dfe17b17c077f79850865247b2448801e8faed2/docs/examples/use_cases/pytorch/resnet50/main.py
https://github.com/pytorch/examples/blob/main/imagenet/main.py

# Nvidia Docker Container Details
https://docs.nvidia.com/deeplearning/frameworks/pytorch-release-notes/rel_22-02.html#rel_22-02

# Docker Export Port
https://www.mend.io/free-developer-tools/blog/docker-expose-port/
```docker run --privileged --shm-size=1g --ulimit memlock=-1 --ipc=host -p 8888:8888 --gpus all -it -v $(pwd):/workspace nvcr.io/nvidia/pytorch:21.06-py3```

## Docker Setup Ubuntu
- https://docs.docker.com/engine/install/ubuntu/

## Kaggle Docker Image
- https://github.com/Kaggle/docker-python

# Distributed Training
https://github.com/pparkitn/Berkeley/tree/master/W251/HW9/models

# Amazon EC2
- https://towardsdatascience.com/choosing-the-right-gpu-for-deep-learning-on-aws-d69c157d8c86
- https://aws.amazon.com/ec2/pricing/on-demand/
- https://aws.amazon.com/ec2/instance-types/

- Nvidia Instance user = ubuntu  
- Amazon Instance user = ec2-user for 

- x2gd.xlarge	$0.334	4	64 GiB	1 x 237 SSD	Up to 10 Gigabit
- High Memory x2gd/r6g -arm processor | Best Price
- GPU G4dn | Best Price one T4
- High CPU C6G/C7G - arm processor

- Deep Learning AMI (Ubuntu 18.04) Version 45.0 | ami-0cc995a23da39b9ba

# Install JupyterLab
`
pip install jupyterlab
`

```
ssh -i us-east-1-jetson.pem -L 8888:localhost:8888 ubuntu@ec2-35-170-68-218.compute-1.amazonaws.com
ssh -i us-east-1-jetson.pem ubuntu@ec2-35-170-68-218.compute-1.amazonaws.com

ssh -i us-east-1-jetson.pem -L 8888:localhost:8888 ec2-user@ec2-35-170-68-218.compute-1.amazonaws.com
ssh -i us-east-1-jetson.pem ec2-user@ec2-35-170-68-218.compute-1.amazonaws.com

```


```
zip -r storage.zip storage/
```

-Fedora
```
sudo yum update -y
sudo yum install git docker -y
sudo systemctl start docker
pip3 install kaggle
ssh-keygen
cat /home/ec2-user/.ssh/id_rsa.pub
git clone git@github.com:pparkitn/docker.git
git clone git@github.com:pparkitn/kaggle-crypto.git
```


-Debian
https://docs.docker.com/engine/install/debian/
```
sudo apt-get update

sudo apt-get install \
    ca-certificates \
    curl \
    gnupg \
    lsb-release

curl -fsSL https://download.docker.com/linux/debian/gpg | sudo gpg --dearmor -o /usr/share/keyrings/docker-archive-keyring.gpg
 echo \
  "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/docker-archive-keyring.gpg] https://download.docker.com/linux/debian \
  $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null

sudo apt-get update -y
sudo apt-get install docker-ce docker-ce-cli containerd.io -y
sudo docker run hello-world
sudo apt-get install python3-pip -y
sudo apt install -y python-pip -y
pip3 install kaggle 
ssh-keygen
cat  /home/pparkitny/.ssh/id_rsa.pub
cat  /home/ubuntu/.ssh/id_rsa.pub
git clone git@github.com:pparkitn/docker.git
git clone git@github.com:pparkitn/kaggle-crypto.git
sudo apt-get update && sudo apt-get upgrade -y
```

# DOCKER CONTAINERS
### Jetson
- https://catalog.ngc.nvidia.com/orgs/nvidia/containers/l4t-pytorch
```
sudo docker pull nvcr.io/nvidia/l4t-pytorch:r35.1.0-pth1.12-py3
```

### 64-BIT
- https://catalog.ngc.nvidia.com/orgs/nvidia/containers/pytorch
```
sudo docker pull nvcr.io/nvidia/pytorch:22.12-py3
docker run --gpus all -it nvcr.io/nvidia/pytorch:22.12-py3
docker run --privileged --shm-size=1g --ulimit memlock=-1 --ipc=host --net=host --gpus all -it -v $(pwd):/workspace nvcr.io/nvidia/pytorch:21.06-py3
docker run --privileged --shm-size=1g --ulimit memlock=-1 --ipc=host --net=host --gpus all -it -v $(pwd):/workspace nvcr.io/nvidia/pytorch:22.12-py3
```

# KAGGLE

```
kaggle competitions download -c g-research-crypto-forecasting
mkdir data
cd kaggle-crypto
cp kaggle.json /root/.kaggle/kaggle.json
cp kaggle.json /home/ec2-user/.kaggle/kaggle.json
cd ..
cd data

kaggle competitions download -c ubiquant-market-prediction
kaggle datasets download -d dsptlp/ubqparquet-window0
kaggle datasets download -d dsptlp/ubq-bw2
kaggle datasets download -d dsptlp/ubq-data-v1
kaggle datasets download -d dsptlp/ubq-models-v1
kaggle datasets download -d dsptlp/89723473

kaggle datasets download -d dsptlp/grc-models-gpu
apt-get install zip
unzip g-research-crypto-forecasting.zip
cd ..
sudo docker/jupyterlab-python/start.sh
```


Create a New Dataset
Here are the steps you can follow to create a new dataset on Kaggle:
Create a folder containing the files you want to upload
Run 
```
kaggle datasets init -p /path/to/dataset to generate a metadata file | no folders just add folders as zipped files
```
Add your dataset’s metadata to the generated file, datapackage.json
Run
```
kaggle datasets create -p /path/to/dataset to create the dataset
```

### Create a New Dataset
Here are the steps you can follow to create a new dataset on Kaggle:

Create a folder containing the files you want to upload

Run kaggle datasets init -p /path/to/dataset to generate a metadata file

Add your dataset’s metadata to the generated file, datapackage.json

Run kaggle datasets create -p /path/to/dataset to create the dataset

Your dataset will be private by default. You can also add a -u flag to make it public when you create it, or navigate to “Settings” > “Sharing” from your dataset’s page to make it public or share with collaborators.

### Create a New Dataset Version
If you’d like to upload a new version of an existing dataset, follow these steps:

Run kaggle datasets init -p /path/to/dataset to generate a metadata file (if you don’t already have one)

Make sure the id field in dataset-metadata.json (or datapackage.json) points to your dataset

Run kaggle datasets version -p /path/to/dataset -m "Your message here"


### START JUPYTER-LAB
```
jupyter-lab --ip=0.0.0.0 --port 8888 --allow-root --no-browser --NotebookApp.token=''
```

### DUPLICATE FILES

```
for file in *.png; do cp "$file" "DUP_$file"; done;
```

### COUNT FILES IN FOLDER
```
ls | wc -l
```
