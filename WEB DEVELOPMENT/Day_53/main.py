from bs4 import BeautifulSoup
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException
import time


def rent_finder():
    rent_of_properties = soup.find_all(
        'span', class_="PropertyCardWrapper__StyledPriceLine")

    unwanted_text_in_price = ["+/mo", '+ 1bd',  '+ 1bd', "/mo"]
    actual_price = []
    for property in rent_of_properties:
        price = property.text

        for item in unwanted_text_in_price:
            price = price.replace(item, '')
        actual_price.append(price)

    return actual_price


def address_finder():
    address_of_property = soup.find_all('address')

    unwanted_symbols = ['|', '#']
    actual_address = []
    for item in address_of_property:
        address = item.text.strip()

        for symbol in unwanted_symbols:
            address = address.replace(symbol, '')
        actual_address.append(address)

    return actual_address


def address_link_finder():
    cards = soup.find_all('div', class_='StyledPropertyCardDataWrapper')
    property_link = []

    for card in cards:
        tag = card.find(
            'a', {'data-test': 'property-card-link'})

        if tag:
            property_link.append(tag.get('href'))

    return property_link


def fill_google_form(rent: list, address: list, property_url: list) -> None:

    total_results = min(len(rent), len(address), len(property_url))

    for item in range(0, total_results):

        # Enter Property address
        fill_property_address = wait.until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')))
        fill_property_address.send_keys(address[item])

        # Enter rent of the property
        price_per_month = wait.until(EC.element_to_be_clickable(
            (By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')))
        price_per_month.send_keys(rent[item])

        # Enter property url
        property_link = wait.until(EC.element_to_be_clickable(
            (By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')))
        property_link.send_keys(property_url[item])

        # Sumbit the data
        send_button = wait.until(EC.element_to_be_clickable(
            (By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span/span')))
        send_button.click()

        another_data = wait.until(EC.element_to_be_clickable(
            (By.XPATH, '/html/body/div[1]/div[2]/div[1]/div/div[4]/a')))
        another_data.click()

        time.sleep(0.5)

    print("All findings filled")


if __name__ == '__main__':
    google_form = "https://docs.google.com/forms/d/e/1FAIpQLSc4VV0f-zStIKSKYEi1QQy6_bEuNADciChiHYYJ8vst7_IXLg/viewform?usp=header"
    house_rent_website = "https://appbrewery.github.io/Zillow-Clone/"

    responce = requests.get(house_rent_website)
    responce.raise_for_status()
    website_data = responce.text
    soup = BeautifulSoup(website_data, "html.parser")
    rent = rent_finder()
    address = address_finder()
    property_url = address_link_finder()

    chrome_option = webdriver.ChromeOptions()
    chrome_option.add_experimental_option("detach", True)

    driver = webdriver.Chrome(options=chrome_option)
    driver.get(google_form)
    wait = WebDriverWait(driver, 2)

    fill_google_form(rent, address, property_url)

    driver.close()
    driver.quit()
