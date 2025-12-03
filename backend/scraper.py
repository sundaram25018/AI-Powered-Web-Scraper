from playwright.async_api import async_playwright
from bs4 import BeautifulSoup

async def scrape_website(url: str) -> str:
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        page = await browser.new_page()
        try:
            await page.goto(url, timeout=60000)
            # Wait for some content to load if necessary
            # await page.wait_for_selector('body')
            
            content = await page.content()
            
            # Clean up HTML to extract text
            soup = BeautifulSoup(content, 'html.parser')
            
            # Remove script and style elements
            for script in soup(["script", "style"]):
                script.decompose()
                
            text = soup.get_text(separator=' ', strip=True)
            return text
            
        except Exception as e:
            print(f"Error scraping {url}: {e}")
            raise e
        finally:
            await browser.close()
