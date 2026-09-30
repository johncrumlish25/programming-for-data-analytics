# print out the dates of the bank holidays that are unique in Northern Ireland
# Author: John Crumlish

import requests 
 
url ="https://www.gov.uk/bank-holidays.json" 
response = requests.get(url) 
data = response.json() 

northern_ireland = data["northern-ireland"]["events"]
england = data["england-and-wales"]["events"]
scotland = data["scotland"]["events"]

other_holidays = []

for holiday in england:
    other_holidays.append(holiday["title"])

for holiday in scotland:
    other_holidays.append(holiday["title"])

for holiday in northern_ireland:
    if holiday["title"] not in other_holidays:
        print(holiday["date"], holiday["title"])