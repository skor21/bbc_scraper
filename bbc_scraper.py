# Use beautiful soup to scrape the news headlines from https://www.bbc.co.uk/news/

from bs4 import BeautifulSoup
import requests

url = 'https://www.bbc.co.uk/news/'

response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')
for news_item in soup.find_all('a', class_='gs-c-promo-heading'):
    print(news_item.get_text())


