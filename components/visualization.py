import streamlit as st
import pandas as pd
from core.visualize import plot_bar, plot_line

def render_visualization():
    st.header("3. Data Visualization")
    
    # Check if we have data from uploaded file or scraper
    if 'data' not in st.session_state or not isinstance(st.session_state.data, pd.DataFrame):
        st.info("Please upload a file or scrape data first")
        return
    
    df = st.session_state.data
    
    # Create visualization options
    col1, col2 = st.columns(2)
    
    with col1:
        x_field = st.selectbox("X-axis field", df.columns)
    
    with col2:
        # Filter to show only numeric columns for y-axis
        numeric_cols = df.select_dtypes(include=['number']).columns.tolist()
        if not numeric_cols:
            st.warning("No numeric columns found for visualization")
            return
        y_field = st.selectbox("Y-axis field (numeric)", numeric_cols)
    
    chart_type = st.radio("Chart Type", ["Bar", "Line"])
    
    if st.button("Generate Chart"):
        if chart_type == "Bar":
            fig = plot_bar(df, x_field, y_field)
            if fig:
                st.pyplot(fig)
        else:
            fig = plot_line(df, x_field, y_field)
            if fig:
                st.pyplot(fig)