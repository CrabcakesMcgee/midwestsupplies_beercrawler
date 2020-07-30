# 07/21/2020

import requests
from bs4 import BeautifulSoup
import csv
import pandas as pd

# Pulls data from url
URL = 'https://www.midwestsupplies.com/collections/beer-brewing-recipe-kits'
page = requests.get(URL)

# Parses page for relevent info
soup = BeautifulSoup(page.content, 'html.parser')
results = soup.find(id='bc-sf-filter-products')
# Finds all elements that meet criteria
product_elems = results.find_all('div', class_='product-item__details')

# print(results.prettify())

# Saves data as list to CSV file
with open("product_data.csv", "w") as csv_file:
    writer = csv.writer(csv_file)

    # Appends each beer to CSV file
    for product_elem in product_elems:
        title_elem = product_elem.find('a', class_='product-item__title')
        price_elem = product_elem.find('span', class_='product-item__price')
        # Replace fixes apostrophe problem in titles
        name = title_elem.text.replace("'", "").replace("Beer Recipe Kit", "")
        price = price_elem.text.replace("$", "").replace("From ", "")
        writer.writerow([name, price])

# Creates column names, and pulls data with Pandas
col_names = ['Beer', 'Price']
data = pd.read_csv("product_data.csv", names=col_names, header=None, encoding='cp1252')

# Creates Menu Options
answer = True
while answer:
    print("""
    1. Under $25
    2. $25 - $40
    3. Over $40
    4. All
    5. Exit/Quit
    """)

    answer = input("Option:  ")
    if answer == "1":
        print("Under $25")
        print(data.loc[data['Price'] < 25])
    elif answer == "2":
        print("$25 - $40")
        print(data.loc[data['Price'].between(25, 40)])
    elif answer == "3":
        print("Over $40")
        print(data.loc[data['Price'] > 40])
    elif answer == "4":
        print("All")
        print(data)
    elif answer == "5":
        print("Goodbye")
        answer = None
    else:
        print("\n Not a Valid Choice. Please choose between 1 and 5")









