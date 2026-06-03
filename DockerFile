FROM python:3.11-slim

WORKDIR /app

COPY . .

RUN pip install ultralytics fastapi uvicorn streamlit pillow python-multipart requests

EXPOSE 7860

CMD uvicorn main:app --host 0.0.0.0 --port 8000 --workers 1 & sleep 3 && streamlit run app.py --server.port 7860 --server.address 0.0.0.0