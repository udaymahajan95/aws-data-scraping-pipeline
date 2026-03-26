# 🚀 AWS Serverless Data Scraping Pipeline

## 📌 Project Overview
This project demonstrates an end-to-end data pipeline built on AWS that automatically scrapes, processes, and stores data.

The pipeline extracts data from a website, stores raw data in S3, processes it using AWS Lambda, and saves structured data in DynamoDB.

---

## 🏗️ Architecture

EC2 (Scraper)
   ↓
S3 (Raw Data Storage)
   ↓
Lambda (Processing)
   ↓
DynamoDB (Structured Data)

---

## ⚙️ Technologies Used

- Python
- AWS EC2
- Amazon S3
- AWS Lambda
- DynamoDB
- BeautifulSoup

---

## 🔄 Workflow

1. Python scraper runs on EC2.
2. Data is scraped from the website.
3. JSON file is uploaded to the S3 bucket.
4. S3 triggers AWS Lambda automatically.
5. Lambda processes the data.
6. Clean data is stored in DynamoDB.

---

## 📂 Project Structure
scraper.py
books.json


---

## 💻 Setup Instructions

**### 1. Install dependencies


```pip install requests beautifulsoup4 boto3

---

### 2. Run scraper

python scraper.py


---

## 📊 Output

- Raw data stored in S3
- Processed data stored in DynamoDB

---

## 🔐 IAM Roles Used

- S3 access for EC2
- S3 read + DynamoDB write for Lambda
- CloudWatch logging permissions

---

## 🚨 Challenges Faced

- S3 bucket not found error
- Lambda timeout issue
- IAM permission errors
- Debugging event triggers

---

## 🎯 Learning Outcomes

- Hands-on experience with AWS services
- Understanding event-driven architecture
- Real-world debugging and troubleshooting
- Cloud-based data pipeline design

---

## 👨‍💻 Author

Uday Mahajan



