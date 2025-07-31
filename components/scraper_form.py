import streamlit as st
import pandas as pd
import json
import asyncio
from core.scraper import scrape_data
from core.utils.sessionOps import save_to_session_state

def render_scraper_form():
    st.header("1. Scrape Data from Website")

    with st.form("scrape_form"):
        url = st.text_input("Target URL", "")
        card_selector = st.text_input("Card Selector (CSS)", "")
        page_timeout = st.number_input("Page Timeout (ms)", min_value=1000, value=12000, step=1000)
        pages = st.multiselect("Select Pages to Scrape", options=list(range(1, 21)))
        pagePattern = st.text_input("Page URL Pattern (optional)", "")
        selectors_json = st.text_area(
            "Field Selectors (JSON)", 
            value='{\n  "title": ".title",\n  "price": ".price"\n}'
        )
        submitted = st.form_submit_button("Scrape Data")

    if submitted:
        try:
            selectors = json.loads(selectors_json)

            # Show the info message before starting the scraping process
            info_placeholder = st.empty()
            info_placeholder.info("Scraping in progress... Please wait.")
            data = asyncio.run(
                scrape_data(
                    url,
                    card_selector,
                    page_timeout=page_timeout,
                    pages=pages if pages else None,
                    pagePattern=pagePattern if pagePattern else None,
                    **selectors
                )
            )

            # Clear the "in progress" message
            info_placeholder.empty()

            if data:
                df = pd.DataFrame(data)
                st.success("Scraping complete!")
                st.write("### Scraped Data Preview", df.head())
                save_to_session_state('data', df)
                csv = df.to_csv(index=False).encode('utf-8')
                st.download_button("Download CSV", csv, "scraped_data.csv", "text/csv")
            else:
                st.warning("No data scraped. Please check your selectors and URL.")
        except Exception as e:
            st.error(f"Error: {e}")