import pandas as pd
import numpy as np

# Sources: Lesson 3 - Intro to Data Science
# Sources: (pandasql guide) https://pypi.python.org/pypi/pandasql
# Sources: http://docs.scipy.org/doc/numpy/reference/generated/numpy.mean.html
# http://openclassroom.stanford.edu/MainFolder/DocumentPage.php?course=MachineLearning&doc=exercises/ex3/ex3.html


def normalize_features(array):
   """
   Normalize the features in our data set.
   """
   array_normalized = (array-array.mean())/array.std() # calculating z-score
   mu = array.mean() # assigning mean
   sigma = array.std() # assigning std. deviation

   return array_normalized, mu, sigma # returning z-score, mean and std. deviation

def compute_cost(features, values, theta):
    
    # compute_cost method used from lesson 3 exercises...will be used as for gradient descent calculations

    m = len(values)
    sum_of_square_errors = np.square(np.dot(features, theta) - values).sum()
    cost = sum_of_square_errors / (2*m)

    return cost

def gradient_descent(features, values, theta, alpha, num_iterations):
    
    m = len(values) # gradietn_descent method used from lesson 3 exercises...returns theta and const_history dataframe
    cost_history = []

    
    for i in range(num_iterations): # reduced size of num_iterations to avoid "server has encountered an error" message (see below in predicitons())
        
        cost_history.append(compute_cost(features, values, theta))
        
        theta = theta - alpha/m * np.dot(((np.dot(features, theta)) - values),features)
        
    return theta, pandas.Series(cost_history)

def predictions(dataframe):
    

    # Select Features (try different features!)
    features = dataframe[['rain', 'precipi', 'Hour', 'meantempi','meandewpti','meanwindspdi']]
    
    # Add UNIT to features using dummy variables
    dummy_units = pandas.get_dummies(dataframe['UNIT'], prefix='unit')
    features = features.join(dummy_units)
    
    # Values
    values = dataframe[['ENTRIESn_hourly']]
    m = len(values)

    features, mu, sigma = normalize_features(features)
    features['ones'] = np.ones(m) # Add a column of 1s (y intercept)
    
    # Convert features and values to numpy arrays
    features_array = np.array(features)
    values_array = np.array(values).flatten()

    # Set values for alpha, number of iterations.
    alpha = 0.5 # Value of alpha changed for increase in R^2 value
    num_iterations = 40 # iterations reduced

    # Initialize theta, perform gradient descent
    theta_gradient_descent = np.zeros(len(features.columns))
    theta_gradient_descent, cost_history = gradient_descent(features_array, 
                                                            values_array, 
                                                            theta_gradient_descent, 
                                                            alpha, 
                                                            num_iterations)
    
    plot = None
    # -------------------------------------------------
    # Uncomment the next line to see your cost history
    # -------------------------------------------------
    plot = plot_cost_history(alpha, cost_history)
    # 
    # Please note, there is a possibility that plotting
    # this in addition to your calculation will exceed 
    # the 30 second limit on the compute servers.
    
    predictions = np.dot(features_array, theta_gradient_descent)
    return predictions, plot


def plot_cost_history(alpha, cost_history):
   
   cost_df = pandas.DataFrame({
      'Cost_History': cost_history,
      'Iteration': range(len(cost_history))
   })
   return ggplot(cost_df, aes('Iteration', 'Cost_History')) + \
      geom_point() + geom_line() + ggtitle('Cost History for alpha = %.3f' % alpha )


def compute_r_squared(data, predictions):
    SST = ((data-np.mean(data))**2).sum()
    SSReg = ((predictions-np.mean(data))**2).sum()
    r_squared = SSReg / SST

    return r_squared


if __name__ == "__main__":
    input_filename = "turnstile_data_master_with_weather.csv"
    turnstile_master = pd.read_csv(input_filename)
    predicted_values = predictions(turnstile_master)
    r_squared = compute_r_squared(turnstile_master['ENTRIESn_hourly'], predicted_values) 

    print r_squared