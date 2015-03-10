import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def entries_line(turnstile_weather):
    
    # Sources: http://matplotlib.org/users/legend_guide.html
    # Sources: http://pandas.pydata.org/pandas-docs/stable/visualization.html
    # Sources: http://stackoverflow.com/questions/24943991/matplotlib-change-grid-interval-and-specify-tick-labels
    # Sources: http://matplotlib.org/users/pyplot_tutorial.html
    
    
    plt.figure();
    
    # creating subframe a
    a = turnstile_weather[['Hour','ENTRIESn_hourly']].groupby(['Hour'], as_index=False)['ENTRIESn_hourly'].mean()
    
    # assignment ot b for ease of plotting line and scatter
    b = a
    
    # plotting the data     
    ax = a.plot(kind='line', x='Hour', y='ENTRIESn_hourly', color='Red', alpha = 0.3, linewidth=2.0);
    b.plot(kind='scatter', x='Hour', y='ENTRIESn_hourly', color='Red', ax=ax);
    
    # plot title and labels, etc
    plt.title("Subway Ridership during the Day")
    plt.xlabel("Hour of the day")
    plt.ylabel("Entries")
    plt.xlim([0,23])
    plt.ylim(0,3000)
    plt.legend(['Entries during the day'], shadow = True)
    
    # aligning the plot to add text below
    axis = plt.subplot(111)
    pos1 = axis.get_position() # get the original position 
    pos2 = [pos1.x0, pos1.y0 + 0.1,  pos1.width, pos1.height / 1.1] 
    axis.set_position(pos2)    
    
    # ticks for x & y grids                                      
    x_ticks = np.arange(0, 23, 1)                                              
    y_ticks = np.arange(0, 3000, 100) 
    min_y_ticks = np.arange(0, 3000, 500) 
    
    axis.set_xticks(x_ticks)                                                       
    axis.set_yticks(y_ticks)                                                       
    axis.set_yticks(min_y_ticks, minor=False)                                           

    # text under the figure
    plt.figtext(.1, .02, "In the above figure, line graph shows the entries (ENTRIESn_hourly) into NYC\nsubways during 24 hours. It is clearly evident that ridership increases during \nthe day time, i.e. from 9 (9:00 am) onwards.")
   
    
    return plt


if __name__ == "__main__":
    image = "plot.png"
    turnstile_weather = pd.read_csv("turnstile_data_master_with_weather.csv")
    plt = entries_line(turnstile_weather)
    plt.savefig(image)