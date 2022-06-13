import requests
from bs4 import BeautifulSoup


def get_price():
    url = input('Enter the URL of the product : ')
    useragent = ''  # Google search 'my user agent'
    try:
        if 'amazon' in url:  # for amazon.in queries
            page = requests.get(url, headers={"User-Agent": useragent})
            soup = BeautifulSoup(page.content, 'html.parser')
            title = soup.find(id='productTitle').text.strip()
            price = float(soup.find(class_="a-offscreen").text.replace('₹', '').replace(',', ''))
            price1 = int(price)
            print(f"{title} : {price1}")
        elif 'flipkart' in url:  # for amazon.com queries
            page = requests.get(url, headers={"User-Agent": useragent})
            soup = BeautifulSoup(page.content, 'html.parser')
            title = soup.find(class_='B_NuCI').text
            price = int(soup.find(class_="_30jeq3 _16Jk6d").text.replace('₹', '').replace(',', ''))
            print(f"{title} : {price}")
    except Exception as e:
        print(e)


get_price()
