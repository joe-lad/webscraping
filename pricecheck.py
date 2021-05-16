# imports
import subprocess
try:
    import requests
    import time
    import random
    from datetime import datetime
    from bs4 import BeautifulSoup
    import matplotlib.pyplot as plt
    import pylab
except:
    subprocess.run('python3 -m pip install requests')

userURL = input('enter curency: ')

URL = (f'https://coinmarketcap.com/currencies/{userURL}/')

dat=[0, 50000]
fig = plt.figure()
ax = fig.add_subplot(111)
Ln, = ax.plot(dat)
ax.set_xlim([0,1000])
ax.set_ylim([0,60000])
plt.ion()
plt.show() 

while True:

    now = datetime.now()

    try:
        page = requests.get(URL)
    except:
        print('couldnt find that crypto...')
        exit()

    soup = BeautifulSoup(page.content, 'html.parser')

    value = soup.find('div', class_='priceValue___11gHJ')

    timenow = now.strftime("%H:%M:%S")

    dat.append(float(value.text[1:].replace(',', '')))
    Ln.set_ydata(dat)
    Ln.set_xdata(range(len(dat)))
    plt.pause(5)
    print(value.text, timenow)