import requests
from bs4 import BeautifulSoup

# try to scrapy the first page of the website

houseFinder = requests.get('https://www.point2homes.com/CA/Real-Estate-Listings.html?LocationGeoId=749568&LocationGeoAreaId=&Location=Regina%2C+SK')
houseFinder_Content = BeautifulSoup(houseFinder.content, 'html.parser')
houseList1 = houseFinder_Content.find_all("div", class_="item-cnt clearfix gold")
for house in houseList1:
    address = house.find("div", class_="item-address").text.strip()
    price = house.find("span", class_="green").span.text.strip()
    info = house.find("div", class_="characteristics-cnt").text.strip()
    all_Info = address + "\n" + price + "\n" + info
    info_without_line = all_Info.splitlines()
    info_without_blank = list(filter(None, info_without_line))
    info_without_space = [info.replace(' ', '') for info in info_without_blank]
    print(info_without_space)


