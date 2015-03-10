def create_master_turnstile_file(filenames, output_file):

    # Sources: Lesson 2 - Intro to Data Science
    # Sources: https://docs.python.org/2/tutorial/inputoutput.html
    
    with open(output_file, 'w') as master_file: # writing to the output_file in binary format using open()
       master_file.write('C/A,UNIT,SCP,DATEn,TIMEn,DESCn,ENTRIESn,EXITSn\n')
       for filename in filenames:
                
                
                with open(filename, 'rb') as f:
                    read_data = f.readlines() # readline()
                    #print read_data
                    output_file= [] # Initializing
                    for row in read_data: # iterating through the files
                         output_file = [master_file.write(row)] # writing back into the output_file
                

if __name__ == "__main__":
    input_files = ['turnstile_110528.txt', 'turnstile_110604.txt']
    output = "turnstile_data_master.csv"
    create_master_turnstile_file(input_files, output)