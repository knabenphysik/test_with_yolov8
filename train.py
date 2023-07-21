from ultralytics import YOLO
import os

# adjust your value according to your CPU core
os.environ["OMP_NUM_THREADS"] = "20"

# Load model
model = YOLO("yolov8n.pt")

# Training setting

results = model.train(
  seed=9397,
  pretrained="yolov8n.pt",
  imgsz=832,
  data="data.yaml",
  epochs=150,
  patience=90,
  device=[0,1],
  batch=16,
  plots=True,
  val=True,
  verbose=True,
  name="yolov8n_custom"
)
