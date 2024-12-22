import pandas as pd
from data_loading import aapl_data

def prepare_data(data):
  """
  Prepares the stock data for analysis.

  Args:
    data: pandas DataFrame containing stock data.

  Returns:
    pandas DataFrame with prepared data.
  """
# Check for missing values before filling
  missing_values = data.isnull().sum()
  print(f"Number of missing values before filling: {missing_values.sum()}")

  # Handle missing values (if any)
  data = data.ffill()

  # Check type of date column
  print(f"Date column type:{data['Date']}")# = pd.to_datetime(data['Date'])

  # Check for missing values after filling
  missing_values = data.isnull().sum()
  print(f"Number of missing values after filling: {missing_values.sum()}")

  return data

# aapl_data is loaded from data_loading.py
prepared_data = prepare_data(aapl_data)