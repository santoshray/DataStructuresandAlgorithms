"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
The text data (text.csv) has the following columns:
sending telephone number (string),
receiving telephone number (string),
timestamp of text message (string).

The call data (call.csv) has the following columns:
calling telephone number (string), 
receiving telephone number (string), 
start timestamp of telephone call (string),
duration of telephone call in seconds (string)
"""
"""
TASK 0:
What is the first record of texts and what is the last record of calls?
Print messages:
"First record of texts, <incoming number> texts <answering number> at time <time>"
"Last record of calls, <incoming number> calls <answering number> at time <time>, lasting <during> seconds"
"""
"""
Complexity :  There is no while loop . 
Please note that reading the  data from csv file is not being considered  . 
To get the first and last record it takes constant time . 
So the below code's Time complexity is  O(1). Space complexity is O(1) 
"""

incoming_number = texts[0][0]
print("First record of texts, %s texts %s at time %s"%(texts[0][0],texts[0][1],texts[0][2]))

lcr_idx = len(calls) - 1
print("Last record of calls, %s calls %s at time %s, lasting %s seconds"%(calls[lcr_idx][0],calls[lcr_idx][1],calls[lcr_idx][2],calls[lcr_idx][3]))
