# Stock Price and News Alert System

This repository contains a Python script that tracks the stock price of a specified company and sends an SMS alert with the latest news headlines if the stock price fluctuates significantly. The script fetches stock data using the Alpha Vantage API and news articles using the NewsAPI. SMS alerts are sent using the Twilio API.

## Features

- Fetches daily stock prices from the Alpha Vantage API.
- Calculates the percentage change between consecutive days' closing prices.
- Fetches the top 3 news articles related to the company from NewsAPI if the stock price changes significantly.
- Sends an SMS alert with the stock price change and news headlines using the Twilio API.

## Prerequisites

- Python 3.x
- Required Python packages: `requests`, `twilio`, `python-dotenv`
- Alpha Vantage API key
- NewsAPI key
- Twilio account credentials (Account SID, Auth Token, phone numbers)

## Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/yourusername/stock-news-alert.git
   cd stock-news-alert
2. **Create a virtual environment (optional but recommended):**
   ```bash
   python -m venv venv
   source venv/bin/activate   # On Windows use `venv\Scripts\activate`
3. **Install required packages:**
   ```bash
   pip install -r requirements.txt
4. **Set up environment variables:**
   - Create a `.env` file in the root directory of the project with the following content:
     ```.env
     STOCK_API=your_alphavantage_api_key
     NEWS_API=your_newsapi_key
     ACCOUNT_SID=your_twilio_account_sid
     AUTH_TOKEN=your_twilio_auth_token
     TWILLIO_FROM=your_twilio_phone_number
     TWILLIO_TO=recipient_phone_number
   - Replace the placeholder values with your actual API keys and credentials.
5. **Run the script:**
   ```bash
   python your_script_name.py

## Usage

- The script monitors the stock price of the specified company (STOCK_NAME) and calculates the percentage change between the closing prices of the last two days.
- If the percentage change exceeds a threshold, the script fetches the top 3 related news articles.
- The news and stock information are sent via SMS to the specified phone number.

## Contributing

Feel free to fork the repository and submit pull requests. Please ensure that your code adheres to the existing style and includes appropriate tests.
