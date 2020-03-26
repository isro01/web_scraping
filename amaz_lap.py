from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd 

driver = webdriver.Chrome()

products =[]   #to store name of the product
prices =[]    
ratings =[]

driver.get('https://www.amazon.in/s?k=laptop&ref=nb_sb_noss_2')

content = driver.page_source
soup = BeautifulSoup(content, "lxml")
for a in soup.findAll('a',href=True, attrs={'class':'a-link-normal a-text-normal'}):
    name = a.find('span', attrs={'class':'a-size-medium a-color-base a-text-normal'}).text
    products.append(name)
for a in soup.findAll('a',href=True,attrs={'class':'a-size-base a-link-normal s-no-hover a-text-normal'}):
    price = a.find('span', attrs={'class':'a-offscreen'}).text
    prices.append(price)

laptops = len(products)
prices_n = len(prices)
for i in range(0,(laptops-prices_n)):
    prices.append('Unavailable')
    
df = pd.DataFrame({'Product Name':products, 'Price':prices})
df.to_csv('laptops_amazon.csv', index=False, encoding='utf-8')
