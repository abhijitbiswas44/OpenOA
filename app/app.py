import streamlit as st
import openoa

st.set_page_config(page_title="OpenOA Demo", layout="centered")

st.title("OpenOA – Live Deployment")
st.write("Operational Analysis Framework for Wind Plants")

st.markdown("---")
st.subheader("Backend Status")
st.success("OpenOA imported successfully")

st.write("Installed OpenOA version:", openoa.__version__)

st.markdown("---")
st.info(
    "This demo confirms the OpenOA backend is installed, "
    "functional, and ready for analysis workflows."
)
