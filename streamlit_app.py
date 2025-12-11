import streamlit as st
import pandas as pd

# ----------------------------
# Load your dataset
# ----------------------------
@st.cache_data
def load_data():
    df = pd.read_csv("DASH_comeback.csv")
    df['date'] = pd.to_datetime(df['date'])
    df['year'] = df['date'].dt.year
    df['month'] = df['date'].dt.month
    df['day'] = df['date'].dt.day
    return df

df = load_data()

# ----------------------------
# Background Video Based on Weather Type
# ----------------------------
def add_bg_video(video_file):
    video_html = f"""
        <video autoplay muted loop id="bg-video" style="
            position: fixed;
            right: 0;
            bottom: 0;
            min-width: 100%;
            min-height: 100%;
            z-index: -1;">
            <source src="{video_file}" type="video/mp4">
        </video>
    """
    st.markdown(video_html, unsafe_allow_html=True)

# ----------------------------
# UI Selection
# ----------------------------
st.title("🌦 Weather Dashboard – Bengaluru")

weather_type = st.selectbox("Select Weather Type", ["Temperature", "Rainfall"])

if weather_type == "Temperature":
    add_bg_video("tempature.mp4")
else:
    add_bg_video("rain.mp4")

# Date selection
year = st.selectbox("Select Year", sorted(df['year'].unique()))
month = st.selectbox("Select Month", sorted(df['month'].unique()))
day = st.selectbox("Select Day", sorted(df['day'].unique()))

# ----------------------------
# Filter Data
# ----------------------------
filtered = df[
    (df['year'] == year) &
    (df['month'] == month) &
    (df['day'] == day)
]

# ----------------------------
# Output
# ----------------------------
if filtered.empty:
    st.warning("No data found for this date.")
else:
    row = filtered.iloc[0]

    st.success(f"Weather for {row['date'].date()}")

    if weather_type == "Temperature":
        st.metric("Max Temperature", f"{row['temp_max']} °C")
        st.metric("Min Temperature", f"{row['temp_min']} °C")

    else:
        st.metric("Rainfall", f"{row['rainfall']} mm")

    # Extra info
    st.subheader("Additional Weather Parameters")
    st.write(f"**Humidity:** {row['humidity']} %")
    st.write(f"**Pressure:** {row['pressure']} hPa")
    st.write(f"**Wind Speed:** {row['wind_speed']} m/s")
    st.write(f"**Condition:** {row['weather']}")
