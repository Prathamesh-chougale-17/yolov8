from ultralytics import YOLO

# Load a model
model = YOLO("yolov8n.yaml")  # build a new model from scratch

# Use the model

results = model("https://ultralytics.com/images/bus.jpg")  # predict on an image
