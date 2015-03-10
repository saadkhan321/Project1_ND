import pandas as pd
import numpy as np

from prediction import predictions


def compute_r_squared(data, predictions):
    
    # Sources: http://docs.scipy.org/doc/numpy/reference/generated/numpy.mean.html
    # Sources: http://docs.scipy.org/doc/numpy/reference/generated/numpy.sum.html 

     mean_data = data.mean() # taking mean of data
    
    r_squared = 1 - (np.square(data - predictions).sum())/(np.square(data - mean_data).sum()) # applying formula for R^2

    return r_squared


if __name__ == "__main__":
    input_filename = "turnstile_data_master_with_weather.csv"
    turnstile_master = pd.read_csv(input_filename)
    predicted_values = predictions(turnstile_master)
    r_squared = compute_r_squared(turnstile_master['ENTRIESn_hourly'], predicted_values)
    print r_squared