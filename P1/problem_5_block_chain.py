import hashlib
import time

class Block:

	def __init__(self, timestamp, data, previous_hash):
		self.timestamp = timestamp
		self.data = data
		self.previous_hash = previous_hash
		self.hash = self.calc_hash()

	def calc_hash(self):
		sha = hashlib.sha256()
		hash_str = self.data.encode('utf-8')
		sha.update(hash_str)

		return sha.hexdigest()

	def set_previous_hash(self,prev_hash):
		self.previous_hash = prev_hash

	def get_previous_hash(self):
		return self.previous_hash

	def get_hash(self):
		return self.hash

	def __repr__(self):
		return str({'data':self.data,'prev_hash':self.previous_hash,
				'hash':self.hash,'timestamp':self.timestamp})


class BlockNode:
    def __init__(self, data):
    	#The below statement to get the GMT time stamp is  googled from the internet 
       	timestamp = time.strftime("%a, %d %b %Y %I:%M:%S %p %Z", time.gmtime())
        self.block = Block(timestamp,data,None)
        self.next = None



class BlockChain:
	def __init__(self):
		self.head = None

	def display(self):
		cur_node = self.head
		i = 0
		while cur_node:
			print("-----Block Chain Node{}-----".format(i))
			print(cur_node.block)
			cur_node = cur_node.next
			i+=1


	def append(self, value):

		if self.head is None:
			self.head = BlockNode(value)
			return

		node = self.head
		while node.next:
			node = node.next

		node_hash = node.block.get_hash()
		node.next = BlockNode(value)
		node.next.block.set_previous_hash(node_hash)

	def size(self):
		size = 0
		node = self.head
		while node:
			size += 1
			node = node.next

		return size


if __name__ == '__main__':

	bc = BlockChain()

	data_l = ["What is the weather",
			  "Hi Udacity",
			  "Thanks for Preparing the program",
			  "I am able to enhance by data structures skills",
			  "Please keep adding good materials",
			  "Special Thanks to Sebasthian Thurn",
			  "I am one of his Fan",
			  "I am also Fan of Google from where I learnt python in 3 days"]

	for data in data_l:
		bc.append(data)
	bc.display()








