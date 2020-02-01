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
TASK 1:
How many different telephone numbers are there in the records? 
Print a message:
"There are <count> different telephone numbers in the records."
"""
"""
Complexity :  As there is are two  while loop is  each of O(n). 

Adding elements to Set is  O(1) . 
Finding the number of records in texts or calls or Set is O(1) . 
While creating the  Set, the number of elements present are tracked . 
So in constant time the  length can be printed . 
Worst case complexity of the below code is  O(n)
Space Complexity is  ie O(n) 
"""

i =0
tn_set = set()
while (i < len(texts)):
	tn_set.add(texts[i][0])
	tn_set.add(texts[i][1])
	i+=1

i =0
while(i < len(calls)):
	tn_set.add(calls[i][0])
	tn_set.add(calls[i][1])
	i+=1

print("There are %d different telephone numbers in the records."%(len(tn_set)))
