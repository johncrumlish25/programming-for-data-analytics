# program that reads in the data and outputs each line as a list
# Author: John Crumlish

import csv

FILENAME = "data.csv"
DATADIR = "../data/"

with open(DATADIR + FILENAME, "rt") as fp:
    reader = csv.reader(fp, delimiter=",", quoting=csv.QUOTE_NONNUMERIC)
    linecount = 0
    total = 0
    for line in reader:
        if not linecount: # header row 
            print (f"{line}\n-------------------") 
        else: # next rows 
            total += line[1] # why 1 
 
        linecount += 1 
    print (f"average is {total/(linecount-1)}") # why -1 ?