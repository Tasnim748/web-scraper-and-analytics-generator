import streamlit as st
import pandas as pd

def render_clean_data():
    st.header("3. Data Clean")
    
    # Check if we have data from uploaded file or scraper
    if 'data' not in st.session_state or not isinstance(st.session_state.data, pd.DataFrame):
        st.info("Please upload a file or scrape data first")
        return
    
    df = st.session_state.data