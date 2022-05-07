from datetime import datetime
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import requests
import lxml
import re


# --- Block for url and user-agent ---
rental_listing = "https://www.zillow.com/homes/for_rent/1-_beds/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22mapBounds%22%3A%7B%22west%22%3A-122.67022170019531%2C%22east%22%3A-122.19643629980469%2C%22south%22%3A37.59787529779996%2C%22north%22%3A37.95228287439649%7D%2C%22mapZoom%22%3A11%2C%22isMapVisible%22%3Afalse%2C%22filterState%22%3A%7B%22price%22%3A%7B%22max%22%3A872627%7D%2C%22beds%22%3A%7B%22min%22%3A1%7D%2C%22fore%22%3A%7B%22value%22%3Afalse%7D%2C%22mp%22%3A%7B%22max%22%3A3000%7D%2C%22auc%22%3A%7B%22value%22%3Afalse%7D%2C%22nc%22%3A%7B%22value%22%3Afalse%7D%2C%22fr%22%3A%7B%22value%22%3Atrue%7D%2C%22fsbo%22%3A%7B%22value%22%3Afalse%7D%2C%22cmsn%22%3A%7B%22value%22%3Afalse%7D%2C%22fsba%22%3A%7B%22value%22%3Afalse%7D%7D%2C%22isListVisible%22%3Atrue%7D"
google_url_short = "https://forms.gle/Lvdxatb15YCKVLyG9"
headers = {
    "Accept": "*/*",
    "User-Agent": "Mozilla/5.0 (iPad; CPU OS 11_0 like Mac OS X) AppleWebKit/604.1.34 (KHTML, like Gecko) Version/11.0 Mobile/15A5341f Safari/604.1"
    }

# --- Block time ---
today = datetime.today().strftime('%Y-%m-%d')

# --- Block to write all webpage to file.html ---
# response = requests.get(url=rental_listing, headers=headers)
# with open(f'file_{today}.html', 'w') as file:
#     file.write(response.text)

# --- Block to work directly with webpage ---
# response = requests.get(url=rental_listing, headers=headers)
# rent_site = response.text

# --- Block to open saved webpage file.txt ---
# with open('file.txt', 'r') as file:
#     rent_site = file.read()
# soup = BeautifulSoup(rent_site, 'html.parser')

# --- Block to open saved webpage file.html ---
with open(f'file_{today}.html', 'r') as file:
    rent_site = file.read()
soup = BeautifulSoup(rent_site, 'lxml')

links = []
prices = []
addresses = []

# --- Block to find search all items on webpage ---
rent_link = soup.find_all(class_="list-card-link")
rent_price = soup.find_all(class_="list-card-price")
rent_address = soup.find_all(class_="list-card-addr")

for i in range(3):
    links.append(rent_link[i].get('href'))
    prices.append(rent_price[i].text)
    addresses.append(rent_address[i].text)

# print(links)
# print(prices)
# print(addresses)


# --- Block for selenium ---
chrome_driver_path = "/Users/dsannikov/Documents/GitHub/ParsingPages/driver/chromedriver"
driver = webdriver.Chrome(executable_path=chrome_driver_path)
url = "https://docs.google.com/forms/d/e/1FAIpQLSf0HrBzF6jTLQBHeitlqTQm9wewg994RJwtb456Fy4WY7DbbA/viewform"
driver.get(url=url)


for i in range(3):
    address_box = driver.find_element(By.XPATH, "//*[@id='mG61Hd']/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input")
    time.sleep(5)
    address_box.send_keys(f"{str(addresses[i])}" + Keys.ENTER)
    time.sleep(5)
    price_box = driver.find_element(By.XPATH, "//*[@id='mG61Hd']/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input")
    time.sleep(5)
    price_box.send_keys(f"{str(prices[i])}" + Keys.ENTER)
    time.sleep(5)
    link_box = driver.find_element(By.XPATH, "//*[@id='mG61Hd']/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input")
    time.sleep(5)
    link_box.send_keys(f"{str(links[i])}" + Keys.ENTER)
    time.sleep(5)
    search_button = driver.find_element(By.XPATH, "//*[@id='mG61Hd']/div[2]/div/div[3]/div[1]/div[1]/div")
    time.sleep(5)
    search_button.send_keys(Keys.ENTER)
    time.sleep(5)
    search_button = driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div[1]/div/div[4]/a")
    time.sleep(5)
    search_button.send_keys(Keys.ENTER)
    time.sleep(5)


driver.close()
driver.quit()

