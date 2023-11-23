import os
import time
import requests
from bs4 import BeautifulSoup

def fetch_latest_news():
    """
    Fetch news from some News API or web scraping.
    """
    # This is a placeholder for the real news fetching logic
    response = requests.get('https://newsapi.org/v2/top-headlines?country=us&apiKey=b5b9a807cf6649128b07b112213b234d')
    return response.json()['articles'][0]['title']

while True:
    with open("README.md", "a") as readme_file:
        news = fetch_latest_news()
        readme_file.write(news + "\n")
    os.system('git config --local user.email "action@github.com"')
    os.system('git config --local user.name "GitHub Action"')
    os.system('git commit -am "Updated with latest news"')
    os.system('git push')
    time.sleep(10) # sleep for 1 hour
