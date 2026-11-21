import csv
import time
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin


def fetch_page(url):
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
        response.encoding = "utf-8"
        return response.text
    except requests.exceptions.RequestException as err:
        print(f"Error fetching {url}: {err}")
        return None


def parse_products(html, base_url):
    """Extracts product details from a catalog page's HTML."""
    soup = BeautifulSoup(html, "html.parser")
    products = []
    product_cards = soup.find_all("article", class_="product_pod")

    rating_map = {"One": 1, "Two": 2, "Three": 3, "Four": 4, "Five": 5}

    for card in product_cards:
        title_tag = card.find("h3").find("a")
        title = title_tag["title"].strip() if title_tag and title_tag.get("title") else "N/A"
        relative_link = title_tag["href"] if title_tag and title_tag.get("href") else ""
        product_url = urljoin(base_url, relative_link)
        price_tag = card.find("p", class_="price_color")
        price = price_tag.get_text(strip=True) if price_tag else "N/A"
        stock_tag = card.find("p", class_="instock availability")
        availability = stock_tag.get_text(strip=True) if stock_tag else "Unknown"

        rating_tag = card.find("p", class_="star-rating")
        rating_word = rating_tag["class"][1] if rating_tag and len(rating_tag["class"]) > 1 else ""
        rating = f"{rating_map.get(rating_word, 0)}/5"

        products.append({
            "Title": title,
            "Price": price,
            "Rating": rating,
            "Availability": availability,
            "Product_URL": product_url
        })

    return products


def save_to_csv(products, filename="scraped_products.csv"):
    """Writes a list of product dictionaries to a CSV file."""
    if not products:
        print("No product data to save.")
        return

    fieldnames = ["Title", "Price", "Rating", "Availability", "Product_URL"]

    with open(filename, mode="w", newline="", encoding="utf-8-sig") as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(products)

    print(f"Success: Saved {len(products)} products to '{filename}'.")


def main():
    base_url = "https://books.toscrape.com/catalogue/page-{}.html"
    all_products = []
    pages_to_scrape = 3 

    for page_num in range(1, pages_to_scrape + 1):
        target_url = base_url.format(page_num)
        print(f"Scraping page {page_num}: {target_url}")

        html = fetch_page(target_url)
        if html:
            page_products = parse_products(html, target_url)
            all_products.extend(page_products)

        time.sleep(1)

    save_to_csv(all_products, "ecommerce_products.csv")


if __name__ == "__main__":
    main()
