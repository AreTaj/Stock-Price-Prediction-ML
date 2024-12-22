import yfinance as yf
import pandas as pd

def load_data():
    """
    Downloads and prepares AAPL stock data.

    Returns:
        pandas DataFrame with AAPL stock data.
    """
    aapl_data = yf.download("AAPL")     # Download data

    # Check if data is a pandas dataframe
    if isinstance(aapl_data, pd.DataFrame):
        print("aapl_data is a pandas DataFrame.")
    else:
        print("aapl_data is not a pandas DataFrame.")
    
    aapl_data.columns = aapl_data.columns.droplevel(1)  # Drop the 'Ticker' level
    aapl_data = aapl_data.reset_index()  # Convert the Date index to a column
    return aapl_data

aapl_data = load_data()
print(f"Columns: {aapl_data.columns}\n")
print(f"Data head: \n{aapl_data.head()}")


""" 
Initial data columns: MultiIndex([( 'Close', 'AAPL'),
            (  'High', 'AAPL'),
            (   'Low', 'AAPL'),
            (  'Open', 'AAPL'),
            ('Volume', 'AAPL')],
           names=['Price', 'Ticker'])
"""