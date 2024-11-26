import requests
from bs4 import BeautifulSoup
from sqlalchemy.orm import Session
from crud import create_product
from schemas import ProductCreate

def parse_products(db: Session):
    url = 'https://www.maxidom.ru/catalog/stroitelnye-smesi/'

    while True:
        print(f"Парсинг: {url}")
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')

        products = soup.find_all('div', class_='l-product__name')
        prices = soup.find_all('div', class_='l-product__price-base')

        for index in range(len(products)):
            try:
                title = products[index].find('span').get_text(strip=True)
                price = prices[index].get_text(strip=True)

                product = ProductCreate(title=title, price=price)
                create_product(db, product)

            except AttributeError:
                continue

        next_page = soup.find('a', {'id': 'navigation_2_next_page'})
        if next_page:
            url = 'https://www.maxidom.ru' + next_page['href']
        else:
            break
