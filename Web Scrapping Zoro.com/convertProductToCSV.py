from bs4 import BeautifulSoup
import pandas as pd
import os

#data dictionary for storing product details
data = {"brand":[],"title":[],"Price":[],"Link":[]}


#loop till all the files in product folder
#here all the files in Gloves folder will be read one by one
for file in os.listdir("Gloves"): #change Gloves to your folder
    #read one file at a iteration
    with open(f"Gloves/{file}","r") as f:
        html_doc= f.read()
        
    soup = BeautifulSoup(html_doc, 'html.parser') #get inctance of BeautifulSoup for file

    #get all the brand name for product
    for title in soup.find_all(class_="brand-name"):
        data['brand'].append(title.get_text())
    #get all the title and link for product
    for title in soup.find_all(class_="product-title"):
        data['Link'].append("https://www.zoro.com/"+title.a['href'])
        data['title'].append(title.a.h3.get_text().strip())
    
    #get all the price for product
    for price in soup.find_all(class_="price-main"):
        data['Price'].append(price.get_text().strip())

# create csv using pandas
df = pd.DataFrame(data=data)
df.to_csv("gloves.csv")