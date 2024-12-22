import yfinance as yf

# Download AAPL stock data from Yahoo Finance
aapl_data = yf.download("AAPL")

# Print the first 5 rows of the data to get a glimpse
print(aapl_data.head())