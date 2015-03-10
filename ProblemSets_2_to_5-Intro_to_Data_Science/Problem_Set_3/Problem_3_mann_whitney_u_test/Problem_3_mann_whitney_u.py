import numpy as np
import scipy
import scipy.stats
import pd


def mann_whitney_plus_means(turnstile_weather):
    

    # Sources: Lesson 3 - Intro to Data Science
    # Sources: (pandasql guide) https://pypi.python.org/pypi/pandasql
    # Sources: http://docs.scipy.org/doc/numpy/reference/generated/numpy.mean.html
    # Sources: http://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.mannwhitneyu.html


    with_rain = turnstile_weather['ENTRIESn_hourly'][turnstile_weather['rain'] == 1] # filtering entries with rain
    without_rain = turnstile_weather['ENTRIESn_hourly'][turnstile_weather['rain'] == 0] # filtering entries without rain
    
    with_rain_mean = np.mean(with_rain) # mean of entries with rain
    without_rain_mean = np.mean(without_rain) # mean of entries with rain
    
    mann = scipy.stats.mannwhitneyu(with_rain, without_rain) # computing Mann-Whitney rank test
    U = mann[0] # assigning the Mann-Whitney statistic
    p = mann[1] # assigning One-sided p-value

    return with_rain_mean, without_rain_mean, U, p

if __name__ == "__main__":
    input_filename = "turnstile_data_master_with_weather.csv"
    turnstile_master = pd.read_csv(input_filename)
    student_output = mann_whitney_plus_means(turnstile_master)

    print student_output