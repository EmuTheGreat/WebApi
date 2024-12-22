import requests
from bs4 import BeautifulSoup
import aiohttp
from bs4 import BeautifulSoup
import asyncio

BASE_URL = "https://www.maxidom.ru"

async def fetch_page(session, url):
    async with session.get(url) as response:
        return await response.text()

async def parse_products_async():
    url = f"{BASE_URL}/catalog/stroitelnye-smesi/"
    product_data = []

    async with aiohttp.ClientSession() as session:
        while url:
            html = await fetch_page(session, url)
            soup = BeautifulSoup(html, 'html.parser')

            products = soup.find_all('div', class_='l-product__name')
            prices = soup.find_all('div', class_='l-product__price-base')

            for index in range(len(products)):
                try:
                    title = products[index].find('span').get_text(strip=True)
                    price = prices[index].get_text(strip=True)
                    product_data.append({"Название": title, "Цена": price})
                except AttributeError:
                    continue

            next_page = soup.find('a', {'id': 'navigation_2_next_page'})
            if next_page:
                url = BASE_URL + next_page['href']
                await asyncio.sleep(0.5)
            else:
                break

    return product_data


