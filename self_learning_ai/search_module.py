import requests
from bs4 import BeautifulSoup
import time
import random
import urllib.parse

def search_web(query):
    """Enhanced web search with multiple strategies and better parsing"""
    print(f"🌐 Searching: {query}")

    # Try multiple search strategies
    strategies = [
        search_duckduckgo,
        search_wikipedia,
        search_google_fallback
    ]

    for strategy in strategies:
        try:
            result = strategy(query)
            if result and result != "No result found." and len(result) > 20:
                print(f"✅ Found result using {strategy.__name__}")
                return result
        except Exception as e:
            print(f"⚠️ {strategy.__name__} failed: {e}")
            continue

    # If all strategies fail, return a more informative message
    return f"Unable to find detailed information about '{query}'. This topic may require specialized knowledge or the search services are currently unavailable."

def search_duckduckgo(query):
    """Search using DuckDuckGo (more bot-friendly)"""
    encoded_query = urllib.parse.quote_plus(query)
    url = f"https://duckduckgo.com/html/?q={encoded_query}"

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    }

    response = requests.get(url, headers=headers, timeout=10)
    soup = BeautifulSoup(response.text, "html.parser")

    # Try different selectors for DuckDuckGo results
    selectors = [
        "a.result__snippet",
        ".result__snippet",
        ".result-snippet",
        ".snippet"
    ]

    for selector in selectors:
        snippets = soup.select(selector)
        if snippets:
            text = snippets[0].get_text().strip()
            if len(text) > 20:
                return text

    return "No result found."

def search_wikipedia(query):
    """Search Wikipedia API for reliable information"""
    try:
        # Wikipedia API search
        search_url = "https://en.wikipedia.org/api/rest_v1/page/summary/" + urllib.parse.quote(query.replace(" ", "_"))

        headers = {
            "User-Agent": "SelfLearningAI/1.0 (Educational Purpose)"
        }

        response = requests.get(search_url, headers=headers, timeout=10)

        if response.status_code == 200:
            data = response.json()
            if 'extract' in data and data['extract']:
                return data['extract']

        # If direct search fails, try Wikipedia search API
        search_api_url = "https://en.wikipedia.org/w/api.php"
        params = {
            "action": "query",
            "format": "json",
            "list": "search",
            "srsearch": query,
            "srlimit": 1
        }

        response = requests.get(search_api_url, params=params, headers=headers, timeout=10)
        data = response.json()

        if 'query' in data and 'search' in data['query'] and data['query']['search']:
            page_title = data['query']['search'][0]['title']
            summary_url = f"https://en.wikipedia.org/api/rest_v1/page/summary/{urllib.parse.quote(page_title)}"

            summary_response = requests.get(summary_url, headers=headers, timeout=10)
            if summary_response.status_code == 200:
                summary_data = summary_response.json()
                if 'extract' in summary_data:
                    return summary_data['extract']

    except Exception as e:
        print(f"Wikipedia search error: {e}")

    return "No result found."

def search_google_fallback(query):
    """Fallback Google search with better parsing"""
    encoded_query = urllib.parse.quote_plus(query)
    url = f"https://www.google.com/search?q={encoded_query}&hl=en"

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
        "Accept-Language": "en-US,en;q=0.5",
        "Accept-Encoding": "gzip, deflate",
        "Connection": "keep-alive",
    }

    # Add random delay to avoid rate limiting
    time.sleep(random.uniform(1, 3))

    response = requests.get(url, headers=headers, timeout=15)
    soup = BeautifulSoup(response.text, "html.parser")

    # Try multiple selectors for Google results
    selectors = [
        "div.BNeawe.s3v9rd.AP7Wnd",
        "div.VwiC3b",
        "span.aCOpRe",
        "div.kCrYT",
        "div.BNeawe",
        ".g .VwiC3b",
        ".rc .s"
    ]

    for selector in selectors:
        snippets = soup.select(selector)
        for snippet in snippets:
            text = snippet.get_text().strip()
            if len(text) > 30 and not text.startswith("http"):
                return text

    return "No result found."
