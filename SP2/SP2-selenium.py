from selenium import webdriver
from apartment import Apartment
# import module
from bs4 import BeautifulSoup


driver = webdriver.Chrome()

#1. Gå ind på boligportal.dk med selenium
#2. 2. Søg på københavn
location = 'københavn'
offset = 0
page = driver.get("https://www.boligportal.dk/lejeboliger/{location}/?offset={offset}".format(location=location, offset=offset))
print(type(page))

#3. Hent alle annoncer fra de seneste 24 timer (4 første sider)
#Appartment object
#type, price, square_meter
#xpath til heading 
# '//*[@id = "app"]/div[2]/div[1]/div/div/div[2]/div[8]/div/div[1]/div/a/div/div[2]/div/div/div[1]/div[1]'
# '#app > div:nth-child(3) > div:nth-child(1) > div > div > div.temporaryFlexColumnClassName.css-ssqjpe > div.css-lakxun > div > div:nth-child(1) > div > a > div > div.css-1qhcvyu > div > div > div.css-lywrpc > div.css-do1lz2'
# parse html content
soup = BeautifulSoup(page, 'html.parser')

mydivs = soup.find_all("div", {"class": "css-do1lz2"})
print(mydivs)
appart = Apartment('lejlighed', 5000, 70, "København, vesterbrogade", 2)
appartments = []

driver.quit()


