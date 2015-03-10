import pandas as pd
import pandasql

def avg_min_temperature(filename):
    
    # Sources: Lesson 2 - Intro to Data Science
    # Sources: https://pypi.python.org/pypi/pandasql
    
    weather_data = pd.read_csv(filename) # reading csv into a dataframe named weather_data

    q = """ SELECT avg(cast (meantempi as integer)) FROM weather_data WHERE (cast (strftime('%w', date) as integer) =0) or (cast (strftime('%w', date) as integer) =6) """
    # assigning the query to variable q which would fetch info from dataframe
   
    mean_temp_weekends = pandasql.sqldf(q.lower(), locals()) # SQL command executed against the pandas frame to generate mean temperature on weekends
    return mean_temp_weekends # mean temperature on weekends returned

if __name__ == "__main__":
    input_filename = "C:\Users\Saad_Khan\Anaconda\ND_Data_Analyst_Project1\Intro_to_Data_Science\Problem_Set_2\Problem_3_mean_temp_on_weekends\weather_underground.csv"
    output_filename = "output.csv"
    student_df = avg_min_temperature(input_filename)
    student_df.to_csv(output_filename)