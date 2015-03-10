import sys

def reducer():
    '''
    Given the output of the mapper for this exercise, the reducer should return one row
    per unit, along with the total number of ENTRIESn_hourly over the course of may. 
    
    You can assume that the input to the reducer is sorted by UNIT, such that all rows 
    corresponding to a particular UNIT are group together.

    '''

    # intializing variables
    people_entered = 0
    unit_key = None

    for line in sys.stdin: # reading line by line
        
        data = line.strip().split("\t") # seperating data on the basis of tab
        
        if len(data) != 2: # checking row entry abnormalities
            continue
            
        this_key, count = data # assigning variables
        
        if unit_key and unit_key != this_key: # generating reducer output
            print "{0}\t{1}".format(unit_key, people_entered)
            
            people_entered = 0
            
        unit_key = this_key
        people_entered += float(count)
        
    if unit_key != None:
        print "{0}\t{1}".format(unit_key, people_entered) # generating final row of the reducer output

        



reducer()
