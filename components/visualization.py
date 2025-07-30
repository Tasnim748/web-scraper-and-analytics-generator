import streamlit as st
import pandas as pd
from core.visualize import plot_bar, plot_line

def render_visualization():
    st.write("### Visualization")
    
    # Check if we have data from uploaded file
    if 'data' not in st.session_state:
        uploaded_file = st.session_state.get('uploaded_file', None)
        if uploaded_file:
            df = pd.read_csv(uploaded_file)
        else:
            st.info("Please upload a file in the data analysis section first")
            return
    else:
        df = st.session_state.data
    
    x_field = st.selectbox("X-axis field", df.columns)
    y_field = st.selectbox("Y-axis field (numeric)", df.columns)
    chart_type = st.radio("Chart Type", ["Bar", "Line"])
    
    if st.button("Plot Chart"):
        if chart_type == "Bar":
            plot_bar(df, x_field, y_field)
        else:
            plot_line(df, x_field, y_field)