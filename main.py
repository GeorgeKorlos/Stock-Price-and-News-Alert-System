import datetime
import requests
from twilio.rest import Client
import os

STOCK_NAME = 'TSM'
COMPANY_NAME = 'Taiwan Semiconductor Manufacturing Company Limited'

NEWS_ENDPOINT = 'https://newsapi.org/v2/everything'
NEWS_API = os.getenv('NEWS_API')
STOCK_ENDPOINT = 'https://www.alphavantage.co/query'
STOCK_API = os.getenv('STOCK_API')

stock_params = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK_NAME,
    'apikey': STOCK_API
}

news_params = {
    'apiKey': NEWS_API,
    'qIntitle': COMPANY_NAME,
}

account_sid = os.getenv('ACCOUNT_SID')
auth_token = os.getenv('AUTH_TOKEN')

response = requests.get(url=STOCK_ENDPOINT, params=stock_params)
response.raise_for_status()
stock_data = response.json()

yesterday = (datetime.datetime.now() - datetime.timedelta(days=1)).strftime("%Y-%m-%d")
yesterday_close = float(stock_data['Time Series (Daily)'][yesterday]['4. close'])

day_before_yesterday = (datetime.datetime.now() - datetime.timedelta(days=2)).strftime("%Y-%m-%d")
day_before_yesterday_close = float(stock_data['Time Series (Daily)'][day_before_yesterday]['4. close'])

difference = abs(yesterday_close - day_before_yesterday_close)
up_down = None
if difference > 0:
    up_down = "🔼"
else:
    up_down = "🔽"

percentage_difference = abs(((yesterday_close - day_before_yesterday_close) / day_before_yesterday_close) * 100)
rounded_percentage_difference = round(percentage_difference, 2)

if rounded_percentage_difference > 0:

    response = requests.get(url=NEWS_ENDPOINT, params=news_params)
    response.raise_for_status()
    news_data = response.json()
    articles = news_data['articles'][:3]
    formatted_article = [f"{STOCK_NAME}: {up_down}{rounded_percentage_difference}%\nHeadline: {article['title']}. \nBrief: {article['description']}" for article in articles]

    client = Client(account_sid, auth_token)
    for article in formatted_article:
        message = client.messages.create(
            body=article,
            from_=os.getenv('TWILLIO_FROM'),
            to=os.getenv('TWILLIO_TO')
        )
