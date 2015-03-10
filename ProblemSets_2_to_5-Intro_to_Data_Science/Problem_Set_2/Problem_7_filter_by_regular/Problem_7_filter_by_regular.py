import pandas as pd

def filter_by_regular(filename):

    # Sources: Lesson 1 - Intro to Data Science
    # Sources: Lesson 2 - Intro to Data Science
    # Sources: http://stackoverflow.com/questions/11869910/pandas-filter-rows-of-dataframe-with-operator-chaining
        
    turnstile_data = pandas.read_csv(filename) # reading the csv into the DataFrame
     
    turnstile_data = turnstile_data[turnstile_data['DESCn'] == 'REGULAR'] # filtering by REGULAR (recalled from lesson 1)
    
    return turnstile_data


if __name__ == "__main__":
    input_filename = "turnstile_data_master.csv"
    output_filename = "output.csv"
    student_df = filter_by_regular(input_filename)
    student_df.to_csv(output_filename)
    