<p align="center">
  <p align="center"><strong>MRI ANALYZER</strong></p>
  <p align="center"><strong>Piotr Parkitny | pparkitny@berkeley.edu</strong></p>
  <p align="center"><strong>Aidan Jackson | aidanjackson@berkeley.edu</strong></p>
  <p align="center"><strong>Dhyani Parekh | dhyanip7@berkeley.edu</strong></p>
  <p align="center"><strong>Candice Sener | senercansu@berkeley.edu</strong></p>
</p>

<!-- TABLE OF CONTENTS -->
## Table of Contents

* [Problem Statement](#problem-statement)
* [Dataset](#dataset)
* [Project Solution](#project-solution)
* [Cloud Training](#cloud-training)
* [Edge Inference](#edge-inference)
* [Dashboard](#Dashboard)
* [Results](#results)
* [Future Work](#future-work)

<!-- PROBLEM STATEMENT -->
## Problem Statement

The MRI Analyzer team’s mission is to aid medical professionals when identifying prostate cancer and determining the best course of follow-up actions. 
MRI Analyzer offers flexibility to patients who only have a partial data record available, qualifies its predictions with uncertainty estimates at each step, and matches in-practice metrics of cancer diagnosis. 
This has the ability to increase the speed with which readings can be performed while maintaining performance and usefulness in a variety of healthcare scenarios.

<!-- DATASET -->
## Dataset

From the National Cancer Institute’s Image Data Commons archive, we obtained the dataset titled Prostate MRI and Ultrasound With Pathology and Coordinates of Tracked Biopsy (Prostate-MRI-US-Biopsy). 

<p align="center">
    <img src="pics/MRI-ORIG.gif" alt="Logo" width="800">
</p>

### Summary of Dataset
This dataset was derived from tracked biopsy sessions using the Artemis biopsy system, many of which included image fusion with MRI targets. Patients received a 3D transrectal ultrasound scan, after which nonrigid registration (e.g. “fusion”) was performed between real-time ultrasound and preoperative MRI, enabling biopsy cores to be sampled from MR regions of interest. Most cases also included sampling of systematic biopsy cores using a 12-core digital template. The Artemis system tracked targeted and systematic core locations using encoder kinematics of a mechanical arm, and recorded locations relative to the Ultrasound scan. MRI biopsy coordinates were also recorded for most cases. STL files and biopsy overlays are available and can be visualized in 3D Slicer with the SlicerHeart extension.  Spreadsheets summarizing biopsy and MR target data are also available. See the Detailed Description tab below for more information.

MRI targets were defined using multiparametric MRI, e.g. t2-weighted, diffusion-weighted, and perfusion-weighted sequences, and scored on a Likert-like scale with close correspondence to PIRADS version 2. t2-weighted MRI was used to trace ROI contours, and is the only sequence provided in this dataset. MR imaging was performed on a 3 Tesla Trio, Verio or Skyra scanner (Siemens, Erlangen, Germany). A transabdominal phased array was used in all cases, and an endorectal coil was used in a subset of cases. The majority of pulse sequences are 3D T2:SPC, with TR/TE 2200/203, Matrix/FOV 256 × 205/14 × 14 cm, and 1.5mm slice spacing. Some cases were instead 3D T2:TSE with TR/TE 3800–5040/101, and a small minority were imported from other institutions (various T2 protocols.)

Ultrasound scans were performed with Hitachi Hi-Vision 5500 7.5 MHz or the Noblus C41V 2-10 MHz end-fire probe. 3D scans were acquired by rotation of the end-fire probe 200 degrees about its axis, and interpolating to resample the volume with isotropic resolution.

Patients with suspicion of prostate cancer due to elevated PSA and/or suspicious imaging findings were consecutively accrued. Any consented patient who underwent or had planned to receive a routine, standard-of-care prostate biopsy at the UCLA Clark Urology Center was included.  

### Data Source Files
- Images DICOM 77GB (67K files)
- Target Data (XLSX) 131 (KB)
- Biopsy Data (XLSX) 4.25 (MB)
- STL Files (ZIP) 274 (MB)
- Biopsy Overlays (ZIP) 333 (MB)

### EDA

<p align="center">
    <img src="pics/weight_hist.png" alt="Logo" width="200">
    <img src="pics/size_hist.png" alt="Logo" width="200">
    <img src="pics/age_hist.png" alt="Logo" width="200">
    <img src="pics/PSA_hist.png" alt="Logo" width="200">
</p>


<!-- PROJECT SOLUTION -->
## Project Solution

The diagram below describes the overall solution.    
The solution is broken down into Cloud and Edge components.

<p align="center">
    <img src="pics/design.PNG" alt="Logo" width="800">
</p>

## Cloud Components
Cloud is composed of Amazon AWS and Google GCP that are used for training, storing results, and displaying real-time results from the Edge device
1. Training      
The model that is used on Amazon AWS for training on the dataset --> [Model](cloud/Model_V4.ipynb)
2. BigQuery  
The Google GCP-hosted database that stores real-time input data from the Edge device.
2. DataStudio     
Datastudio dashboard hosted on Google GCP for displaying data from BigQuery 

## Edge Device
Jetson is used as the edge device for running the model
1. MQTT Broker --> [edge-MQTT-broker](edge-MQTT-broker/).
The Edge MQTT broker stores the detected facial emotion.
2. MQTT Forwarder --> [edge-MQTT-forwarder](edge-MQTT-forwarder/).
The Edge MQTT Forwarder subscribes to the local MQTT Broker and publishes to the cloud DB.
3. Face Detector --> [edge-emotion-detector](edge-face-emotion/).
The Edge Face Detector detects the facial emotion and publishes it to the local MQTT Broker.

<!-- CLOUD TRAINING -->
## Cloud Training
------------
Training is done on Amazon AWS EC2 using g4dn.xlarge instance. Below are the steps required to set up training
- Start Amazon VM and SSH into the box

```
ssh -i us-east-1-jetson.pem -L 7777:127.0.0.1:7777 ubuntu@ec2-34-238-51-68.compute-1.amazonaws.com 
```

### Start Docker and JupyterLab
- After starting docker open the notebook and run file --> [cloud-train](cloud/Model_V4.ipynb). 
- At each epoch the model is saved to S3 bucket so it can be pulled down by the edge device.

```
docker run --privileged --shm-size=1g --ulimit memlock=-1 --ipc=host --net=host --gpus all -it -v $(pwd):/workspace nvcr.io/nvidia/pytorch:21.06-py3
jupyter-lab --ip=0.0.0.0 --port 7777 --allow-root --no-browser --NotebookApp.token=''
```

### Weights & Biases
Weights & Biases is used for tracking the progress of the training along with keeping all the results saved.   
Below are an example of the generated graphs.

<p align="center">
    <img src="pics/acc1.PNG"  width="800">
</p>

<p align="center">
    <img src="pics/acc5.PNG"  width="800">
</p>

<p align="center">
    <img src="pics/loss.PNG"  width="800">
</p>


<!-- Edge Inference-->
## Edge Inference
------------
Running on the edge is done on the Jetson, the following code will start the process.

Start Broker
```
cd edge-MQTT-broker
./start.sh
```

Start Forwarder
```
cd edge-MQTT-forwarder
./start.sh
```

Start Face Emotion Detector
```
sudo xrandr --fb 1900x1000
xhost +
cd edge-face-detect
start.sh
python3 emotion_detect.py
```

Below are some images that are based on running on the Jetson. No noticeable lag can be observed and the overall performance is very good.

<p align="center">
    <img src="pics/face_happy.PNG"  width="300">
    <img src="pics/face_suprised.PNG"  width="300">
  <img src="pics/face_angry.PNG"  width="300">
</p>

<!-- DASHBOARD -->
### Dashboard
------------
The dashboard pulls the data from bigquery that is used by MQTT Fowarder to store emotions along with a timestamp.

<p align="center">
    <img src="pics/emotion_dashboard.PNG"  width="800">
</p>

<!-- RESULTS -->
### Results
------------
- Very good results classifying happy and surprised
- Angry, disgusted, and fearful show very low performance
- Acc1 = 62.5 %


<p align="center">
    <img src="pics/results-faces.PNG"  width="800">
</p>

<p align="center">
    <img src="pics/confusion_matrix.PNG"  width="400">
</p>

<p align="center">
    <img src="pics/confusion_matrix_normalized.PNG"  width="400">
</p>

<p align="center">
    <img src="pics/report.PNG"  width="400">
</p>
