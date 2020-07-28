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

with open("product_data.csv", "a") as csv_file:
    writer = csv.writer(csv_file)

    # Appends each beer to CSV file
    for product_elem in product_elems:
        title_elem = product_elem.find('a', class_='product-item__title')
        price_elem = product_elem.find('span', class_='product-item__price')
        # Replace fixes apostrophe problem in titles
        name = {title_elem.text.replace("'", "")}
        price = {price_elem.text}
        writer.writerow([name, price])










