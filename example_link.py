# -*- coding: utf-8 -*-
"""
Created on Wed Nov 15 14:10:42 2023

@author: alex-
"""

import requests
from bs4 import BeautifulSoup as BS
from time import sleep

# list_card_url = []
headers = {'User-Agent' : 
           'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36 Edg/119.0.0.0'}
def get_url():
    for count in range(1, 8):
        
        url = 'https://scrapingclub.com/exercise/list_basic/?page={count}'
        response = requests.get(url, headers = headers)

        soup = BS(response.text, 'lxml')

        data = soup.find_all('div', class_='w-full rounded border')    
        # print(data)

        for i in data:
            # name = i.find('h4').text.replace("\n", "")
            # price = i.find('h5').text
            # url_img = "https://scrapingclub.com" + i.find('img', class_ = 'card-img-top img-fluid').get('src') # помогает получить значение атрибута
            # print(name + "\n" + price + "\n" + url_img + "\n\n")
            card_url = "https://scrapingclub.com" + i.find("a").get("href")
            yield card_url

        
for card_url in get_url():
    response = requests.get(card_url, headers = headers)
    sleep(3)

    soup = BS(response.text, 'lxml')

    data = soup.find('div', class_='my-8 w-full rounded border')   
    name = data.find('h3', class_ = 'card-title').text
    price = data.find('h4', class_= 'my-4 card-price').text
    text = data.find('p', class_ = 'card-description').text
    url_img = "https://scrapingclub.com" + data.find('img', class_ = 'card-img-top').get('src') # помогает получить значение атрибута
    print(name + "\n" + price + "\n" + text+ "\n" + url_img + "\n\n")
    
    
    

    



    
