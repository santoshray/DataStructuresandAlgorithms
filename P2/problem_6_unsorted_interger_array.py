import random
def get_min_max(ints):
	i  =0
	int_len = len(ints)
	min_x = ints[i]
	max_x = ints[i]
	while i < int_len :
		if (ints[i] < min_x):
			min_x = ints[i]

		if(ints[i] > max_x):
			max_x = ints[i]

		i+=1

	return(min_x,max_x)




if __name__ == '__main__':
	l = [i for i in range(0, 10)]  # a list containing 0 - 9
	random.shuffle(l)

	print ("Pass" if ((0, 9) == get_min_max(l)) else "Fail")

	print()
