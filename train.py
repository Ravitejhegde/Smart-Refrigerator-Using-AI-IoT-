from ultralytics import YOLO

# Load the pre-trained YOLOv8n model
model = YOLO("yolov8n.pt")

# Train on your dataset
model.train(data="./dataset/data.yaml", epochs=30, imgsz=640)

# After training, test the model
results = model.predict(source="./dataset/images/val", conf=0.25)

