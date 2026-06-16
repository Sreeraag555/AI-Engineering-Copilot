import streamlit as st

st.set_page_config(
    page_title="AI Engineering Copilot",
    page_icon="🤖"
)

st.title("🤖 AI Engineering Copilot")

uploaded_file = st.file_uploader(
    "Upload a Python file or Notebook",
    type=["py", "ipynb"]
)

if uploaded_file:
    st.success(f"{uploaded_file.name} uploaded successfully!")