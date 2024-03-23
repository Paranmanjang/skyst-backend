from utils.web_crawler import crawl_website
from utils.ai.summarizer import generate_summary

# POST /bookmarks
url = "https://www.mindorizip.tistory.com"
title, content = crawl_website(url)

# summarizer.py
result = generate_summary(content)
print(result)
