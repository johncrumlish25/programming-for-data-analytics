# print out the dates of the bank holidays that are unique in Northern Ireland
# Author: John Crumlish

import requests 
 
url ="https://www.gov.uk/bank-holidays.json" 
response = requests.get(url) 
data = response.json() 

# get bank holidays for each part of the UK 
northern_ireland = data["northern-ireland"]["events"]
england = data["england-and-wales"]["events"]
scotland = data["scotland"]["events"]

# empty list
other_holidays = []

# add holidays to empty list
for holiday in england:
    other_holidays.append(holiday["title"])

for holiday in scotland:
    other_holidays.append(holiday["title"])

# print holidays that have not already been added to the list
for holiday in northern_ireland:
    if holiday["title"] not in other_holidays:
        print(holiday["date"], holiday["title"])