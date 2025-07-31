import streamlit as st
import pandas as pd
from core.analysis import basic_analysis

def render_data_analysis():
    st.header("2. Upload and Analyze Data")

    # Check if data exists in session state (from scraper_form or previous upload)
    if 'data' in st.session_state and isinstance(st.session_state.data, pd.DataFrame):
        df = st.session_state.data
        st.success("Using data from previous step")
        
        # Add option to clear the data and upload a different file
        if st.button("Clear data and upload new file"):
            st.session_state.pop('data', None)
            st.rerun()
    else:
        # If no data in session, show the file uploader
        uploaded_file = st.file_uploader("Upload cleaned CSV data", type=["csv"])
        
        if uploaded_file:
            df = pd.read_csv(uploaded_file)
            # Save to session state for other components to use
            st.session_state['data'] = df
        else:
            st.info("Please upload a CSV file or use the scraper to get data")
            return  # Exit the function if no data is available

    # Display data preview and analysis options
    st.write("### Data Preview", df.head())

    st.write("### Data Analysis")
    numeric_fields = st.multiselect("Select numeric fields for analysis", 
                                   [col for col in df.columns if pd.api.types.is_numeric_dtype(df[col])])
    text_fields = st.multiselect("Select text fields for analysis", 
                                [col for col in df.columns if pd.api.types.is_string_dtype(df[col])])
    
    if st.button("Run Analysis"):
        basic_analysis(df, numeric_fields=numeric_fields, text_fields=text_fields)