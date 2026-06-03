from fastapi import FastAPI, File, UploadFile
from fastapi.responses import StreamingResponse, JSONResponse
from ultralytics import YOLO
from PIL import Image
import io

app = FastAPI()
model = YOLO("yolov8m.pt")

@app.post("/detect")
async def detect(file: UploadFile = File(...)):
    contents = await file.read()
    image = Image.open(io.BytesIO(contents))

    results = model(image)

    # Annotated image
    annotated = results[0].plot()
    annotated_image = Image.fromarray(annotated)
    buf = io.BytesIO()
    annotated_image.save(buf, format="PNG")
    buf.seek(0)

    return StreamingResponse(buf, media_type="image/png")

@app.post("/detect-details")
async def detect_details(file: UploadFile = File(...)):
    contents = await file.read()
    image = Image.open(io.BytesIO(contents))

    results = model(image)

    # Extract detection data
    detections = []
    for box in results[0].boxes:
        label = model.names[int(box.cls)]
        confidence = round(float(box.conf) * 100, 1)
        detections.append({"object": label, "confidence": confidence})

    # Sort by confidence
    detections.sort(key=lambda x: x["confidence"], reverse=True)

    return JSONResponse(content={"detections": detections})