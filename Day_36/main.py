import requests
import smtplib
from email.message import EmailMessage
import os

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

sender_email = "amardeepverma03@gmail.com"
receiver_email = "pythontest0802@gmail.com"

# ------------ ENV API ---------------------
stock_api = os.environ.get("STOCK_API")
news_api = os.environ.get("NEWS_API")
gmail_password = os.environ.get("GMAIL_PYTHON_PASSWORD")

# -------------- URL SETUP -----------------
# STOCK API URL
stock_url = "https://www.alphavantage.co/query"
stock_parameters = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK,
    "apikey": stock_api
}

# STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
stock_responce = requests.get(url=stock_url, params=stock_parameters)
stock_responce.raise_for_status()
stock_data = stock_responce.json()
last_two_days_close_price = []
dates = []
last_two_days_data = list(stock_data['Time Series (Daily)'].items())[:2]

for val in last_two_days_data:
    last_two_days_close_price.append(float(val[1]['4. close']))
    dates.append(val[0])

change_percent = (
    last_two_days_close_price[0] - last_two_days_close_price[1]) / last_two_days_close_price[0] * 100

if abs(change_percent) >= 5:
    # STEP 2: Use https://newsapi.org
    # Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME.
    # News API URL
    news_url = "https://newsapi.org/v2/everything"
    news_parameters = {
        "q": COMPANY_NAME,
        "apiKey": news_api,
        "language": "en",
        "from": f"{dates[1]}",
        "to": f"{dates[0]}",
        "searchIn": "title,description"
    }
    news_responce = requests.get(url=news_url, params=news_parameters)
    news_responce.raise_for_status()
    news_data = news_responce.json()

    news = [{
        'title': article['title'],
        'description': article['description']
    }
        for article in news_data['articles'][:3]
    ]
    # STEP 3: Use https://www.twilio.com
    # Send a seperate message with the percentage change and each article's title and description to your phone number.

    if change_percent < 0:
        trend_sign = "DOWN"
    else:
        trend_sign = "UP"

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=sender_email, password=gmail_password)

        for each_news in news:
            msg = EmailMessage()
            msg["Subject"] = f"TSLA {trend_sign}{int(abs(change_percent))} % ,{each_news['title']}"
            msg["From"] = sender_email
            msg["To"] = receiver_email

            msg.set_content(
                f"{each_news['description']}"
            )

            connection.send_message(msg)
    print("Email sent..")
else:
    print("change is less than 5%")
