from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException
import os
import time


def login():
    # Find login button on the homepage
    # login = driver.find_element(By.XPATH, value='//*[@id="login-button"]')
    login = wait.until(
        EC.element_to_be_clickable((By.ID, "login-button")))
    login.click()

    # Find email section on the login page
    # email = driver.find_element(By.ID, value='email-input')
    email = wait.until(EC.presence_of_element_located((By.ID, 'email-input')))
    email.clear()
    email.send_keys(ACCOUNT_EMAIL)

    # Find password section on the login page
    # password = driver.find_element(By.ID, value='password-input')
    password = wait.until(
        EC.presence_of_element_located((By.ID, 'password-input')))
    password.clear()
    password.send_keys(ACCOUNT_PASSWORD)

    # Click on the login button
    login_button = driver.find_element(By.ID, value='submit-button')
    login_button.click()

    wait.until(EC.presence_of_element_located((By.ID, "schedule-page")))


def book_class():
    class_cards = driver.find_elements(
        By.CSS_SELECTOR, "div[id^='class-card-']")

    for card in class_cards:
        day_group = card.find_element(
            By.XPATH, "./ancestor::div[contains(@id, 'day-group')]")
        day_title = day_group.find_element(By.TAG_NAME, "h2").text

        if "Tue" in day_title or "Thu" in day_title:
            time_text = card.find_element(
                By.CSS_SELECTOR, "p[id^='class-time-']").text

            if "6:00 PM" in time_text:
                # Get the class name
                class_name = card.find_element(
                    By.CSS_SELECTOR, "h3[id^='class-name-']").text

                # book the class
                book_button = card.find_element(
                    By.CSS_SELECTOR, "button[id^='book-button-']")

                if book_button.text == 'Booked':
                    print(f"Already booked: {class_name} on {day_title}")
                elif book_button.text == "Waitlisted":
                    print(f"Already on waitlist {class_name} on {day_title}")
                elif book_button.text == "Book Class":
                    book_button.click()
                    print(f"successfuly booked {class_name} on {day_title}")
                elif book_button.text == 'Join Waitlist':
                    book_button.click()
                    print(f"Joined waitlist for {class_name} on {day_title}")
                break


def get_my_bookings():
    # Go to the my booking page and get the list of all the classes with their status and print the summary
    # my_booking_page = driver.find_element(
    #     By.XPATH, value='//*[@id="my-bookings-link"]')
    my_booking_page = wait.until(
        EC.element_to_be_clickable((By.ID, "my-bookings-link")))
    my_booking_page.click()

    # booking_classes_details = driver.find_element(
    #     By.XPATH, value='//*[@id="my-bookings-page"]')

    booking_classes_details = wait.until(
        EC.presence_of_element_located((By.ID, "my-bookings-page")))

    # get the list of the confirmed booking classes
    try:
        confirmed_booking = booking_classes_details.find_element(
            By.XPATH, value='//*[@id="confirmed-bookings-section"]')

        confirmed_booking_list = confirmed_booking.find_elements(
            By.CSS_SELECTOR, "div[id^='booking-card-booking_']")

        total_booked_classes["total"] = len(confirmed_booking_list)

        for each in confirmed_booking_list:
            confirmed_classes = each.find_element(By.TAG_NAME, "h3").text
            confirmed_classes_time = each.find_element(
                By.XPATH, './/p[strong[text()="When:"]]')

            confirmed_classes_time_only = confirmed_classes_time.text.replace(
                "When:", "").strip().strip('"')

            message = f"{confirmed_classes} on {confirmed_classes_time_only}"
            total_booked_classes["classes_details"].append(message)

    except NoSuchElementException:
        print("There is no confirmed booking yet")

    # get the list of the waitlisted classes
    try:
        waiting_booking = booking_classes_details.find_element(
            By.XPATH, value='//*[@id="waitlist-section"]')

        waiting_booking_list = waiting_booking.find_elements(
            By.CSS_SELECTOR, "div[id^='waitlist-card-waitlist_']")

        total_waitlist_classes["total"] = len(waiting_booking_list)

        for each in waiting_booking_list:
            waitlist_classes = each.find_element(By.TAG_NAME, "h3").text
            waitlist_classes_only = waitlist_classes.split('(')
            waitlist_classes_time = each.find_element(
                By.XPATH, './/p[strong[text()="When:"]]')
            waitlist_classes_time_only = waitlist_classes_time.text.replace(
                "When:", "").strip().strip('"')

            message = f"{waitlist_classes_only[0]} on {waitlist_classes_time_only}"
            total_waitlist_classes["classes_details"].append(message)

    except NoSuchElementException:
        print("There is no waiting list booking")


def retry(func, retries=7, description=None):
    for i in range(retries):
        print(f"Trying {description}. Attempt {i+1}")
        try:
            return func()
        except TimeoutException:
            if i == retries - 1:
                raise
            time.sleep(1)


if __name__ == '__main__':
    # Add your credentials at the top of your script
    ACCOUNT_EMAIL = "pythontest@test.com"  # The email you registered with
    ACCOUNT_PASSWORD = "python1234"      # The password you used during registration
    GYM_URL = "https://appbrewery.github.io/gym/"

    total_booked_classes = {
        "total": 0,
        "classes_details": []
    }

    total_waitlist_classes = {
        "total": 0,
        "classes_details": []
    }

    chrome_option = webdriver.ChromeOptions()
    chrome_option.add_experimental_option("detach", True)

    # directory in your project folder to store your Chrome Profile information
    user_data_dir = os.path.join(os.getcwd(), "chrome_profile")
    # tell your Chrome Driver to use the directory you specified to store a "profile"
    chrome_option.add_argument(f"--user-data-dir={user_data_dir}")

    driver = webdriver.Chrome(options=chrome_option)
    driver.get(GYM_URL)
    wait = WebDriverWait(driver, 10)

    retry(login, description="login")
    book_class()
    retry(get_my_bookings, description="Get my bookings")
    # Summary of the bookings
    print(f" Booked : {total_booked_classes}")
    print(f" Waitlist bookings {total_waitlist_classes}")

    driver.close()
    driver.quit()
