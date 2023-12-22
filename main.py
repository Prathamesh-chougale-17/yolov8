from ultralytics import YOLO

# from ultralytics.yolo.v8.detect.predict import Detection
# Load a model
model = YOLO("yolov8n.pt")  # build a new model from scratch

# Use the model
# results = model.train(data="config.yaml", epochs=1)

# results = model("https://ultralytics.com/images/bus.jpg")  # predict on an image

result = model.predict(source="0", show=True)

print(result)
