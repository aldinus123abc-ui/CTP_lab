import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin


def scrape_news_headlines(url):
    headers = {
        "User-Agent": (
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
            "AppleWebKit/537.36 (KHTML, like Gecko) "
            "Chrome/124.0.0.0 Safari/537.36"
        )
    }

    try:
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status() 
    except requests.exceptions.RequestException as err:
        print(f"Error fetching the web page: {err}")
        return []

    soup = BeautifulSoup(response.text, "html.parser")

    extracted_articles = []
    seen_links = set()

    for tag in soup.find_all(["h1", "h2", "h3", "a"]):
        anchor = tag if tag.name == "a" else tag.find("a")
        if tag.name == "a" and not tag.find(["h1", "h2", "h3"]):
            continue

        if anchor and anchor.get("href"):
            headline_text = anchor.get_text(" ", strip=True)
            raw_link = anchor["href"].strip()
            full_url = urljoin(url, raw_link)
            if len(headline_text) >= 15 and full_url not in seen_links:
                seen_links.add(full_url)
                extracted_articles.append({
                    "headline": headline_text,
                    "url": full_url
                })

    return extracted_articles


def main():
    target_url = input("Enter news website URL (or press Enter for default): ").strip()
    if not target_url:
        target_url = "https://www.bbc.com/news"

    print(f"\nFetching headlines from: {target_url}...\n")
    articles = scrape_news_headlines(target_url)

    if not articles:
        print("No headlines found. The site may load content dynamically via JavaScript.")
        return

    print(f"Found {len(articles)} headlines:\n")
    for idx, item in enumerate(articles[:15], start=1):
        print(f"{idx}. {item['headline']}")
        print(f"   Link: {item['url']}\n")


if __name__ == "__main__":
    main()
