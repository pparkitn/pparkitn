# Human Pose Estimation

**Real-time pose tracking with MediaPipe** — video trimming, side-by-side comparison, GIF generation, and motion-tracked output.

## Overview
A complete pipeline for human pose estimation using Google's MediaPipe Pose solution. The notebook demonstrates end-to-end video processing: trimming, side-by-side merging, animated GIF creation, motion-tracked video overlay, and H.265 compression.

## Challenge
- **End-to-end video processing pipeline**: From raw footage to annotated output with synchronized dual-view comparison
- **Real-time pose landmark detection**: 33 3D landmarks with timestamp overlay

## Stack
- `Python`
- `MediaPipe`
- `OpenCV`
- `ffmpeg`
- `subprocess`

## Pipeline Steps
1. **Input**: Videos from `video_source/` directory (expects `.MOV` files)
2. **Trimming**: `trim_video_from_beg()` — cuts first N seconds using ffmpeg stream copy
3. **Side-by-side merge**: `merge_two_videos_sbys()` — pads and overlays two videos horizontally using all CPU cores
4. **Motion tracking**: `add_motion_track()` — runs MediaPipe Pose on each frame, draws skeleton with landmark IDs and timestamps
5. **GIF generation**: `make_gif()` — converts to animated GIF at 10 fps, 640px width
6. **Compression**: H.265/HEVC encoding via ffmpeg for reduced file size

## Usage
```bash
# Prerequisites
pip install mediapipe opencv-python
# ffmpeg must be installed and on PATH (or update ffmpeg_path in notebook)

# Run notebook cells sequentially
jupyter notebook HumanPoseEstimation.ipynb
```

> **Note**: The notebook contains hardcoded paths (`video_source/*`, `../../../ffmpeg/bin/ffmpeg.exe`) from the original Windows development environment. Adapt paths for your OS/environment before running.

## Example Outputs
- `image.gif` / `image1.gif` — animated GIFs of pose-tracked comparisons
- `combined_videoC.mp4` — side-by-side merged video
- `compressed_video.mp4` — H.265 compressed output
- `motionA.avi` / `motionB.avi` — pose-annotated intermediate videos

## Artifacts
- `HumanPoseEstimation.ipynb` — Full pipeline notebook
- `pics/demo.png` — Pipeline thumbnail