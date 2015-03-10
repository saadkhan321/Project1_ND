import numpy as np
import pandas
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
    
    '''
    Before we perform any analysis, it might be useful to take a
    look at the data we're hoping to analyze. More specifically, let's 
    examine the hourly entries in our NYC subway data and determine what
    distribution the data follows. This data is stored in a dataframe
    called turnstile_weather under the ['ENTRIESn_hourly'] column.
    
    Let's plot two histograms on the same axes to show hourly
    entries when raining vs. when not raining. Here's an example on how
    to plot histograms with pandas and matplotlib:
    turnstile_weather['column_to_graph'].hist()
    
    Your histograph may look similar to bar graph in the instructor notes below.
    
    You can read a bit about using matplotlib and pandas to plot histograms here:
    http://pandas.pydata.org/pandas-docs/stable/visualization.html#histograms
    
    You can see the information contained within the turnstile weather data here:
    https://www.dropbox.com/s/meyki2wl9xfa7yk/turnstile_data_master_with_weather.csv
    '''

    plt.figure();
    
    # creating subframes for rainy and non rainy entries and plotting histogram
    turnstile_weather['ENTRIESn_hourly'][turnstile_weather['rain'] == 0].hist(bins=180, label='No Rain') # historgram for hourly entries when it is not raining
    turnstile_weather['ENTRIESn_hourly'][turnstile_weather['rain'] == 1].hist(bins=180, alpha=0.8, label='Rain') # historgram for hourly entries when it is raining
    
    ## plot title and labels, etc
    plt.title("Histogram of ENTRIESn_hourly")
    plt.xlabel("ENTRIESn_hourly")
    plt.ylabel("Frequency")
    plt.xlim([0,6000])
    plt.legend(shadow=True)
    
    # aligning the plot to add text below
    axis = plt.subplot(111)
    pos1 = axis.get_position() # get the original position 
    pos2 = [pos1.x0, pos1.y0 + 0.1,  pos1.width, pos1.height / 1.1] 
    axis.set_position(pos2)    
    
    # text under the figure
    plt.figtext(.08, .06, "In the above figure, the two histograms compare hourly entries (ENTRIESn_hourly)\ninto NYC subways for rainy days and non-rainy days.")
   
    
    return plt
