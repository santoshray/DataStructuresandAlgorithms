
def sort_012(a):
	p0=0
	p2=len(a)-1
	i =0 

	while ( a[p2] ==2):
		p2 -=1

	print("p2=",p2)

	while (a[p0]==0):
		p0+=1
	print("p0=",p0)

	i =p0
	while(i <= p2 ):

		print("At beginning i={},p2={},p0={}".format(i,p2,p0))
		if(a[i] ==0):
			print("Inside 02 found 0 at i =".format(i))
			swap(a,i,p0)
			print(a)
			while(a[p0] == 0):
				p0+=1

			if(a[i] ==2):
				print("Inside 02 found 2 at i =".format(i))
				swap(a,i,p2)
				print(a)
				while(a[p2] == 2):
					p2-=1

		if(a[i] ==2):
			print("Inside 20 found 2 at i ={}".format(i))
			swap(a,i,p2)
			print(a)
			while(a[p2] == 2):
				p2-=1

			if(a[i] ==0):
				print("Inside 20 found 0 at i ={}".format(i))
				swap(a,i,p0)
				print(a)
				while(a[p0] == 0):
					p0+=1


		i+=1
		print("At end i={},p2={},p0={}".format(i,p2,p0))


	print (a)

def swap(a , i,j):
	t =a[i]
	a[i] = a[j]
	a[j] = t 

if __name__ == '__main__':
	a=[0, 0, 2, 2, 2, 1, 1, 1, 2, 0, 2]
	print("original list = {}".format(a))
	sort_012(a)

	print(a)