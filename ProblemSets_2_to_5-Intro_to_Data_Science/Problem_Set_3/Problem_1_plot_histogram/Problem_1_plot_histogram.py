import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def entries_histogram(turnstile_weather):
    
    # Sources: Lesson 3 - Intro to Data Science
    # Sources: (pandasql guide) https://pypi.python.org/pypi/pandasql
    # Sources: https://bespokeblog.wordpress.com/2011/07/11/basic-data-plotting-with-matplotlib-part-3-histograms/
    # Sources: http://pandas.pydata.org/pandas-docs/stable/visualization.html#histograms
    # Sources: http://stackoverflow.com/questions/2849286/python-matplotlib-subplot-how-to-set-the-axis-range
    # Sources: http://matplotlib.org/examples/pylab_examples/legend_demo
    # Sources: http://stackoverflow.com/questions/23137991/matplotlib-get-and-set-axes-position
    # Sources: http://stackoverflow.com/questions/11143619/add-graph-description-under-graph-in-pylab
        
    plt.figure();
    turnstile_weather['ENTRIESn_hourly'][turnstile_weather['rain'] == 0].hist(bins=180, label='No Rain') # your code here to plot a historgram for hourly entries when it is not raining
    turnstile_weather['ENTRIESn_hourly'][turnstile_weather['rain'] == 1].hist(bins=180, alpha=0.8, label='Rain') # your code here to plot a historgram for hourly entries when it is raining
    plt.title("Histogram of ENTRIESn_hourly")
    plt.xlabel("ENTRIESn_hourly")
    plt.ylabel("Frequency")
    plt.xlim([0,6000])
    plt.legend(shadow=True)
    
    axis = plt.subplot(111)
    pos1 = axis.get_position() # get the original position 
    pos2 = [pos1.x0, pos1.y0 + 0.1,  pos1.width, pos1.height / 1.1] 
    axis.set_position(pos2)    
    
    plt.figtext(.08, .06, "In the above figure, the two histograms compare hourly entries (ENTRIESn_hourly)\ninto NYC subways for rainy days and non-rainy days.")
   
    
    return plt


if __name__ == "__main__":
    image = "plot.png"
    turnstile_weather = pd.read_csv("turnstile_data_master_with_weather.csv")
    plt = entries_histogram(turnstile_weather)
    plt.savefig(image)