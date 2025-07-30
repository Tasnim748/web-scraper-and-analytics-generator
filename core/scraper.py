import asyncio
from playwright.async_api import async_playwright

try:
    from .utils.buildPageUrl import build_page_url
except ImportError:
    from utils.buildPageUrl import build_page_url

async def scrape_data(
        url,
        card_selector, 
        scroll_times=5,
        scroll_pause=1000,
        page_timeout=60000,
        pages=None,
        pagePattern=None,
        **selectors):
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        page = await browser.new_page()
        
        data = []
        if pages:
            for pg in pages:
                currentUrl = build_page_url(url, pagePattern, pg)
                print("collecting data from page:", currentUrl)
                await page.goto(currentUrl, timeout=page_timeout)
                cards = await page.query_selector_all(card_selector)
                for product in cards:
                    item = {}
                    for key, selector in selectors.items():
                        el = await product.query_selector(selector)
                        text = await el.text_content() if el else "-"
                        item[key] = text.strip()
                    data.append(item)
        else:
            print("collecting data from page:", build_page_url(url))
            await page.goto(build_page_url(url), timeout=page_timeout)

            # Scroll to load more products if needed
            for _ in range(scroll_times):
                await page.evaluate("window.scrollTo(0, document.body.scrollHeight);")
                await page.wait_for_timeout(scroll_pause)

            cards = await page.query_selector_all(card_selector)  # Example selector
            for product in cards:
                item = {}
                for key, selector in selectors.items():
                    el = await product.query_selector(selector)
                    text = await el.text_content() if el else "-"
                    item[key] = text.strip()
                data.append(item)
        
        try:
            await browser.close()
        except:
            print("already closed")

        return data

if __name__ == "__main__":
    url = "https://chaldal.com/spices"
    card_selector = "div.product"
    selectors = {
        "title": "div.name",
        "quantity": "div.subText",
        "price": "div.discountedPrice span:nth-child(2)",
    }
    pages = [2,3]
    pagePattern = '?page'

    
    scraped_data = asyncio.run(
        scrape_data(
            url, 
            card_selector, 
            page_timeout=12000, 
            pagePattern=pagePattern, 
            **selectors
        )
    )
    print(scraped_data)
    print("Total products found:", len(scraped_data))