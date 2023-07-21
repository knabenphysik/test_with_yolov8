# Yolov8 Exploration

## Setup

For Windows & Ubuntu 22.04:
- cuda 11.8 + cudnn 8.6

## Installation

```
pip install torch==2.0.0+cu118 torchvision==0.15.1+cu118 torchaudio==2.0.1 --index-url https://download.pytorch.org/whl/cu118
pip install ultralytics py-cpuinfo opencv-python pillow matplotlib
```

## Custom Training
### Windows 11


### Ubuntu 22.04

## Data Labelling


## Result & Discussion


## FAQ
* **I get the error `torch.cuda.OutOfMemoryError: CUDA out of memory..`, when i train with gpu on Windows 11. How do I fix this?** Reduce _batch size_ $\leq$ *_8_*
* **I get the error `NOTE: Redirects are currently not supported in Windows or MacOs.`, when i train multi-gpu on Windows 11. How do I fix this?**

