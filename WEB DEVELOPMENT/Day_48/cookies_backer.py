from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import StaleElementReferenceException
import time


# ------------------- Create chrome driver for selinimum
def create_driver() -> object:
    chrome_option = webdriver.ChromeOptions()
    chrome_option.add_experimental_option("detach", True)

    driver = webdriver.Chrome(options=chrome_option)
    driver.get("https://ozh.github.io/cookieclicker/")

    return driver

# ------------------ English Language Selector ---------------------------------


def select_english_language(driver: object) -> None:
    wait = WebDriverWait(driver, 10)
    try:
        language = wait.until(EC.element_to_be_clickable(
            (By.XPATH, '//*[@id="langSelect-EN"]')))
        language.click()
        # print("Language selected successfully.")
    except Exception as e:
        print(f"Error selecting language: {e}")

# --------------------Get cookies button---------------------------


def find_cookies(driver: object) -> object:
    cookies_button = driver.find_element(By.ID, value="bigCookie")
    return cookies_button

# --------------------Click on cookies button---------------------------


def click_cookie_safe(driver: object, cookies_button: object) -> None:
    try:
        cookies_button.click()
    except StaleElementReferenceException:
        # If it goes stale, find it again and then click
        new_button = driver.find_element(By.ID, "bigCookie")
        new_button.click()
# ------------------------------------------------------------------------------------


def cookie_game(driver: object, cookies_button: object, user_choice: int) -> str:
    start_time = time.time()
    next_check = start_time
    cookies_to_sell = 0

    # run the while loop for 5 minutes (300 seconds)
    while time.time() < start_time + 300:
        current_time = time.time()
        click_cookie_safe(driver, cookies_button)  # click cokkies button

        # Run this after every 5 seconds and check the right pane to look for availabe items to buy and buy the costly one first
        if current_time >= next_check:
            item_available_to_buy = True
            products = []
            # get the total cookies backed
            cookies = driver.find_element(By.XPATH, value='//*[@id="cookies"]')
            total_cookies = cookies.text
            cookies_to_sell = int(total_cookies.split()[0])
            print(f"totale cokkies backed so far {cookies_to_sell}")

            if user_choice == 2:
                if cookies_to_sell > 10:  # this case for the starting to remove the race while condition
                    while (item_available_to_buy):
                        products_enabled = driver.find_elements(
                            By.CSS_SELECTOR, ".product.unlocked.enabled")   # check which items are available
                        for item in products_enabled:
                            try:
                                price = item.find_element(
                                    By.CLASS_NAME, value="price")
                                products.append((int(price.text), item))
                            except:
                                continue

                        # print(f"Available items: {products}")
                        # Figure out which one is most expensive one and buy that item first
                        if products:
                            products.sort(reverse=True)
                            total_item_incart = len(products)
                            item_unable_to_purchase = 0
                            for each in products:
                                if cookies_to_sell >= each[0]:
                                    each[1].click()
                                    bought_items = each[1].text.split()
                                    cookies_to_sell -= each[0]
                                    print(
                                        f"Bought {bought_items[0]} total {bought_items[0]}: {bought_items[2]}, Cookies available after buying {cookies_to_sell}")
                                else:
                                    item_unable_to_purchase += 1
                            if item_unable_to_purchase == total_item_incart:
                                item_available_to_buy = False

                            products.clear()
            if user_choice == 1:
                products_enabled = driver.find_elements(
                    By.CSS_SELECTOR, ".product.unlocked.enabled")   # check which items are available
                for item in products_enabled:
                    try:
                        price = item.find_element(By.CLASS_NAME, value="price")
                        products.append((int(price.text), item))
                    except:
                        continue

                # print(f"Available items: {products}")
                # Figure out which one is most expensive one and buy that item first
                if products:
                    products.sort(reverse=True)
                    for each in products:
                        if cookies_to_sell >= each[0]:
                            each[1].click()
                            bought_items = each[1].text.split()
                            cookies_to_sell -= each[0]
                            print(
                                f"Bought {bought_items[0]} total {bought_items[0]}: {bought_items[2]}, Cookies available after buying {cookies_to_sell}")
                    products.clear()

            next_check += 5
    cookies_per_second = driver.find_element(
        By.XPATH, value='//*[@id="cookiesPerSecond"]')

    return cookies_per_second.text


def main():
    user_choice = int(input("There are two types of algo\n 1. after 5 second run one loop buy the costly one first then buy the other items.\n 2.after 5 second buy all the items that is possible in a single loop. \n Type 1 or 2."))
    driver = create_driver()
    select_english_language(driver)
    cookies_button = find_cookies(driver)
    # print(f"user input is {user_choice}")
    cookies_per_second = cookie_game(driver, cookies_button, user_choice)
    print(f"cookies {cookies_per_second}")
    driver.close()
    driver.quit()


if __name__ == '__main__':
    main()
