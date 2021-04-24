#%%

import requests
from bs4 import BeautifulSoup

URL = ('https://steamladder.com/')
page = requests.get(URL)

soup = BeautifulSoup(page.content, 'html.parser')

stats = soup.find_all('tr')

for stat in stats:
    if stat.has_attr('onclick'):
        steamName = stat.find(class_='full')
        steamLevel = stat.find(class_='stat level relevant')
        try:
            print('Name: ' + steamName.text.strip() + '\nLevel: ' + steamLevel.text.strip() + '\n')
        except:
            print('NO DATA')