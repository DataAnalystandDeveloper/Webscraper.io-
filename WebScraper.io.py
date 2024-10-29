import requests
from bs4 import BeautifulSoup
import re
import pandas as pd
import os


URL ='https://webscraper.io/test-sites/e-commerce/allinone/computers/tablets'
page = requests.get(URL)
### print(page) when the response is 200 then the access was approved

soup=BeautifulSoup(page.text, 'lxml')
### print(soup) verify if you get the html website in your output

product_name = soup.find_all('a', class_ = 'title')
##print(product_name)
price = soup.find_all('h4', class_ = 'price float-end card-title pull-right')
##print(price)
reviews = soup.find_all('p', class_ = re.compile('review-count float-end'))
##print(reviews)
description = soup.find_all('p', class_ = 'description card-text')
##print(description)

product_name_list =[]
for i in product_name:
    name = i.text
    product_name_list.append(name)
##print(product_name_list)

price_list =[]
for i in price:
    price2 = i.text
    price_list.append(price2)
##print(price_list)

reviews_list =[]
for i in reviews:
    reviews2 = i.text
    reviews_list.append(reviews2)
##print(reviews_list)

descriptions_list =[]
for i in description:
    description2 = i.text
    descriptions_list.append(description2)
##print(descriptions_list)

table = pd.DataFrame({'Product Name': product_name_list, 'Description' : descriptions_list, 'Price' : price_list, 'Reviews' : reviews_list})

directory = r'C:\Users\jespinoza\Desktop\Python\Webscraping outputs'
filename = 'products.xlsx'
full_path = os.path.join(directory, filename)

# Ensure the directory exists
os.makedirs(directory, exist_ok=True)

# Export to an Excel file without index
table.to_excel(full_path, index=False)

print(f"Data exported to '{full_path}'")

