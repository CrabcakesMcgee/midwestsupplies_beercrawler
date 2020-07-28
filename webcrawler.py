# 07/21/2020

import requests
from bs4 import BeautifulSoup
import csv

# a Python object (dict):


URL = 'https://www.midwestsupplies.com/collections/beer-brewing-recipe-kits'
page = requests.get(URL)

soup = BeautifulSoup(page.content, 'html.parser')
# results = soup.find(class_='product-item__details')
results = soup.find(id='bc-sf-filter-products')


product_elems = results.find_all('div', class_='product-item__details')

# print(results.prettify())


# for product_elem in product_elems:
#     # Each job_elem is a new BeautifulSoup object.
#     # You can use the same methods on it as you did before.
#     title_elem = product_elem.find('a', class_='product-item__title')
#     price_elem = product_elem.find('span', class_='product-item__price')
#     # name = {title_elem.text}
#     # price = {price_elem.text}

with open("product_data.csv", "a") as csv_file:
    writer = csv.writer(csv_file)

    for product_elem in product_elems:
        # Each job_elem is a new BeautifulSoup object.
        # You can use the same methods on it as you did before.
        title_elem = product_elem.find('a', class_='product-item__title')
        price_elem = product_elem.find('span', class_='product-item__price')
        name = {title_elem.text}
        price = {price_elem.text}
        writer.writerow([name, price])










