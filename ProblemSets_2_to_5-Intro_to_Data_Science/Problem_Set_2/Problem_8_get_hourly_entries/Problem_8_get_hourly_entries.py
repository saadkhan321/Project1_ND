import pandas as pd

def get_hourly_entries(df):
    
    # Sources: Lesson 1 - Intro to Data Science
    # Sources: Lesson 2 - Intro to Data Science
    # Sources: http://stackoverflow.com/questions/11869910/pandas-filter-rows-of-dataframe-with-operator-chaining
    
    df['ENTRIESn_hourly'] = 0 # Initializing
    df['ENTRIESn_hourly'] = df['ENTRIESn'] - df['ENTRIESn'].shift(1) # taking the difference and filling 'ENTRIESn_hourly'
    df['ENTRIESn_hourly'] = df['ENTRIESn_hourly'].fillna(1) # replacing NaN with 1
    return df

if __name__ == "__main__":
    input_filename = "turnstile_data_master_subset_regular.csv"
    output_filename = "output_csv.csv"
    turnstile_master = pd.read_csv(input_filename)
    student_df = turnstile_master.groupby(['C/A','UNIT','SCP']).apply(get_hourly_entries)
    student_df.to_csv(output_filename)