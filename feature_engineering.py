import pandas as pd
from data_preparation import prepared_data

def add_features(data, window_size):
  """
  Adds features to the stock data.

  Args:
    data: pandas DataFrame containing stock data.
    window_size: Integer representing the window size for moving averages.

  Returns:
    pandas DataFrame with added features.
  """

  # Calculate daily returns
  data['Daily Return'] = data['Close'].pct_change()

  # Calculate Simple Moving Average (SMA)
  data['SMA_' + str(window_size)] = data['Close'].rolling(window=window_size).mean()

  return data

# prepared_data is loaded from data_preparation.py

window_size = 20  # Value is adjustable
featured_data = add_features(prepared_data.copy(), window_size)
print(f"SMA column head: \n{featured_data['SMA_'+ str(window_size)].head(21)}\n")
print(f"SMA column length: {len(featured_data['SMA_'+ str(window_size)])}\n")
