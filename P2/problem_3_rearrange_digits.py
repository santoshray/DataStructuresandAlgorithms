class heap:
	def __init__(self,l):
		self.a = l
		self.capacity = len(l)
		self.size  = 0 

	def create_heap(self,l):
		i =0 
		list_len = len(l)
		while i < list_len:
			self.insert_element(l[i],i)
			i+=1

	def has_left_chid(self,idx):
		return self.left_child_index(idx) < self.size 

	def has_right_chid(self,idx):
		return self.right_child_index(idx) < self.size

	def has_parent(self,idx):
		return self.parent_index(idx) >=0 
	
	def left_child_index(self,idx):
		return 2*idx+1

	def right_child_index(self,idx):
		return 2*idx+2

	def parent_index(self,idx):
		return (idx-1)//2


	def get_left_child(self,idx):
		return self.a[self.left_child_index(idx)]

	def get_right_child(self,idx):
		return self.a[self.right_child_index(idx)]

	def get_parent(self,idx):
		return self.a[self.parent_index(idx)]


	def insert_element(self,num,last_index):
		self.heapify_up(num,last_index)
		self.size +=1


	def swap(self,a,i,j):
		 a[j],a[i]  = a[i],a[j]

	def heapify_up(self,num,last_index):
		if (last_index == 0):
			return
		self.a[last_index] = num 
		p_idx = self.parent_index(last_index)
		while p_idx >=0  and self.a[last_index] < self.a[p_idx] :
			self.swap (self.a,p_idx,last_index )
			last_index = p_idx
			p_idx = self.parent_index(last_index)


	def heapify_down(self):

		idx = 0
		while (self.has_left_chid(idx)):
			smaller_idx =  self.left_child_index(idx)
			if (self.has_right_chid(idx) and (self.get_right_child(idx) < self.get_left_child(idx))):
				smaller_idx =  self.right_child_index(idx)

			if (self.a[idx] < self.a[smaller_idx]):
				break
			else:
				self.swap(self.a,idx,smaller_idx)

			idx = smaller_idx

	def peek(self):
		if self.size == 0 :
			return None 

		return self.a[0]

	def pop(self):
		x = self.a[0]
		self.swap(self.a,0,self.size-1)
		self.size -=1
		self.heapify_down()
		return x

	def sort(self):
		sl = []
		l = len(self.a)
		while l > 0 :
			sl.append(self.pop())
			l -=1
		return sl
	#create heap 

def heap_sort(a):
	h= heap(a)
	h.create_heap(a)
	return h.sort()


def rearrange_digits(a):
	l = heap_sort(a)
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

	print("\n---Test case 1 ---")
	input_list = [1,2,3,4,5]
	print("rearranged list :{} o/p:{}".format(input_list,rearrange_digits(input_list)))

	print("\n---Test case 2 ---")
	input_list = [4, 6, 2, 5, 9, 8]
	print("rearranged  list :{} o/p:{}".format(input_list,rearrange_digits(input_list)))

	print("\n---Test case 3 ---")
	input_list = []
	print("rearranged list :{} o/p:{}".format(input_list,rearrange_digits(input_list)))


	print("\n---Test case 4 ---")
	input_list = [1,0,0,1]
	print("rearranged list :{} o/p:{}".format(input_list,rearrange_digits(input_list)))

