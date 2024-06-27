import streamlit as st
from utils import get_answer_csv

st.header("Chat with any CSV")
upload_file = st.file_uploader("Upload a CSV file", type = ['csv'])

if upload_file is not None:
    query = st.text_area("Ask any question related to the document")
    button = st.button("Submit")
    if button:
        st.write(get_answer_csv(upload_file, query))