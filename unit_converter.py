import streamlit as st

st.markdown(
    """
    <style>
    .header {
        font-size: 40px;
        font-weight: bold;
        color: #4CAF90;
        text-align: center;
        padding: 10px;
        background-color: #f0f0f0;
        border-radius: 10px;
    }
    .stButton button {
        background-color: #4CAF90;
        color: white;
        font-size: 18px;
        border-radius: 10px;
        padding: 10px 20px;
    }
    .stButton button:hover {
        background-color:;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Header
st.markdown('<div class="header">🌍 UNIT CONVERTER APP</div>', unsafe_allow_html=True)
st.markdown("### Converts length, weight, and time instantly")
st.write("WELCOME 🤍 Select a category, enter a value, and get the converted result in real time.")

# Define the convert_units function
def convert_units(category, value, unit):
    if category == "Length":
        if unit == "kilometers to miles":
            return value * 0.621371, "miles"
        elif unit == "miles to kilometers":
            return value * 1.60934, "kilometers"  
    elif category == "Weight":
        if unit == "kilograms to pounds":
            return value * 2.20462, "pounds"
        elif unit == "pounds to kilograms":
            return value / 2.20462, "kg"
    elif category == "Time":
        if unit == "seconds to minutes":
            return value / 60, "minutes"
        elif unit == "minutes to seconds":
            return value * 60, "seconds"
        elif unit == "minutes to hours":
            return value / 60, "hours"
        elif unit == "hours to minutes":
            return value * 60, "minutes"
        elif unit == "hours to days":
            return value / 24, "days"
        elif unit == "days to hours":
            return value * 24, "hours"

# Sidebar for inputs
with st.sidebar:
    st.header("Inputs")
    category = st.selectbox("Select a category:", ["Length", "Weight", "Time"])
    
    if category == "Length":
        unit = st.selectbox("📏 Select conversion", ["kilometers to miles", "miles to kilometers"])
    elif category == "Weight":
        unit = st.selectbox("⚖️ Select conversion", ["kilograms to pounds", "pounds to kilograms"])
    elif category == "Time":
        unit = st.selectbox("⏱️ Select conversion", ["seconds to minutes", "minutes to seconds", "minutes to hours", "hours to minutes", "hours to days", "days to hours"])
    
    value = st.number_input("Enter the value to convert.")

# Convert button
if st.button("Convert"):
    with st.spinner("Converting..."):
        result, result_unit = convert_units(category, value, unit)  # Call the function
        st.markdown(
            f"""
            <div style="
                background-color: #4CAF90;
                padding: 20px;
                border-radius: 10px;
                text-align: center;
                color: white;
                font-size: 24px;
            ">
                The result is <strong>{result:.2f} {result_unit}</strong>
            </div>
            """,
            unsafe_allow_html=True
        )

# Footer
st.markdown("---")
st.markdown(
    """
    <div style="text-align: center; color: gray;">
        Made by 🤍 YOUSRA KHAN
    </div>
    """,
    unsafe_allow_html=True
)