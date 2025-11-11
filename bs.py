from bs4 import BeautifulSoup
from selenium import webdriver
import requests
driver = webdriver.Chrome()
driver.get('https://automatetheboringstuff.com/3e/chapter14.html')
url = "https://automatetheboringstuff.com/3e/chapter14.html"
response = requests.get(url)
html_content = response.text
soup = BeautifulSoup(html_content, 'html.parser')

title = soup.title.string
print(f"Title of the page: {title}")

links = soup.find_all('a')
print(f"Number of links on the page: {len(links)}")
for link in links:
    print(link.get('href'))