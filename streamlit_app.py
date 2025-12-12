import streamlit as st

st.title("Rain Video Example")

# Load and display rain.mp4
try:
    with open("rain.mp4", "rb") as video_file:
        video_bytes = video_file.read()
        st.video(video_bytes)
except Exception as e:
    st.error("❌ rain.mp4 not found or cannot be read.")
    st.write(e)

st.write("### Hello guys 👋")

