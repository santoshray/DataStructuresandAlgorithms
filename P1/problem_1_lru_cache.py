
class Node:
	def __init__(self,data=None):
		self.prev = None
		self.next = None
		self.data = data

class DoubleLinkedList:
	def __init__(self):
		self.head  = None
		self.tail  = None

	def add_at_beginning(self,data):
		#The function returns the node as its reference 
		#can be passed later to deleted the node in O(1)

		node  = Node(data)

		if (self.head == None and self.tail == None) :
			# The list is empty
			self.head = node
			self.tail = node

			node.prev = None 
			node.next = None
			return node

		#else there is one or more node 
		node.next = self.head
		self.head.prev = node
		node.prev = None
		self.head = node 

		return node

	def display_items(self):
		cur_node = self.head
		while(cur_node!=None):
			print(cur_node.data)
			cur_node = cur_node.next

		return


	def remove_node(self,node):
		if self.head == None :
			print("The Double linked list is empty")
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
		print("get is called key={} ".format(key))

		if key in self.cache:
			node  =  self.cache[key]
			key,value = node.data
			self.dlist.remove_node(node)
			print("key= {},value={}".format(key,value))
			self.dlist.add_at_beginning((key,value))

			return value

		else:
			return -1
	        

	def set(self, key, value):
		# Set the value if the key is not present in the cache. If the cache is at capacity remove the oldest item. 
		print("set is called key={} value ={}".format(key,value))
		if len(self.cache) < self.size:
			#Add to dict and also add at beginning of the double linked list 

			self.cache[key] = self.dlist.add_at_beginning((key,value))
			print("cache_size = {}".format(len(self.cache)))
		else:
			#cache is full  remove the LRU 
			node = self.dlist.remove_from_tail()
			if node:
				k,v = node.data 
				print(k,v)
				self.cache.pop(k)

			if len(self.cache) < self.size:
				self.cache[key] = self.dlist.add_at_beginning((key,value))


if __name__ == '__main__':

	"""
	dlist = DoubleLinkedList()
	n1 = dlist.add_at_beginning((1,1))
	n2 = dlist.add_at_beginning((2,2))
	n3 = dlist.add_at_beginning((5,10))
	n4 =dlist.add_at_beginning((10,15))
	print("--------list the items-------")
	dlist.display_items()

	dlist.remove_node(n3)
	dlist.remove_node(n2)
	print("--------list the items-------")
	dlist.display_items()
	"""
	our_cache = LRUcache(5)

	our_cache.set(1, 1);
	our_cache.set(2, 2);
	our_cache.set(3, 3);
	our_cache.set(4, 4);


	print(our_cache.get(1) )      # returns 1
	print(our_cache.get(2) )      # returns 2
	print(our_cache.get(9))      # returns -1 because 9 is not present in the cache

	our_cache.set(5, 5)
	our_cache.set(6, 6)
	print(our_cache.get(3))      # returns -1 because the cache reached it's capacity and 3 was the least recently used entry


