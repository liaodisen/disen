import requests
from bs4 import BeautifulSoup

link = 'https://www.point2homes.com/CA/Real-Estate-Listings.html?LocationGeoId=749568&LocationGeoAreaId=&Location=Regina%2C+SK'
r = requests.get(link)

soup = BeautifulSoup(r.text, 'lxml')
house_list = soup.find_all('div', class_="item-cnt clearfix golden")
for house in house_list:
    address = house.find('div', class_='item-address').text.strip()
    price = house.find('span', class_='green').span.text.strip()
    print(price)
    

