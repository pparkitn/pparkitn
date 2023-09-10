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
    <img src="pics/MRI-ORIG.gif" alt="Logo" width="300">
  <img src="pics/US-ORIG.gif" alt="Logo" width="300">
</p>

### Summary of Dataset
This dataset was derived from tracked biopsy sessions using the Artemis biopsy system, many of which included image fusion with MRI targets. Patients received a 3D transrectal ultrasound scan, after which nonrigid registration (e.g. “fusion”) was performed between real-time ultrasound and preoperative MRI, enabling biopsy cores to be sampled from MR regions of interest. Most cases also included a sampling of systematic biopsy cores using a 12-core digital template. The Artemis system tracked targeted and systematic core locations using encoder kinematics of a mechanical arm, and recorded locations relative to the Ultrasound scan. MRI biopsy coordinates were also recorded for most cases. STL files and biopsy overlays are available and can be visualized in 3D Slicer with the SlicerHeart extension.  Spreadsheets summarizing biopsy and MR target data are also available. See the Detailed Description tab below for more information.

MRI targets were defined using multiparametric MRI, e.g. t2-weighted, diffusion-weighted, and perfusion-weighted sequences, and scored on a Likert-like scale with close correspondence to PIRADS version 2. t2-weighted MRI was used to trace ROI contours, and is the only sequence provided in this dataset. MR imaging was performed on a 3 Tesla Trio, Verio, or Skyra scanner (Siemens, Erlangen, Germany). A transabdominal phased array was used in all cases, and an endorectal coil was used in a subset of cases. The majority of pulse sequences are 3D T2:SPC, with TR/TE 2200/203, Matrix/FOV 256 × 205/14 × 14 cm, and 1.5mm slice spacing. Some cases were instead 3D T2:TSE with TR/TE 3800–5040/101, and a small minority were imported from other institutions (various T2 protocols.)

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
</p>
<p align="center">
  <img src="pics/age_hist-768x526.png" alt="Logo" width="200">
    <img src="pics/PSA_hist.png" alt="Logo" width="200">
</p>
