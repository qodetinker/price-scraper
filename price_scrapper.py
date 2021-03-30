import requests
from bs4 import BeautifulSoup

long_sleeves = {'Grey': 'https://www.nike.com/t/pro-mens-long-sleeve-top-sDW22X/BV5594-011', 'Ocean Fog': 'https://www.nike.com/t/pro-mens-long-sleeve-top-sDW22X/BV5594-451'}

html_class = {'reg_price':'product-price css-11s12ax is--current-price', 'sale_price':'product-price is--current-price css-s56yt7'}

def get_price(url_list, og_price):
    ori_price = int(og_price)
    # Pass in the URL value
    for color, url in url_list.items():
        page = requests.get(url)
        #print(page.status_code)

        soup = BeautifulSoup(page.content, 'html.parser')
        
        for x in html_class.values():
            tags = soup.find_all(class_=x)

            for i in tags:
                c_price = float(i.string[1:])
                if c_price < ori_price:
                    print(f'There is a sale on {color}, the price is now {i.string}')



get_price(long_sleeves, 35)