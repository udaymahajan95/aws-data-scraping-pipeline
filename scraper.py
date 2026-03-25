import requests
from bs4 import BeautifulSoup
import json
import boto3

url = "https://books.toscrape.com/"

response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

books = []

items = soup.find_all("article", class_="product_pod")

for item in items:
    name = item.h3.a["title"]
    price = item.find("p", class_="price_color").text
    rating = item.find("p", class_="star-rating")["class"][1]

    books.append({
        "name": name,
        "price": price,
        "rating": rating
    })

with open("books.json", "w") as f:
    json.dump(books, f)

s3 = boto3.client("s3")

s3.upload_file(
    "books.json",
    "scraping-data-uday",
    "raw/books.json"
)

print("Uploaded to S3")
