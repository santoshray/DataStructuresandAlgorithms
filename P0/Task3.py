"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv
import re

with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 3:
(080) is the area code for fixed line telephones in Bangalore.
Fixed line numbers include parentheses, so Bangalore numbers
have the form (080)xxxxxxx.)

Part A: Find all of the area codes and mobile prefixes called by people
in Bangalore.
 - Fixed lines start with an area code enclosed in brackets. The area
   codes vary in length but always begin with 0.
 - Mobile numbers have no parentheses, but have a space in the middle
   of the number to help readability. The prefix of a mobile number
   is its first four digits, and they always start with 7, 8 or 9.
 - Telemarketers' numbers have no parentheses or space, but they start
   with the area code 140.

Print the answer as part of a message:
"The numbers called by people in Bangalore have codes:"
 <list of codes>
The list of codes should be print out one per line in lexicographic order with no duplicates.

Part B: What percentage of calls from fixed lines in Bangalore are made
to fixed lines also in Bangalore? In other words, of all the calls made
from a number starting with "(080)", what percentage of these calls
were made to a number also starting with "(080)"?

Print the answer as a part of a message::
"<percentage> percent of calls from fixed lines in Bangalore are calls
to other fixed lines in Bangalore."
The percentage should have 2 decimal digits
"""
"""
Complexity : Time complexity of  While loop is  O(n) .
Within the While loop we are doing a regular expression Match.
The complexity depends on the length of the string In this case
the  Telephone numbers are limited to 10 to 12 characters. 
In this particular case it can be assumed to be constant as the inputs are of fixed length.
say O(K) where K is constant 

Adding elements to Set is  O(1). Union of two set is O(n)
Sorting the list is O(nlogn)
Worst case complexity of the below code is  O(nlogn)
Space Complexity is O(n)
Over time complexity is  O(n).
"""

tn_set = set()
fixed_lines_codes = set()
mobile_numbers_codes = set()
tele_marketers_codes =set()


re_fixed_line = '\(0[0-9]+\)'
re_mobile_number = '([7-9][0-9]{3})'
re_tele_market  = '140'
calls_to_blore = 0
calls_from_blore =0
i =0
while(i < len(calls)):
	if (calls[i][0].find('(080)') >=0):
		calls_from_blore +=1
		tn_set.add(calls[i][1])
		m = re.search(re_fixed_line,(calls[i][1]))

		if(m):
			fixed_lines_codes.add(m.group())
			if(m.group().find('(080)') >=0):
				calls_to_blore +=1

		m = re.match(re_mobile_number,(calls[i][1]))
		if m:
			mobile_numbers_codes.add(m.group())

		m= re.match(re_tele_market,calls[i][1])
		if m:
			tele_marketers_codes.add(m.group())

	i+=1

print("The numbers called by people in Bangalore have codes:")
s = fixed_lines_codes.union(mobile_numbers_codes).union(tele_marketers_codes)
for c in sorted(s):
	print(c)

print("%.2f percent of calls from fixed lines in Bangalore are calls"%(float((100*calls_to_blore)/calls_from_blore)))
print("to other fixed lines in Bangalore.")	