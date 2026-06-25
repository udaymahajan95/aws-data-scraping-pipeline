import json
import boto3
import requests
from bs4 import BeautifulSoup


URL = "https://books.toscrape.com/"
BUCKET_NAME = "scraping-data-uday"
FILE_NAME = "books.json"
S3_KEY = "raw/books.json"


def scrape_books():
    """Scrape book data from BooksToScrape."""

    print("Fetching website...")

    response = requests.get(URL, timeout=30)
    response.raise_for_status()

    soup = BeautifulSoup(response.text, "html.parser")

    books = []

    items = soup.find_all("article", class_="product_pod")

    for item in items:
        try:
            name = item.h3.a["title"]
            price = item.find("p", class_="price_color").text.strip()
            rating = item.find("p", class_="star-rating")["class"][1]

            books.append({
                "name": name,
                "price": price,
                "rating": rating
            })

        except Exception as e:
            print(f"Error processing book: {e}")

    return books


def save_to_json(data):
    """Save scraped data to JSON file."""

    with open(FILE_NAME, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4)

    print(f"Saved {len(data)} records to {FILE_NAME}")


def upload_to_s3():
    """Upload JSON file to S3."""

    s3 = boto3.client("s3")

    s3.upload_file(
        FILE_NAME,
        BUCKET_NAME,
        S3_KEY
    )

    print(f"Uploaded to s3://{BUCKET_NAME}/{S3_KEY}")


def main():
    try:
        books = scrape_books()

        if not books:
            print("No books found.")
            return

        save_to_json(books)
        upload_to_s3()

        print("Scraping completed successfully!")

    except requests.exceptions.RequestException as e:
        print(f"Website request failed: {e}")

    except Exception as e:
        print(f"Unexpected error: {e}")


if __name__ == "__main__":
    main()
