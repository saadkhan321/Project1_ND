import pandas as pd
import pandasql

def max_temp_aggregate_by_fog(filename):

    # Sources: Lesson 2 - Intro to Data Science
    # Sources: https://pypi.python.org/pypi/pandasql
    
    weather_data = pd.read_csv(filename) # reading csv into a dataframe named weather_data

    q = """ SELECT count(*) FROM weather_data WHERE rain = 1 """ # assigning the query to variable q which would fetch info from dataframe 
    
    
    rainy_days = pandasql.sqldf(q.lower(), locals()) # SQL command executed against the pandas frame to generate number of rainy days
    return rainy_days # number of rainy days returned



if __name__ == "__main__":
    input_filename = "C:\Users\Saad_Khan\Anaconda\ND_Data_Analyst_Project1\Intro_to_Data_Science\Problem_Set_2\Problem_1_num_rainy_days\weather_underground.csv"
    output_filename = "output.csv"
    student_df = max_temp_aggregate_by_fog(input_filename)
    student_df.to_csv(output_filename)