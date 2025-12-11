import streamlit as st
import pandas as pd

# ----------------------------------------------------
# 1️⃣ PAGE SETTINGS + BACKGROUND VIDEO (from GitHub repo)
# ----------------------------------------------------
video_url = "https://raw.githubusercontent.com/USERNAME/REPO/main/video.mp4"  
# 🔼 Replace with your RAW GitHub video link

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
# 2️⃣ IMPORT DATA
# ----------------------------------------------------
df = pd.read_csv("DATASET_BEN.csv")
df['date'] = pd.to_datetime(df['date'])

# ----------------------------------------------------
# 3️⃣ CREATE YEAR & MONTH OPTIONS
# ----------------------------------------------------
df["year"] = df["date"].dt.year
df["month"] = df["date"].dt.month

st.title("Weather Summary App - Bengaluru")

# ----------------------------------------------------
# 4️⃣ USER INPUTS
# ----------------------------------------------------
year = st.selectbox("Select Year", sorted(df["year"].unique()))
month = st.selectbox("Select Month (1–12)", range(1, 13))

weather_type = st.selectbox(
    "Select Weather Type",
    ["Rainfall", "Temperature"]
)

# ----------------------------------------------------
# 5️⃣ FILTER DATA
# ----------------------------------------------------
filtered = df[(df["year"] == year) & (df["month"] == month)]

# ----------------------------------------------------
# 6️⃣ OUTPUT CALCULATION
# ----------------------------------------------------
if weather_type == "Rainfall":
    avg_value = filtered["precipitation"].mean()
    label = "Average Rainfall (mm)"
else:
    avg_value = filtered["temperature_mean"].mean()
    label = "Average Temperature (°C)"

# ----------------------------------------------------
# 7️⃣ SHOW OUTPUT
# ----------------------------------------------------
st.subheader(f"Result for {month}/{year}")

if filtered.empty:
    st.error("No data available for selected month/year.")
else:
    st.metric(label, f"{avg_value:.2f}")

# ----------------------------------------------------
# 8️⃣ EXPANDER TO SHOW DATA
# ----------------------------------------------------
with st.expander("Show Raw Data"):
    st.write(filtered)
