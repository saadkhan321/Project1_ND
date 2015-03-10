import csv
import pandas as pd

def fix_turnstile_data(filenames):

    # Sources: Lesson 2 - Intro to Data Science
    # Sources: https://piazza.com/class/i23uptiifb6194?cid=133
    # https://docs.python.org/2/library/csv.html
    # https://docs.python.org/2/library/functions.html#open

    for name in filenames: # stores the filenames
        
        with open(name, 'rb') as a: # reading the file in binary format using open()
            reader = csv.reader(a)
            for row in reader:
                
                first_part = row[0:3] # first bit that is going to repeat itself
                
                second_part = row[3:] # second bit that is going to be appended
                
                updated = [] # Initializing
                with open("updated_" + name, 'ab') as b: # appending the file in binary format using open()
                    writer = csv.writer(b)
                    x = 0
                    for i in range (len(second_part)/5): # traversing the row
                         updated = first_part + second_part[x:(x+5)]
                         writer.writerow(updated)
                         x = x+5

        

if __name__ == "__main__":
    input_files = ['turnstile_110528.txt', 'turnstile_110604.txt']
    fix_turnstile_data(input_files)
