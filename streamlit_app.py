import streamlit as st
import pandas as pd

# ----------------------------------------------------
# 1️⃣ SET BACKGROUND VIDEO BASED ON WEATHER TYPE
# ----------------------------------------------------
def set_background(weather_choice):
    if weather_choice == "Rainfall":
        video_name = "rain.mp4"
    else:
        video_name = "tempature.mp4"

    # GitHub RAW video link
    video_url = f"https://raw.githubusercontent.com/USERNAME/REPO/main/{video_name}"

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
# 2️⃣ LOAD DATA
# ----------------------------------------------------
df = pd.read_csv("DATASET_BEN.csv")
df['date'] = pd.to_datetime(df['date'])

# Extract month
df["month"] = df["date"].dt.month

st.title("Bengaluru Weather Summary")

# ----------------------------------------------------
# 3️⃣ USER INPUTS (Month + Weather Type)
# ----------------------------------------------------
month = st.selectbox("Select Month (1–12)", range(1, 13))

weather_type = st.selectbox(
    "Select Weather Type",
    ["Rainfall", "Temperature"]
)

# Apply background video
set_background(weather_type)

# ----------------------------------------------------
# 4️⃣ FILTER DATA BY MONTH ONLY
# ----------------------------------------------------
filtered = df[df["month"] == month]

# ----------------------------------------------------
# 5️⃣ CALCULATE AVERAGE VALUES
# ----------------------------------------------------
if weather_type == "Rainfall":
    avg_value = filtered["precipitation"].mean()
    label = "Average Rainfall (mm)"
else:
    avg_value = filtered["temperature_mean"].mean()
    label = "Average Temperature (°C)"

# ----------------------------------------------------
# 6️⃣ SHOW RESULT
# ----------------------------------------------------
st.subheader(f"Result for Month: {month}")

if filtered.empty:
    st.error("No data available for this month.")
else:
    st.metric(label, f"{avg_value:.2f}")

# Optional: Show data
with st.expander("Show Raw Data"):
    st.write(filtered)
