import requests
import time
from bs4 import BeautifulSoup

userFind = input('What would you like to find: ')
userPrice = float(input('What price would you like: £'))
userTimeout = int(input('Timeout seconds: '))

start_time = time.perf_counter()

URL = ('https://ebay.co.uk/sch/i.html?_from=R40&_trksid=p2380057.m570.l1313&_nkw='+userFind+'&_sacat=0&_udhi='+str(userPrice))
page = requests.get(URL)

soup = BeautifulSoup(page.content, 'html.parser')

# info = soup.find_all('div', class_='s-item__info clearfix')
# title = soup.find_all('h3', class_='s-item__title')

info = soup.find_all('div', class_='s-item__info clearfix')

for details in info:
    if time.perf_counter() > start_time + userTimeout:
        print('Timeout, exiting...')
        exit()

    # print(details)

    name = details.find('h3', class_='s-item__title')
    price = details.find('span', class_='s-item__price')
    link = details.find('a', href=True)

    if name != None:
        print('--------------------\n' + name.text + '\n' + 
        price.text + '\n' + link['href'] +'\n--------------------\n')

    # link = details.find('a', href=True)
    # name = details.find('span', class_='clipped')
    # price = details.find('span', class_='s-item__price')
    
    # print(name + '\n' + '£' + price + '\n' + link + '\n--------------------')

    # for prices in price:
    #     if prices <= userPrice:
    #         allprices.append(prices)
    # print(name['alt'] + '\n' + allprices + '\n' + link['href'] + '\n--------------------')
