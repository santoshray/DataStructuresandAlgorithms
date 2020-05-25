
def sort_012(a):

	#position_0 - variable that points to the index in array a where  for all i, 0<i<position_0 a[i] = 0  
	#position_2 - variable that points to the index in array a where  for all i, position_2<i<len(a) a[i] = 2  
	a_len = len(a)
	if (a_len == 0 ):
		return []

	position_0=0
	position_2=a_len-1
	i =0 

	while ( a[position_2] ==2):
		position_2 -=1


	while (a[position_0]==0):
		position_0+=1

	i =position_0
	while(i <= position_2 ):

		if(a[i] ==0):
			swap(a,i,position_0)
			while(a[position_0] == 0):
				position_0+=1

			if(a[i] ==2):
				swap(a,i,position_2)
				print(a)
				while(a[position_2] == 2):
					position_2-=1

		if(a[i] ==2):
			swap(a,i,position_2)
			while(a[position_2] == 2):
				position_2-=1

			if(a[i] ==0):
				swap(a,i,position_0)
				while(a[position_0] == 0):
					position_0+=1


		i+=1



def swap(a , i,j):
	t =a[i]
	a[i] = a[j]
	a[j] = t 

if __name__ == '__main__':

	print("\n---Test Case 1---")
	a=[0, 0, 2, 2, 2, 1, 1, 1, 2, 0, 2]
	print("original list a : {}".format(a))
	sort_012(a)
	print("after sort012(a) :{}".format(a))


	print("\n---Test Case 2---")
	a=[]
	print("original list a : {}".format(a))
	sort_012(a)
	print("after sort012(a) :{}".format(a))

	print("\n---Test Case 3---")
	a=[1,1,1,1,2,2,2,0]
	print("original list a : {}".format(a))
	sort_012(a)
	print("after sort012(a) :{}".format(a))

	print("\n---Test Case 4---")
	a=[0,0,0,2,2,2]
	print("original list a : {}".format(a))
	sort_012(a)
	print("after sort012(a) :{}".format(a))

	print("\n---Test Case 5---")
	a=[0,1,0,1,]
	print("original list a : {}".format(a))
	sort_012(a)
	print("after sort012(a) :{}".format(a))


	print("\n---Test Case 6---")
	a=[1,1]
	print("original list a : {}".format(a))
	sort_012(a)
	print("after sort012(a) :{}".format(a))


	print("\n---Test Case 6---")
	a=[1,1]
	print("original list a : {}".format(a))
	sort_012(a)
	print("after sort012(a) :{}".format(a))
