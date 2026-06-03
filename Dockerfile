FROM python:3.11-slim

WORKDIR /app

COPY . .

RUN pip install ultralytics streamlit pillow

EXPOSE 7860

CMD streamlit run app.py --server.port 7860 --server.address 0.0.0.0