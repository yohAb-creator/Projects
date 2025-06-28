import requests
from smtplib import SMTP
from email.message import EmailMessage
import os
from dotenv import load_dotenv
print(load_dotenv())
STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
STOCK_API_KEY = os.getenv("STOCK_API_KEY")
NEWS_API_KEY = os.getenv("NEWS_API_KEY")

PASSWORD = os.getenv('PASSWORD')
EMAIL = os.getenv('EMAIl')
BIRTH_PASS = os.getenv('BIRTH_PASS')
REC_MAIL = os.getenv('REC_MAIL')



stock_params = {
    'function': 'TIME_SERIES_DAILY',
    'symbol': STOCK_NAME,
    'apikey': STOCK_API_KEY
}
response = requests.get(STOCK_ENDPOINT, params=stock_params)
data = response.json()["Time Series (Daily)"]
data_list = [value for (key,value) in data.items()]
yesterday_close = float(data_list[0]['4. close'])

before_yesterday_close = float(data_list[1]['4. close'])
difference = yesterday_close - before_yesterday_close
updown = None
if difference > 0:
    updown = "🔺"
elif difference < 0:
    updown = "🔻"
perc = abs(difference)/ yesterday_close * 100
print(perc)

news_params = {
    "apiKey": NEWS_API_KEY,
    "qInTitle": COMPANY_NAME
}
news_response = requests.get(NEWS_ENDPOINT, params=news_params)
articles = news_response.json()["articles"]

if perc > 0:
    print(articles)

three_articles = articles[:3]
nl = "\n"
formatted_articles = [f"Headline: {article['title']}.{nl}Brief: {article['description']}" for article in three_articles]


if perc > 0:
    for article in formatted_articles:
        msg = EmailMessage()
        msg['From'] = EMAIL
        msg['To'] = REC_MAIL
        msg['Subject'] = f"TSLA: {updown}{round(perc, 2)}%"
        msg.set_content(article)  # UTF-8 safe

        with SMTP("smtp.gmail.com", 587) as connection:
            connection.starttls()
            connection.login(user=EMAIL, password=BIRTH_PASS)
            connection.send_message(msg)





