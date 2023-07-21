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

In your windows terminal:

```
set OMP_NUM_THREADS[=20]
yolo task=detect mode=train seed=9397 pretrained="yolov8n.pt" imgsz=832 data="data.yaml" epochs=150 patience=90 device=0 batch=16 plots=True val=True verbose=True name="yolov8n_custom"
```

or run from [script](train.py)

> Note: on Windows, we can only training using 1 GPU

### Ubuntu 22.04

In your linus terminal:

```
export OMP_NUM_THREADS=20
yolo task=detect mode=train seed=9397 pretrained="yolov8n.pt" imgsz=832 data="data.yaml" epochs=150 patience=90 device=[0,1] batch=16 plots=True val=True verbose=True name="yolov8n_custom"
```

## Data Labelling

- use [RoboFlow](https://roboflow.com/)
- use [Label Studio](https://labelstud.io/)

## Custom Training

Set your working directory like the following. For this example, we use pre-annotated dataset from [here](https://universe.roboflow.com/justin-burger/goats-hqnax)

```
Woking directory
    ├── datasets
    |	   ├── train
    |	   |     ├── images
    |	   |     └── labels
    |	   ├── test
    |	   |     ├── images
    |	   |     └── labels
    |	   ├── valid
    |	   |     ├── images
    |	   |     └── labels
    |	   └── data.yaml
    └── data.yaml
```

YOLOv8 has a simple annotation format which is the same as the YOLOv5 PyTorch. Every image sample has one .txt file with one line for each bounding box. The format of each row is presented as follows:

```
class_id center_x center_y width height
```

**YOLOv8 annotation format example**:

```
1:  1 0.317 0.30354206008 0.114 0.173819742489
2:  1 0.694 0.33726094420 0.156 0.23605150214
3:  1 0.395 0.32257467811 0.13 0.195278969957
```

Notice that each field is space delimited and the coordinates are normalized from zero to one. The data.yaml folder contains information used by the model to locate images and map class names to the class ids.

```
train: ../train/images
test: ../test/images
val: ../valid/images

nc: 5
names: ['kambing', 'kucing', 'orang', 'anjing', 'ikan']
```

## Result & Discussion


## FAQ
* **I get the error `torch.cuda.OutOfMemoryError: CUDA out of memory..`, when i train with gpu on Windows 11. How do I fix this?** Reduce _batch size_ $\leq$ *_8_*
* **I get the error `NOTE: Redirects are currently not supported in Windows or MacOs.`, when I train multi-gpu on Windows 11. How do I fix this?** Use Ubuntu instead!

