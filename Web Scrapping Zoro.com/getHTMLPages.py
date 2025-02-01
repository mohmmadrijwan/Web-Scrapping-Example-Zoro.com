import requests
import time
import os
from fake_useragent import UserAgent

# Headers for site
headers = {
        'User-Agent' : UserAgent().random,
        'Accept-Language' : 'en-US,en;q=0.9',
        'Accept-Encoding' : 'gzip, deflate, br',
        'Connection' : 'keep-alive',
        'Referer' : 'https://www.google.com'

    }

# for downloading web pages of Zoro.com from 1 to 20
for pageNum in range(1,20):

    # Replace this URL with the actual URL you want
    url = f"https://www.zoro.com/gloves-hand-protection/c/4448/?page={pageNum}"

    session = requests.Session() #create session
    
    time.sleep(2)
    #get the url
    res = session.get(url, headers=headers)
    
    #if product name folder is not created create one
    #here we are creating for Gloves product
    if not os.path.exists("Gloves"):
        os.makedirs("Gloves")
    
    #Write html page from 1 to 20 in product folder Gloves
    with open(f"Gloves/page_{pageNum}.html","w",encoding="utf-8") as f:
        f.write(res.text)