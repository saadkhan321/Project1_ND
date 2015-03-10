from pandas import *
from ggplot import *

def plot_weather_data(turnstile_weather):

    # Sources: http://blog.yhathq.com/posts/ggplot-0.4-released.html
    # Sources: https://piazza.com/class/i23uptiifb6194?cid=233
    # Sources: http://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.groupby.html
    
    
    # a sub frame of turnstile_weather
    sub_frame = turnstile_weather[['Hour', 'ENTRIESn_hourly']]
    
    # sum of entries per hour
    sub_hour_entries = sub_frame.groupby('Hour', as_index=False).mean()
      
      
    plot = ggplot(aes(x='Hour'), data = sub_hour_entries) + \
    geom_bar(aes(weight='ENTRIESn_hourly'), color = 'black', fill = 'orange',alpha = 0.5, binwidth=1) + \
    ggtitle("NYC Subway Ridership during the Day") + \
    xlab('Time of the Day') + ylab('Riders entering the subways') + \
    xlim(0,23)
    
    
    
    return plot


if __name__ == "__main__":
    image = "plot.png"
    turnstile_weather = pd.read_csv("turnstile_data_master_with_weather.csv")
    gg =  plot_weather_data(turnstile_weather)
    ggsave(gg, image)