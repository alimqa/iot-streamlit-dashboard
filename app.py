import streamlit as st
import pandas as pd
import random
from datetime import datetime

st.title(" IoT Temperature & Humidity Dashboard")

if "data" not in st.session_state:
    st.session_state.data = pd.DataFrame(
        columns=["Time", "Temperature (°C)", "Humidity (%)"]
    )

if st.button(" Collect IoT Sensor Data"):
    new_data = {
        "Time": datetime.now().strftime("%H:%M:%S"),
        "Temperature (°C)": round(random.uniform(20, 30), 2),
        "Humidity (%)": round(random.uniform(40, 70), 2)
    }
    st.session_state.data = pd.concat(
        [st.session_state.data, pd.DataFrame([new_data])],
        ignore_index=True
    )

st.subheader(" Latest Sensor Data")
st.dataframe(st.session_state.data.tail(5))

st.subheader(" Sensor Data Visualization")
if not st.session_state.data.empty:
    st.line_chart(
        st.session_state.data.set_index("Time")[["Temperature (°C)", "Humidity (%)"]]
    )
else:
    st.info("No data collected yet.")
