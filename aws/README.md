# Mount Ephemeral Storage
```
sudo fdisk --list
mkdir storage
sudo mkfs.ext4 /dev/nvme1n1
sudo mount -t ext4 /dev/nvme1n1 storage
sudo chmod 777 storage/ -R
```