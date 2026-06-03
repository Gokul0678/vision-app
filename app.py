import streamlit as st
import requests
from PIL import Image
import io

# Page config
st.set_page_config(
    page_title="Object Detection App",
    page_icon="🔍",
    layout="wide"
)

# Header
st.title("🔍 Object Detection App")
st.markdown("Upload an image and the AI will detect and label objects instantly.")
st.divider()

# Layout — two columns
col1, col2 = st.columns(2)

uploaded_file = st.file_uploader("Choose an image", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    with col1:
        st.subheader("📷 Original Image")
        st.image(uploaded_file, use_column_width=True)

    with col2:
        st.subheader("🤖 Detected Objects")
        with st.spinner("AI is analyzing your image..."):
            files = {"file": uploaded_file.getvalue()}
            response = requests.post("http://127.0.0.1:8000/detect", files=files)

        result_image = Image.open(io.BytesIO(response.content))
        st.image(result_image, use_column_width=True)

    # Show detection stats
    st.divider()
    st.subheader("📊 Detection Info")
    st.success("Detection complete!")
    # Get detection details
    uploaded_file.seek(0)
    detail_response = requests.post(
        "http://127.0.0.1:8000/detect-details",
        files={"file": uploaded_file.getvalue()}
    )
    data = detail_response.json()

    if data["detections"]:
        st.markdown("### Objects Found:")
        for item in data["detections"]:
            confidence = item["confidence"]
            label = item["object"]
            st.progress(int(confidence), text=f"**{label}** — {confidence}%")
    else:
        st.warning("No objects detected")
    st.info(f"Image size: {result_image.width} x {result_image.height} pixels")

else:
    # Show instructions when no image uploaded
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