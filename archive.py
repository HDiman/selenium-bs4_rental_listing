
# =====================================================================================
# google_url = "https://docs.google.com/forms/d/e/1FAIpQLSf0HrBzF6jTLQBHeitlqTQm9wewg994RJwtb456Fy4WY7DbbA/viewform?usp=sf_link"

# =====================================================================================
href_tags = soup.find_all(href=True)

# =====================================================================================
with open(f'file_{today}.json', 'w', encoding='utf-8') as file:
    json.dump(file, file, ensure_ascii=False, indent=4)

# =====================================================================================
# --- Block to find all href from webpage file.html ---
for a in soup.find_all('a', href=True):
    print("Found the URL:", a['href'])

#  --- Block to find search 1 item ---
rent_link = soup.find(class_="list-card-link")["href"]
rent_price = soup.find(class_="list-card-price").text
rent_address = soup.find(class_="list-card-addr").text

print(rent_link)
print(rent_price)
print(rent_address)

--- Block to find search all items on webpage ---
rent_link = soup.find(class_="list-card-link")
rent_price = soup.find_all(class_="list-card-price")
rent_address = soup.find_all(class_="list-card-addr")

for link in rent_link:
    try:
        print(link["href"])
    except KeyError:
        pass

rent_all = soup.select("l//*[@id='grid-search-results']/ul/li[1]")
print(rent_all)

for item in rent_all:
    print(item.text)

for tag in soup.find_all(True):
    print(tag.name)

body_ul = soup.body.ul
print(body_ul)

# store_list = [item.get_attribute("id") for item in items]
# store_list.reverse()

find_by_a_tag = soup.find(id="grid-search-results").find("ul")
for item_a in find_by_a_tag:
    # print(item_a.get('href'))
    print(item_a)

find_by_id = soup.find(id="zpid_2064093318")
print(find_by_id)


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
driver = webdriver.Firefox()

# Navigate to url
driver.get("http://www.google.com")

# Enter "webdriver" text and perform "ENTER" keyboard action
driver.find_element(By.NAME, "q").send_keys("webdriver" + Keys.ENTER)


enter_box = driver.find_element(By.XPATH, "//*[@id='SMMuxb']/a[1]")
time.sleep(5)
enter_box.send_keys(Keys.ENTER)
time.sleep(5)

input_email = driver.find_element(By.XPATH, "//*[@id='view_container']/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div[1]/div/div[1]/div/div[1]/div")
time.sleep(5)
input_email.send_keys("dsannikov@gmail.com" + Keys.ENTER)
time.sleep(5)