import sys
import os
# Add the current directory to path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

import streamlit as st

# Import components
from components.header import render_header
from components.scraper_form import render_scraper_form
from components.data_analysis import render_data_analysis
from components.visualization import render_visualization

def main():
    # Set page configuration
    st.set_page_config(
        page_title="Web Scraper Dashboard",
        layout="wide"
    )
    
    # Render components
    render_header()
    render_scraper_form()
    render_data_analysis()
    render_visualization()

if __name__ == "__main__":
    main()