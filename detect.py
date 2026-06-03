from ultralytics import YOLO
from PIL import Image

# Load the YOLO model (downloads automatically on first run)
model = YOLO("yolov8m.pt")

# Run detection on a test image
results = model("https://ultralytics.com/images/bus.jpg")

# Show the result
results[0].show()

# Print what was detected
for result in results:
    for box in result.boxes:
        label = model.names[int(box.cls)]
        confidence = float(box.conf)
        print(f"Detected: {label} — Confidence: {confidence:.2f}")