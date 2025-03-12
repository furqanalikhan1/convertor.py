
import streamlit as st

# Page Configuration
st.set_page_config(page_title="Unit Convertor", layout="centered")

# Title
st.title("Unit Convertor")

github_repo_url = "https://github.com/furqanalikhan1/convertor.py/blob/main/convertor.py"

unit_conversions = {
    "Length": {"Meters": 1, "Kilometers": 0.001, "Miles": 0.000621371, "Feet": 3.28084},
    "Weight": {"Kilograms": 1, "Grams": 1000, "Pounds": 2.20462, "Ounces": 35.274},
    "Speed": {"Meters per second": 1, "Kilometers per hour": 3.6, "Miles per hour": 2.23694}
}

category = st.selectbox("Select Conversion Category", list(unit_conversions.keys()))
from_unit = st.selectbox("Convert from", list(unit_conversions[category].keys()))
to_unit = st.selectbox("Convert to", list(unit_conversions[category].keys()))
value = st.number_input("Enter the value to convert:", min_value=0.0, step=0.01)

if st.button("Convert"):
    converted_value = value * (unit_conversions[category][to_unit] / unit_conversions[category][from_unit])
    st.success(f"✅ Converted Value: {converted_value:.4f} {to_unit}")

    st.markdown("### 📝 How This Works")
st.write("""
1️⃣ **Select a category** (Length, Weight, or Speed).  
2️⃣ **Choose units** from which you want to convert and the target unit.  
3️⃣ **Enter a value** and press **Convert** to see the result.  
""")

st.markdown(f"🔗 [View Source Code on GitHub]({https://github.com/furqanalikhan1/convertor.py/edit/main/convertor.py})")
