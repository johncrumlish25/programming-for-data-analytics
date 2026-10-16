# Find text in smaller-log using regex
# Author: John Crumlish

import re 

regex = "\[.*\]" 
FILENAME = "smaller-acess.log"
DATADIR = "../data/"

with open(DATADIR + FILENAME) as inputFile: 
    for line in inputFile: 
        foundTextList = re.findall(regex, line) 
        if (len(foundTextList)!= 0): 
            #print(foundTextList) 
            foundText = foundTextList[0] 
            print(foundText) 
            # if I did not want the [] at the beginning and end 
            print(foundText[1:-1]) 