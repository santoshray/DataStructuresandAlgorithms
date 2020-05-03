

def rearrange_digits(input_list):
	l = sorted(input_list)
	list_len = len(l)
	num1 = get_num(l,list_len,0,2)
	num2 = get_num(l,list_len,1,2)

	if (num2 > num1):
		return [num2,num1]
	else:
		return [num1,num2]


def get_num(input_list,list_len,start_idx,step):

	i = start_idx
	k =1
	num =0
	while i < list_len :	
		d = input_list[i]
		num += d*k
		k*=10
		i+=step

	return num

if __name__ == '__main__':
	input_list = [1,2,3,4,5]

	print(rearrange_digits(input_list))

	input_list = [4, 6, 2, 5, 9, 8]
	print(rearrange_digits(input_list))


