from firecrawl import FirecrawlApp
from config import Config

def scrape_url(url):
    """Scrapes a website and returns clean Markdown text."""
    app = FirecrawlApp(api_key=Config.FIRECRAWL_API_KEY)
    try:
        result = app.scrape_url(url, params={'formats': ['markdown']})
        return result.get('markdown', '')
    except Exception as e:
        return f"Could not scrape {url}: {str(e)}"