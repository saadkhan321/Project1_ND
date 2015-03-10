from pandas import *
from ggplot import *

def plot_weather_data(turnstile_weather):

    # Sources: http://blog.yhathq.com/posts/ggplot-0.4-released.html
    # Sources: https://piazza.com/class/i23uptiifb6194?cid=233
    # Sources: http://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.groupby.html
    # Sources: https://docs.python.org/2/library/datetime.html
    # Sources: https://github.com/yhat/ggplot/blob/master/ggplot/stats/stat_bin.py

    
    # a sub frame of turnstile_weather
    sub_frame = turnstile_weather[['DATEn', 'ENTRIESn_hourly']]
    
    # sum of entries per dates
    sub_date_entries = sub_frame.groupby('DATEn', as_index=False).sum()
    
    # adding a day of the week column to the data frame
    sub_date_entries['Day'] = sub_date_entries['DATEn'].apply(lambda x: datetime.strptime(x, '%Y-%m-%d').strftime('%w-%A'))
    
    
    #print sub_date_entries            
    
    # smaller data frame wihtout DATEn
    sub_day_entries = sub_date_entries[['Day', 'ENTRIESn_hourly']]
    
    #print sub_day_entries
    
    # sum of entries per day of the week
    sub_day_entries_sum = sub_day_entries.groupby('Day', as_index=False).sum()
    
    #print sub_day_entries_sum
    
      
    plot = ggplot(aes(x='Day'), data = sub_day_entries_sum) + \
    geom_bar(aes(weight='ENTRIESn_hourly'), color = 'blue', fill = 'lightblue',alpha = 0.5) + \
    ggtitle("NYC Subway Ridership / Day of the Week") + \
    xlab('Days of the Week') + ylab('Riders entering the subways')
    
    return plot


if __name__ == "__main__":
    image = "plot.png"
    turnstile_weather = pd.read_csv("turnstile_data_master_with_weather.csv")
    gg =  plot_weather_data(turnstile_weather)
    ggsave(gg, image)