import streamlit as st
from ultralytics import YOLO
from PIL import Image
import io

# Page config
st.set_page_config(
    page_title="Object Detection App",
    page_icon="🔍",
    layout="wide"
)

# Load model
@st.cache_resource
def load_model():
    return YOLO("yolov8m.pt")

model = load_model()

# Header
st.title("🔍 Object Detection App")
st.markdown("Upload an image and the AI will detect and label objects instantly.")
st.divider()

col1, col2 = st.columns(2)

uploaded_file = st.file_uploader("Choose an image", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    image = Image.open(uploaded_file)

    with col1:
        st.subheader("📷 Original Image")
        st.image(image, use_column_width=True)

    with col2:
        st.subheader("🤖 Detected Objects")
        with st.spinner("AI is analyzing your image..."):
            results = model(image)
            annotated = results[0].plot()
            annotated_image = Image.fromarray(annotated)
        st.image(annotated_image, use_column_width=True)

    # Detection details
    st.divider()
    st.subheader("📊 Detection Info")

    detections = []
    for box in results[0].boxes:
        label = model.names[int(box.cls)]
        confidence = round(float(box.conf) * 100, 1)
        detections.append({"object": label, "confidence": confidence})

    detections.sort(key=lambda x: x["confidence"], reverse=True)

    if detections:
        st.success(f"Found {len(detections)} object(s)!")
        for item in detections:
            st.progress(int(item["confidence"]), text=f"**{item['object']}** — {item['confidence']}%")
    else:
        st.warning("No objects detected")

else:
    st.info("👆 Upload an image above to get started")
    st.markdown("""
    ### What this app can detect:
    - 🚗 Vehicles (cars, trucks, buses)
    - 🧑 People
    - 🐕 Animals (dogs, cats, birds)
    - 📱 Electronics (phones, laptops)
    - 🍎 Food items (apple, banana, orange)
    - And 75 more object types!
    """)