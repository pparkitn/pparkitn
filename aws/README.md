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
