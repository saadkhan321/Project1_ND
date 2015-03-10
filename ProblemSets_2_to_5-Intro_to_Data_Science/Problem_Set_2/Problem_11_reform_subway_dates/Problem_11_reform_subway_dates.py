import datetime

def reformat_subway_dates(date):
    

    # help source :
    # http://stackoverflow.com/questions/14524322/
    # how-to-convert-a-date-string-to-different-format-in-python

    date_formatted = datetime.datetime.strptime(date, '%m-%d-%y').strftime('%Y-%m-%d') # converts the format as required %Y keep the year in eg '2005' format
    
   
   
    return date_formatted

if __name__ == "__main__":
    input_filename = "turnstile_data_master_subset_time_to_hours.csv"
    output_filename = "output.csv"

    turnstile_master = pd.read_csv(input_filename)
    student_df = turnstile_master.copy(deep=True)
    student_df['DATEn'] = student_df['DATEn'].map(reformat_subway_dates)
    student_df.to_csv(output_filename)
