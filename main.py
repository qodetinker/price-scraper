import requests
from bs4 import BeautifulSoup
from datetime import datetime
import config as c
import math


def get_price(url_list, attribute_list):
    for color, url in url_list.items():
        og_price = float()
        new_price = float()

        if requests.get(url):
            print(f'Requesting URL for {color}')
            page = requests.get(url)
            soup = BeautifulSoup(page.content, 'html.parser')
            
            print('Looking for attributes')
            for count, target_atrribute in enumerate(attribute_list):
                tag = soup.find('div', attrs={'data-test': target_atrribute})
                try:
                    if count == 0:
                        og_price = float(tag.string[1:])
                    else:
                        new_price = float(tag.string[1:])
                except AttributeError as err:
                    continue
                    
    sale_price = og_price - new_price    
    if sale_price > 0: 
        price = math.floor(sale_price)
        print(f'There is a sale of ${price} OFF!! for ${new_price}')

if __name__ == '__main__':
    print(f'**** Start Time: {datetime.now().strftime("%A %B %d %I:%M %S %p %Y")}\n')
    
    # Nike Gear
    get_price(c.nike_gear, c.nike_attribute)
    
    print(f'**** End Time: {datetime.now().strftime("%A %B %d %I:%M %S %p %Y")}\n')