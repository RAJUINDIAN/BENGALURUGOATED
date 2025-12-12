import streamlit as st
import base64

# Load video
video_file = open("rain.mp4", "rb").read()
video_base64 = base64.b64encode(video_file).decode()

# Background video
st.markdown(
    f"""
    <video autoplay muted loop id="bg-video">
        <source src="data:video/mp4;base64,{video_base64}" type="video/mp4">
    </video>

    <div class="overlay">Hello guys 👋<br>Welcome!</div>

    <style>
        #bg-video {{
            position: fixed;
            right: 0;
            bottom: 0;
            min-width: 100%;
            min-height: 100%;
            z-index: -1;
        }}

        .overlay {{
            position: fixed;
            top: 30px;
            left: 30px;
            font-size: 40px;
            font-weight: bold;
            color: white;
            z-index: 1;
        }}
    </style>
    """,
    unsafe_allow_html=True
)
