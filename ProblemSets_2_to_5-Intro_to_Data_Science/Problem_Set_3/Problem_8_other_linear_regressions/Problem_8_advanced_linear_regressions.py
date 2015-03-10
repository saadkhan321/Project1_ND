import numpy as np
import pandas as pd
import scipy
import statsmodels

# Lesson 3 - Intro to Data Science
# http://statsmodels.sourceforge.net/devel/
# http://statsmodels.sourceforge.net/devel/example_formulas.html

def predictions(weather_turnstile):
    
    # prediction results to show what influence 'UNIT' has on R^2
    result = sm.ols(formula="ENTRIESn_hourly ~ rain + UNIT + fog + thunder + precipi", data=weather_turnstile).fit()
    
    
    prediction = result.predict()

    return prediction

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
