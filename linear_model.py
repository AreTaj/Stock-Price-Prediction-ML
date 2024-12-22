from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
import pandas as pd
from feature_engineering import featured_data, window_size

def train_model(data,window_size):
  """
  Trains a linear regression model on the given data.

  Args:
    data: pandas DataFrame containing stock data with features.

  Returns:
    Trained linear regression model.
  """

  # Prepare data for training
  X = data
  X = data.drop('Date', axis=1)  # Drop the 'date' column from X

  y = data['Close'].shift(-1)  # Target: Close price on the next day

  # Remove rows with NaN values in X
  combined = pd.concat([X, y], axis=1)  # Combine X and y along columns
  data_clean = combined.dropna()  # Drop rows with NaN in either X or y
  
  # Split data into training and testing sets
  X_clean = data_clean#[sma_column_name]
  y_clean = data_clean['Close']
  X_train, X_test, y_train, y_test = train_test_split(X_clean, y_clean, test_size=0.2, random_state=42)

  # Reshape X_train and X_test if necessary
  if not isinstance(X_train, pd.DataFrame):
      X_train = X_train.values.reshape(-1, 1)  # Reshape to 2D with 1 column
  if not isinstance(X_test, pd.DataFrame):
      X_test = X_test.values.reshape(-1, 1)  # Reshape for prediction

  # Create and train the model
  model = LinearRegression()
  model.fit(X_train, y_train)

  # Make predictions
  y_pred = model.predict(X_test)  # Predicts for the next day; not currently used

  return model, X_test, y_test

# featured_data is loaded from feature_engineering.py
window_size=window_size
trained_model, X_test, y_test = train_model(featured_data, window_size)

# Evaluate linear model
from evaluation import evaluate_model, print_model_evaluation
rained_model, X_test, y_test = train_model(featured_data, window_size)
metrics = evaluate_model(trained_model, X_test, y_test)
print_model_evaluation("Linear Regression", metrics)