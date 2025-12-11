import streamlit as st
import pandas as pd

# ----------------------------------------------------
# 1️⃣ FUNCTION TO LOAD CORRECT BACKGROUND VIDEO
# ----------------------------------------------------
def set_background(weather_choice):
    if weather_choice == "Rainfall":
        video_file = "rain.mp4"
    else:
        video_file = "tempature.mp4"

    # GitHub RAW video link
    video_url = f"https://raw.githubusercontent.com/USERNAME/REPO/main/{video_file}"

    st.markdown(
        f"""
        <style>
            .stApp {{
                background: url('{video_url}') no-repeat center center fixed;
                background-size: cover;
            }}
        </style>
        """,
        unsafe_allow_html=True
    )

# ----------------------------------------------------
# 2️⃣ LOAD DATASET
# ----------------------------------------------------
df = pd.read_csv("DATASET_BEN.csv")
df['date'] = pd.to_datetime(df['date'])

# Add year & month columns
df["year"] = df["date"].dt.year
df["month"] = df["date"].dt.month

st.title("Weather Summary App - Bengaluru")

# ----------------------------------------------------
# 3️⃣ USER INPUT SELECTION
# ----------------------------------------------------
year = st.selectbox("Select Year", sorted(df["year"].unique()))
month = st.selectbox("Select Month (1–12)", range(1, 13))

weather_type = st.selectbox(
    "Select Weather Type",
    ["Rainfall", "Temperature"]
)

# Set background video dynamically
set_background(weather_type)

# ----------------------------------------------------
# 4️⃣ FILTER DATA
# ----------------------------------------------------
filtered = df[(df["year"] == year) & (df["month"] == month)]

# ----------------------------------------------------
# 5️⃣ CALCULATE RESULT
# ----------------------------------------------------
if weather_type == "Rainfall":
    avg_value = filtered["precipitation"].mean()
    label = "Average Rainfall (mm)"
else:
    avg_value = filtered["temperature_mean"].mean()
    label = "Average Temperature (°C)"

# ----------------------------------------------------
# 6️⃣ DISPLAY RESULT
# ----------------------------------------------------
st.subheader(f"Weather Summary for {month}/{year}")

if filtered.empty:
    st.error("No data available for this month/year.")
else:
    st.metric(label, f"{avg_value:.2f}")

# Extra: Show raw data
with st.expander("Show Data Table"):
    st.write(filtered)
