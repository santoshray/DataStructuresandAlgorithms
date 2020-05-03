def rotated_array_search(input_list, number):
	"""
	Find the index by searching in a rotated sorted array

	Args:
	   input_list(array), number(int): Input array to search and the target
	Returns:
	   int: Index or -1
	"""
	l =0 
	h = len(input_list) -1
	while (l < h):
		m = (l+h)//2
		print ("low ={} mid ={} high ={} target ={}".format(l,m,h,number))
		if(input_list[m] == number):
			return m
		if(input_list[h] == number):
			return h
		if(input_list[l] == number):
			return l

		if(number < input_list[m] and  number < input_list[h]):
			l = m

		elif(number < input_list[m] and  number > input_list[h]):
			h =m
		elif(number > input_list[m] and  number > input_list[h]):
			h =m 
		elif(number > input_list[m] and  number < input_list[h]):
			l=m

	return -1


if __name__ == '__main__':
	
	l=[4,5,6,7,0,1,2]
	t = 0
	print(l,t)

	print("Target = {} index ={}".format(t,  rotated_array_search(l,t)))
	t=1
	print("Target = {} index ={}".format(t,  rotated_array_search(l,t)))
	t=2
	print("Target = {} index ={}".format(t,  rotated_array_search(l,t)))
	t = 4
	print("Target = {} index ={}".format(t,  rotated_array_search(l,t)))
	t = 10
	print("Target = {} index ={}".format(t,  rotated_array_search(l,t)))
	t = 5
	print("Target = {} index ={}".format(t,  rotated_array_search(l,t)))
	t = 7
	print("Target = {} index ={}".format(t,  rotated_array_search(l,t)))
