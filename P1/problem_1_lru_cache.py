
class Node:
	def __init__(self,data=None):
		self.prev = None
		self.next = None
		self.data = data

class DoubleLinkedList:
	def __init__(self):
		self.head  = None
		self.tail  = None

	def add_at_beginning(self,data,node):
		#The function returns the node as its reference 
		#can be passed later to deleted the node in O(1)
		if node == None: 
			node  = Node(data)

		if (self.head == None and self.tail == None) :
			# The list is empty
			self.head = node
			self.tail = node

			self.head.prev = None 
			self.head.next = None
			return node

		#if there is one or more node  
		self.head.prev = node
		node.next = self.head
		self.head = node 
		self.head.prev = None

		return node

	def display_items(self):
		cur_node = self.head
		print("\nList from Head  to Tail")
		s =""
		while(cur_node!=None):
			s+=str(cur_node.data)+"->"
			cur_node = cur_node.next

		print(s)

		cur_node = self.tail
		print("\nList from Tail to Head")

		s =""
		while(cur_node!=None):
			s+=str(cur_node.data)+"->"
			cur_node = cur_node.prev

		print(s)
		return


	def remove_node(self,node):
		if self.head == None :
			return None

		#if there is only one node 
		if self.head == node and self.tail ==node:
			self.head = None
			self.tail = None
			return node

		#if the node in the head of the double linked list 
		if self.head == node:
			self.head.next.prev =None
			self.head = self.head.next
			return node

		#if node is the tail of the double linked list  
		if self.tail == node:
			self.tail.prev.next = None
			self.tail = self.tail.prev
			return node 

		#if node is in any other position of double linked list 

		node.prev.next = node.next
		node.next.prev = node.prev 
		return node

	def remove_from_tail(self):

		if self.head == None:
			return None

		node = self.tail
		node.prev.next = None
		self.tail = node.prev

		return node




class LRUcache:
	def __init__(self,size =5):
		self.size = size
		self.dlist = DoubleLinkedList()
		self.cache = dict()


	def get(self, key):
		# Retrieve item from provided key. Return -1 if nonexistent.
		#check if the  key is present in the  cache  
		#if present  
		#Remove the data and add at beginning of the linked list
		#return the value corresponding to the key
		if self.size < 0:
			return -1
		if key in self.cache :
			node  =  self.cache[key]
			key,value = node.data
			
			#self.dlist.display_items()
			self.dlist.remove_node(node)
			self.dlist.add_at_beginning(None,node)

			return value

		else:
			return -1
	        

	def set(self, key, value):
		# Set the value if the key is not present in the cache. 
		#If the cache is at capacity remove the oldest item. 
		if self.size <=0:
			return

		if  len(self.cache) < self.size:
			self.cache[key] = self.dlist.add_at_beginning((key,value),None)
		else:
			#cache is full  remove the LRU 
			node = self.dlist.remove_from_tail()
			if node:
				k,v = node.data 
				self.cache.pop(k)

				self.cache[key] = self.dlist.add_at_beginning((key,value),None)


if __name__ == '__main__':

	print("\n---Test 1 ----")
	our_cache = LRUcache(5)
	key,value = 1,1
	print("\nset is called key={} value ={}".format(key,value))
	our_cache.set(1, 1);

	key,value = 2,2
	print("\nset is called key={} value ={}".format(key,value))
	our_cache.set(2, 2);

	key,value = 3,3
	print("\nset is called key={} value ={}".format(key,value))
	our_cache.set(3, 3);

	key,value = 4,4
	print("\nset is called key={} value ={}".format(key,value))
	our_cache.set(4, 4);

	key=1
	print("\nget({}) returns:{}".format(key,our_cache.get(key)))	# returns 1

	key=2
	print("\nget({}) returns:{}".format(key,our_cache.get(key)))	# returns 2

	key=9
	print("\nget({}) returns:{}".format(key,our_cache.get(key)))	# returns -1 because 9 is not present in the cache

	key,value = 5,5
	print("\nset is called key={} value ={}".format(key,value))
	our_cache.set(5, 5)

	key,value = 6,6
	print("\nset is called key={} value ={}".format(key,value))
	our_cache.set(6, 6)

	key=3
	print("\nget({}) returns:{}".format(key,our_cache.get(key)))	# returns -1 because the cache reached it's capacity and 3 was the least recently used entry


	print("\n---Test 2 ----")
	our_cache = LRUcache(-1)
	key,value = 1,1
	print("\nset is called key={} value ={}".format(key,value))
	our_cache.set(1, 1)  

	key,value = 1,1
	print("\nset is called key={} value ={}".format(key,value))
	our_cache.set(7, 14)

	key=7
	print("\nget({}) returns:{}".format(key,our_cache.get(key)))	# returns  -1 as the  the cache size is set to  -1
	
	key=3
	print("\nget({}) returns:{}".format(key,our_cache.get(key)))	# returns  -1 as the  the cache size is set to  -1

	print("\n---Test 3 ---")
	c  =  LRUcache(3)
	key,value = "fruit","Apple"
	print("\nset is called key={} value ={}".format(key,value))
	c.set(key,value)
	key,value = "veg","Potatoes"
	print("\nset is called key={} value ={}".format(key,value))
	c.set(key,value)

	key,value = "games","Chess"
	print("\nset is called key={} value ={}".format(key,value))
	c.set(key,value)

	key = "fruit"
	print("\nget({}) returns:{}".format(key,c.get(key)))  # returns  "Apple" 

	key,value = "sports","Chess"
	print("\nset is called key={} value ={}".format(key,value))
	c.set("sports","Chess")   #replaces the key "veg"

	key = "veg"
	print("\nget({}) returns:{}".format(key,c.get(key)))  # #returns -1 as the  key is not present 

	key,value = "veg","Tomatoes"
	print("\nset is called key={} value ={}".format(key,value))

	key="fruit"
	print("\nget({}) returns:{}".format(key,c.get(key)))  #Returns Apple 

	key ="games"
	print("\nget({}) returns:{}".format(key,c.get(key))) # Returns Chess

	key = "fruit"
	print("\nget({}) returns:{}".format(key,c.get(key)))  #Returns Apple
	
	key = "veg"
	print("\nget({}) returns:{}".format(key,c.get(key)))  #Returns Tomatoes

