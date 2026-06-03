---
title: Vision App
emoji: 🔍
colorFrom: blue
colorTo: purple
sdk: docker
pinned: false
---
<<<<<<< HEAD

# 🔍 Object Detection App

A web application that uses AI to detect and label objects in images in real time.

## Demo
Upload any image and the app detects objects like people, cars, animals, and more — drawing bounding boxes with confidence scores.

## Tech Stack
- **YOLOv8** — object detection model
- **FastAPI** — backend API
- **Streamlit** — frontend UI
- **Python** — core language

## How it works
1. User uploads an image on the Streamlit frontend
2. Image is sent to the FastAPI backend
3. YOLOv8 model runs inference and detects objects
4. Annotated image is returned with bounding boxes and labels
5. Detection details shown with confidence scores

## How to run locally

### 1. Clone the repo
git clone https://github.com/Gokul0678/vision-app.git
cd vision-app

### 2. Create virtual environment
python -m venv venv
venv\Scripts\activate

### 3. Install dependencies
pip install ultralytics fastapi uvicorn streamlit pillow python-multipart

### 4. Run the backend
uvicorn main:app --reload

### 5. Run the frontend (new terminal)
streamlit run app.py

## What I learned
- How YOLOv8 object detection works
- Building REST APIs with FastAPI
- Connecting a frontend to a backend
- Deploying ML models as web services
=======
---
title: Vision App
emoji: 🏃
colorFrom: indigo
colorTo: indigo
sdk: docker
pinned: false
license: mit
---

Check out the configuration reference at https://huggingface.co/docs/hub/spaces-config-reference
>>>>>>> 22e1f62f0bdcd0d82bda1c92c668f3cc665b232f
