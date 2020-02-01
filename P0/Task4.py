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
TASK 4:
The telephone company want to identify numbers that might be doing
telephone marketing. Create a set of possible telemarketers:
these are numbers that make outgoing calls but never send texts,
receive texts or receive incoming calls.

Print a message:
"These numbers could be telemarketers: "
<list of numbers>
The list of numbers should be print out one per line in lexicographic order with no duplicates.
"""

"""
Complexity :  Time complexity for executing While loop is  O(n).
Adding elements to Set is  O(1) . Union of two set is O(n)
Sorting the list is O(nlogn)
Worst case complexity of the below code is  O(nlogn)
Space Complexity is O(n)
"""
i =0
ncalls = len(calls)
ntexts = len(texts)
outgoing_call_set = set()
incoming_call_set =set()
send_receive_text_set = set()
while(i < max(ncalls,ntexts)):
	if ( i< ncalls):
		outgoing_call_set.add(calls[i][0])
		incoming_call_set.add(calls[i][1])

	if(i < ntexts):
		send_receive_text_set.add(texts[i][0])
		send_receive_text_set.add(texts[i][1])

	i+=1

s = incoming_call_set.union(send_receive_text_set)
for num in s:
	if num in outgoing_call_set:
		outgoing_call_set.remove(num)



telemarketers_list = sorted(outgoing_call_set)
print("These numbers could be telemarketers:" )
for t in telemarketers_list:
	print(t)
