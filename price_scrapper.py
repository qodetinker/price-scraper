import requests
from bs4 import BeautifulSoup

URL = 'https://www.nike.com/t/pro-mens-long-sleeve-top-sDW22X/BV5594-011'

page = requests.get(URL)
print(page.status_code)

soup = BeautifulSoup(page.content, 'html.parser')

target_class = 'product-price css-11s12ax is--current-price'

results = soup.find(id='PDP')

for result in results:
    price = result.find('div', class_=target_class)

    if price.text == '$35':
        print(price.text)