import streamlit as st
import pandas as pd
from core.analysis import basic_analysis

def render_data_analysis():
    st.header("2. Upload and Analyze Data")

    uploaded_file = st.file_uploader("Upload cleaned CSV data", type=["csv"])

    if uploaded_file:
        df = pd.read_csv(uploaded_file)
        st.write("### Data Preview", df.head())

        st.write("### Data Analysis")
        numeric_fields = st.multiselect("Select numeric fields for analysis", df.columns)
        text_fields = st.multiselect("Select text fields for analysis", df.columns)
        if st.button("Run Analysis"):
            basic_analysis(df, numeric_fields=numeric_fields, text_fields=text_fields)