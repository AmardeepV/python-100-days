from bs4 import BeautifulSoup
import requests
import smtplib
from email.message import EmailMessage
import os


URL = "https://www.amazon.de/-/en/gp/product/B07FVZFFXD"
GMAIL_SENDER_ID = "amardeepverma03@gmail.com"
GMAIL_RECEIVER_ID = "pythontest0802@gmail.com"
GMAIL_PASS = os.environ.get("GMAIL_PYTHON_PASSWORD")

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)",
    "Accept-Language": "en-US,en;q=0.9"
}

response = requests.get(URL, headers=headers)
soup = BeautifulSoup(response.text, "html.parser")
price_in_eur = soup.find("span", class_="a-offscreen").get_text()

current_price = float(price_in_eur.strip('€').replace(',', ''))
desired_price = 1350

if current_price <= desired_price:
    print("Sending email..")
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=GMAIL_SENDER_ID, password=GMAIL_PASS)
        msg = EmailMessage()
        msg['Subject'] = "Drone Amazon price alert"
        msg['To'] = GMAIL_RECEIVER_ID
        msg['From'] = GMAIL_SENDER_ID

        msg.set_content(
            "The price of the DJi Air 3s on Amazon is lowest, go buy it"
        )
        connection.send_message(msg)

else:
    print("price hasn't reached to the desired amount")
