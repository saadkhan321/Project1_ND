import pandas

def time_to_hour(time):
    
    '''help source 
    http://stackoverflow.com/questions/5306079/
    python-how-do-i-convert-an-array-of-strings-to-an-array-of-numbers'''
    
    hour = hour = time[0:2] # spliting time in hours and assigning to hour
    hour = int(hour) # converting to intiger and assigning it back to hour 
    
    
    return hour

if __name__ == "__main__":
    input_filename = "turnstile_data_master_subset_consolidate_rows.csv"
    output_filename = "output.csv"
    turnstile_master = pd.read_csv(input_filename)
    student_df = turnstile_master.copy(deep=True)
    student_df['Hour'] = student_df['TIMEn'].map(time_to_hour)
    student_df.to_csv(output_filename)