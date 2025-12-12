import streamlit as st
import base64

st.set_page_config(layout="wide")

# ---- Load rain.mp4 ----
def load_video():
    with open("rain.mp4", "rb") as f:
        return base64.b64encode(f.read()).decode()

video_data = load_video()

# ---- Overlay video + text ----
st.markdown(
    f"""
    <div style="position: relative; width: 100%; height: 60vh; overflow: hidden;">

        <!-- Video -->
        <video autoplay muted loop style="width: 100%; height: 100%; object-fit: cover;">
            <source src="data:video/mp4;base64,{video_data}" type="video/mp4">
        </video>

        <!-- OVERLAY TEXT -->
        <div style="
            position: absolute;
            top: 20px;
            left: 20px;
            font-size: 40px;
            font-weight: bold;
            color: white;
            text-shadow: 2px 2px 10px black;
        ">
            Hello guys 👋
        </div>

    </div>
    """,
    unsafe_allow_html=True
)
