import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


def plot_residuals(dataframe, predictions):
    
    

    plt.figure()
    
    h = (turnstile_weather['ENTRIESn_hourly'] - predictions)
    h.hist(normed=True, bins=100, label='Residuals')
    plt.title("Histogram of Residuals")
    plt.xlabel("Residuals")
    plt.ylabel("Relative Frequency")
    plt.xlim([-6000,6000])
    plt.ylim([0,0.0005])
    plt.legend(shadow=True)

    return plt

def normalize_features(array):
   """
   Normalize the features in our data set.
   """
   array_normalized = (array-array.mean())/array.std()
   mu = array.mean()
   sigma = array.std()

   return array_normalized, mu, sigma

def compute_cost(features, values, theta):
    """
    Compute the cost function given a set of features / values, and the values for our thetas.
    """
    m = len(values)
    sum_of_square_errors = np.square(np.dot(features, theta) - values).sum()
    cost = sum_of_square_errors / (2*m)

    return cost

def gradient_descent(features, values, theta, alpha, num_iterations):
    """
    Perform gradient descent given a data set with an arbitrary number of features.
    """

    m = len(values)
    cost_history = []

    for i in range(num_iterations):
        predicted_values = np.dot(features, theta)
        theta = theta - alpha / m * np.dot((predicted_values - values), features)

        cost = compute_cost(features, values, theta)
        cost_history.append(cost)

    return theta, pandas.Series(cost_history)

def predictions(dataframe):

    dummy_units = pandas.get_dummies(dataframe['UNIT'], prefix='unit')
    features = dataframe[['rain', 'precipi', 'Hour', 'meantempi']].join(dummy_units)
    values = dataframe[['ENTRIESn_hourly']]
    m = len(values)

    features, mu, sigma = normalize_features(features)

    features['ones'] = np.ones(m)
    features_array = np.array(features)
    values_array = np.array(values).flatten()

    #Set values for alpha, number of iterations.
    alpha = 0.1
    num_iterations = 75

    #Initialize theta, perform gradient descent
    theta_gradient_descent = np.zeros(len(features.columns))
    theta_gradient_descent, cost_history = gradient_descent(features_array, values_array, theta_gradient_descent,
                                                            alpha, num_iterations)
    predictions = np.dot(features_array, theta_gradient_descent)

    return predictions

if __name__ == "__main__":
    input_filename = "turnstile_data_master_with_weather.csv"
    turnstile_master = pd.read_csv(input_filename)
    prediction_values = predictions(turnstile_master)

    image = "plot.png"
    plt = plot_residuals(turnstile_master, prediction_values)
    plt.savefig(image)
