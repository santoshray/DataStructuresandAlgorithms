"""
Read file into texts and calls.
It's ok if you don't understand how to read files
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during 
September 2016.".
"""
"""
Complexity :  Time Complexity for executing While loop is  O(n).
Adding elements to to dictionary is  O(1) .
Union of two set is O(n)
Sorting the list is O(nlogn)
Worst case complexity of the below code is  O(nlogn)
Space Complexity is O(n)
"""

time_spent_dict = dict()
i =0
while(i < len(calls)):
	try:
		time_spent_dict[calls[i][0]] += int(calls[i][3])
	except:
		time_spent_dict[calls[i][0]] = int(calls[i][3])

	try:
		time_spent_dict[calls[i][1]] += int(calls[i][3])
	except:
		time_spent_dict[calls[i][1]] = int(calls[i][3])

	i+=1

#ph_num= sorted(time_spent_dict, key=time_spent_dict.get ,reverse=True)[0]
ph_num= max(time_spent_dict, key=time_spent_dict.get )

print("%s spent the longest time, %d seconds, on the phone during September 2016."%(ph_num,time_spent_dict[ph_num]))