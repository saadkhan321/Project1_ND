import pandas

def get_hourly_exits(df):
    
    # Sources: Lesson 1 - Intro to Data Science
    # Sources: Lesson 2 - Intro to Data Science
    # Sources: http://stackoverflow.com/questions/11869910/pandas-filter-rows-of-dataframe-with-operator-chaining

    df['EXITSn_hourly'] = 0 # Initializing
    df['EXITSn_hourly'] = df['EXITSn'] - df['EXITSn'].shift(1) # taking the differnece and filing 'EXITSn_hourly'
    df['EXITSn_hourly'] = df['EXITSn_hourly'].fillna(0) # replacing NaN with 0
   
    return df

if __name__ == "__main__":
    input_filename = "turnstile_data_master_subset_get_hours_entries.csv"
    output_filename = "output.csv"
    turnstile_master = pd.read_csv(input_filename)
    student_df = turnstile_master.groupby(['C/A','UNIT','SCP']).apply(get_hourly_exits)
    student_df.to_csv(output_filename)