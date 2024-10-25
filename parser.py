import requests
from bs4 import BeautifulSoup
import json
import time

url = 'https://www.maxidom.ru/catalog/stroitelnye-smesi/'
product_data = []

while True:
    print(url)
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    products = soup.find_all('div', class_='l-product__name')
    prices = soup.find_all('div', class_='l-product__price-base')

    for index in range(len(products)):
        try:
            title = products[index].find('span').get_text(strip=True)
            price = prices[index].get_text(strip=True)

            product_data.append({
                'Название': title,
                'Цена': price
            })

        except AttributeError:
            continue

    next_page = soup.find('a', {'id': 'navigation_2_next_page'})
    if next_page:
        url = 'https://www.maxidom.ru' + next_page['href']
        time.sleep(0.5)
    else:
        break

print(product_data)