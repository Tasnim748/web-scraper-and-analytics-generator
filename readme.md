# Web Scraper Dashboard

A dynamic web scraping application that allows users to easily extract structured data from websites without writing any code. This tool is particularly useful for scraping product listings, book catalogs, and other structured content from modern websites, including those that use JavaScript to load data.

## Features

- **Scrape Dynamic Websites**: Leverages Playwright's headless Chrome browser to handle JavaScript-rendered content
- **Flexible Selector System**: Easily configure CSS selectors for different data fields
- **Multi-page Scraping**: Support for pagination with configurable page patterns
- **Data Analysis**: Basic analysis and visualization of scraped data
- **Export Options**: Download scraped data as CSV files

## Technology Stack

- **Python**: Core programming language
- **Playwright**: Headless browser automation library for scraping JavaScript-heavy websites
- **Streamlit**: Interactive web application framework for the user interface
- **Pandas**: Data manipulation and analysis
- **Matplotlib**: Data visualization

## How to Use

### 1. Installation

```bash
# Clone the repository
git clone <repository-url>
cd web-scraper-dashboard

# Create and activate virtual environment
python -m venv virtualEnv
source virtualEnv/bin/activate  # On Windows: virtualEnv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

### 2. Running the Application

```bash
streamlit run app.py
```

### 3. Scraping Data

The application has three main sections:

#### Scrape Data from Website
- **Target URL**: Enter the base URL of the website you want to scrape
- **Card Selector**: CSS selector that identifies each product/item card
- **Page Timeout**: Configure timeout in milliseconds
- **Pages to Scrape**: Select specific page numbers to scrape
- **Page URL Pattern**: Specify the pagination pattern (e.g., `?page` or `/pages/page`)
- **Field Selectors**: Define JSON mapping of field names to CSS selectors:

```json
{
  "title": "div.title h3",
  "price": "p.price span.text",
  "reviews": "div.reviews"
}
```

#### Data Analysis
- Upload previously scraped CSV files
- Select fields for basic statistical analysis

#### Visualization
- Create bar and line charts from your data
- Configure X and Y axes based on your dataset columns

## Example Use Case

1. To scrape products from an e-commerce site:
   - Enter the URL: `https://example.com/products`
   - Card Selector: `.product-card`
   - Timeout: `300000ms (300s)`
   - Pages: `1, 2, 3`
   - Page Pattern: `?page`
   - Field Selectors:
     ```json
     {
       "title": ".product-title",
       "price": ".price-current",
       "rating": ".rating-score",
       "availability": ".stock-status"
     }
     ```

2. Click "Scrape Data" and wait for the process to complete
3. Download the CSV file or perform analysis directly in the app

## Project Structure

- app.py: Main application entry point
- components: UI components for different sections of the app
- core: Core functionality including scraping, analysis, and visualization
- utils: Utility functions for URL building and other helpers

## Limitations

- Respects website terms of service - use responsibly
- Performance depends on the complexity of the target website
- Some websites may implement anti-scraping measures