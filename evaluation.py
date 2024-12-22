from sklearn.metrics import mean_squared_error
from sklearn.metrics import mean_absolute_error
from sklearn.metrics import r2_score
from sklearn.metrics import explained_variance_score
import numpy as np

def median_absolute_error(y_true, y_pred):
    errors = np.abs(y_true - y_pred)
    return np.median(errors)

def evaluate_model(model, X_test, y_test):
    """Evaluates a model and returns metrics in a dictionary."""
    y_pred = model.predict(X_test)
    metrics = {
        "mse": mean_squared_error(y_test, y_pred),
        "mae": mean_absolute_error(y_test, y_pred),
        "r2": r2_score(y_test, y_pred),
        "explained_variance": explained_variance_score(y_test, y_pred),
        "med_ae": median_absolute_error(y_test, y_pred),
    }
    return metrics

def print_model_evaluation(model_name, metrics):
    """Prints the evaluation results from a metrics dictionary."""
    print(f"{model_name} Evaluation:")
    for metric_name, metric_value in metrics.items():
        print(f"{metric_name.upper()}: {metric_value}")

# def evaluate_model(model, X_test, y_test):
#   """
#   Evaluates a model using Mean Squared Error (MSE).

#   Args:
#     model: Trained model object.
#     X_test: Testing features.
#     y_test: Actual target values for testing data.

#   Returns:
#     MSE score of the model.
#   """
#   y_pred = model.predict(X_test)
#   mse = mean_squared_error(y_test, y_pred)
#   mae = mean_absolute_error(y_test, y_pred)
#   r2 = r2_score(y_test, y_pred)
#   explained_variance = explained_variance_score(y_test, y_pred)
#   med_ae = median_absolute_error(y_test,y_pred)
#   return mse, mae, r2, explained_variance, med_ae

# def print_model_evaluation(model_name, mse, mae, r2, explained_variance, med_ae):
#   """
#   Prints the evaluation results for a model.

#   Args:
#     model_name: Name of the model being evaluated.
#     mse: MSE score of the model.
#     mae: MAE score of the model.
#     r2: R-squared score of the model.
#     explained_variance: Explained variance score of the model.
#     med_ae: Median absolute error (optional).
#   """
#   print(f"{model_name} Evaluation:")
#   print(f"Mean Squared Error: {mse}")
#   print(f"Mean Absolute Error: {mae}")
#   print(f"R-squared: {r2}")
#   print(f"Explained Variance: {explained_variance}")
#   print(f"Median Absolute Error: {med_ae}")
