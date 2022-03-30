from selenium import webdriver
from apartment import Apartment
from bs4 import BeautifulSoup
import requests
import pandas as pd
from datetime import date
import os

# 1. Gå ind på boligportal.dk med selenium
# 2. 2. Søg på københavn


def get_apartments_one_page(location, offset):

    appartments = []
    URL = "https://www.boligportal.dk/lejeboliger/{location}/?offset={offset}".format(
        location=location, offset=offset)
    # Page content from Boligportal.dk
    page = requests.get(URL)
    # parse html content
    soup = BeautifulSoup(page.content, 'html.parser')

    #headers = soup.find_all("div", {"class": "css-do1lz2"})
    # css-19j7wz6
    appartment_article = soup.find_all(
        "div", {"class": "temporaryFlexColumnClassName css-1p8oyon"})
    print(len(appartment_article))
    for article in appartment_article:
        # Get header data
        header = article.find("div", {"class": "css-do1lz2"})
        header_string = header.text.replace(' ', '')
        my_list = header_string.split('·')
        appertment_type = my_list[1]
        rooms = int(my_list[0][:-4])  # cut vær.
        square_meter = int(my_list[2][:-2])  # cut m2

        # get location data
        location = article.find("div", {"class": "css-1vahile"})
        location_string = location.text

        # get price
        price = article.find("span", {"class": "css-dpmn2u"})
        price_int = int(price.text.replace(".", "")[:-3])  # cut .kr + .

        # get link to verify
        link = article.find(
            "a", {"class": "AdCardSrp__Link css-1gsgxxt"})['href']
        link_string = 'www.boligportal.dk' + link  # add full link. not provied

        # get article created timestamp
        created = article.find('span', {"class": "css-1bremdn"})
        created_string = created.text

        # When the data was fetched
        fetched = date.today()

        #print(appertment_type, price_int, square_meter, location_string,rooms, link_string, created_string, fetched)
        # Create Appartment object:
        appart = Apartment(appertment_type, price_int, square_meter,
                           location_string, rooms, link_string, created_string, fetched)
        appartments.append(appart)
    return appartments


# 3. Hent alle annoncer fra de seneste 24 timer (4 første sider)
    # page number 1: offset=0, page number 2: offset=18, page number 3: offset=36
def scrape_more_pages(page_number, location):
    full_list = []
    for number in (n+1 for n in range(page_number)):
        if(number == 1):
            offset = 0
        else:
            offset = (page_number-1) * 18

        one_page_data = get_apartments_one_page(location, offset)
        full_list.extend(one_page_data)

        lst_type = []
        lst_price = []
        lst_square_meter = []
        lst_street = []
        lst_room = []
        lst_link = []
        lst_created = []
        lst_fetched = []

        for data in full_list:
            lst_type.append(data.type)
            lst_price.append(data.price)
            lst_square_meter.append(data.square_meter)
            lst_street.append(data.street)
            lst_room.append(data.room)
            lst_link.append(data.link)
            lst_created.append(data.created)
            lst_fetched.append(data.fetched)

        # Calling DataFrame constructor after zipping
        df = pd.DataFrame(list(zip(lst_type, lst_price, lst_square_meter, lst_street, lst_room, lst_link, lst_created, lst_fetched)),
                          columns=['type', 'price', 'square_meter', 'location', 'rooms', 'link', 'created', 'fetched'])
    return df


location = 'københavn'
number_of_pages = 3
final_df = scrape_more_pages(number_of_pages, location)
print(len(final_df))
print(final_df)
csv_path = os.getcwd() + "/boligportalen.csv"
final_df.to_csv(csv_path)
