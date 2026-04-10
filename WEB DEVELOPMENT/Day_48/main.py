from selenium import webdriver
from selenium.webdriver.common.by import By

# keep Chrome browser open after program finishes
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

# If you want you browser to close immediatly then use the below one and remove the options parameters
driver = webdriver.Chrome(options=chrome_options)
# driver.get("https://www.amazon.de/-/en/gp/product/B07FVZFFXD")

# price_euro = driver.find_element(By.CLASS_NAME, value="a-price-whole")
# price_cent = driver.find_element(By.CLASS_NAME, value="a-price-fraction")
# print(f"the price of the item is {price_euro.text}.{price_cent.text}")
driver.get("https://www.python.org")
# events = driver.find_element(By.NAME, value="q")
# print(events.get_attribute('type'))
# events = driver.find_element(By.ID, value="submit")
# print(events.size)

# documentation_link = driver.find_element(
#     By.CSS_SELECTOR, value=".do-not-print a")
# print(documentation_link.text)

# xpath_link = driver.find_element(
#     By.XPATH, value='//*[@id="site-map"]/div[2]/div/ul/li[2]/a')
# print(xpath_link.text)

events = driver.find_element(
    By.XPATH, value='//*[@id="content"]/div/section/div[3]/div[2]/div/ul')
list_of_events = events.text.split('\n')
event_dict = {}
date = []
event_names = []
for count, each in enumerate(list_of_events):
    if count % 2 == 0:
        date.append(each)
    else:
        event_names.append(each)

for count, entry in enumerate(date):
    event_dict[count] = {
        "Date": entry,
        "Event": event_names[count]
    }

print(event_dict)


driver.close()  # close the single tab after opening by the option method
driver.quit()  # close all the tabs opened by the option method
