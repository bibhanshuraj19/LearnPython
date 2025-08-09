import requests
from bs4 import BeautifulSoup

response = requests.get('https://www.geeksforgeeks.org/python/python-programming-language-tutorial/')
print(response.status_code)

soup = BeautifulSoup(response.content, 'html.parser')
# Find the main content container
content_div = soup.find('div', class_='article--viewer_content')
if content_div:
    for para in content_div.find_all('p'):
        print(para.text.strip())
else:
    print('No content found')

from selenium import webdriver

driver = webdriver.Firefox()
driver.get("https://www.google.co.in/ / search?q = geeksforgeeks")



