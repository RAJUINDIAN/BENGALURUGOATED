import streamlit as st

st.title("Upload a Video")

uploaded_file = st.file_uploader("rain.mp4", type=["mp4", "mov", "avi"])

if uploaded_file is not None:
    st.video(uploaded_file)
    st.success("Video uploaded successfully!")
