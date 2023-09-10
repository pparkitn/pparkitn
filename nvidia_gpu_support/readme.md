# Adding NVIDIA GPU Support for PyTorch on Ubuntu

This guide will help you set up NVIDIA GPU support on Ubuntu to run PyTorch with GPU acceleration.

## 1. Check Your GPU

Open a terminal and verify that you have an NVIDIA GPU installed in your machine:

```bash
lspci | grep -i nvidia

This should display information about your NVIDIA GPU.

## 2. Install NVIDIA Drivers

```bash
sudo apt update
sudo apt install nvidia-driver-XXX
sudo reboot




export PATH=/usr/local/cuda-XXX/bin:$PATH
export LD_LIBRARY_PATH=/usr/local/cuda-XXX/lib64:$LD_LIBRARY_PATH
