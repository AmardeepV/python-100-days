from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("http://secure-retreat-92358.herokuapp.com")

# active_editors = driver.find_element(
#     By.XPATH, value='//*[@id="articlecount"]/ul/li[1]/a')
# print(active_editors.text)

# Find elements by link text
# all_portals = driver.find_element(By.LINK_TEXT, value='Content portals')
# all_portals.click()
# find the search input by name
# search = driver.find_element(By.NAME, value='search')
# Sending keyboard input to selinium

# search.send_keys("Python")
# search.send_keys(Keys.ENTER)
# driver.close()
# driver.quit()


first_name = driver.find_element(By.NAME, value='fName')
last_name = driver.find_element(By.NAME, value='lName')
email = driver.find_element(By.NAME, value='email')

first_name.send_keys("Python")
last_name.send_keys("Test")
email.send_keys("pythontest@gmail.com")

sign_up = driver.find_element(By.XPATH, value='/html/body/form/button')
sign_up.click()
