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
