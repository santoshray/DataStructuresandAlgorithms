import sys

class TreeNode:
	def __init__(self,ch,freq,left=None,right=None):
		self.ch = ch
		self.freq = freq
		self.left  = left
		self.right = right


	def add_left_child_node(self,node):
		self.left = node

	def add_right_child_node(self,node):
		self.right = node


class HuffmanTree:
	def __init__(self,root):
		self.root = root


def  calulate_frequency(string):
	d = dict()
	for ch in string:
		try:
			d[ch]+=1
		except:
			d[ch] =1
	return d 



def create_parent_node(left_node,right_node):
	ch = left_node.ch + right_node.ch
	freq = left_node.freq + right_node.freq
	pnode = TreeNode(ch,freq,left_node,right_node)
	return pnode

def create_huffman_tree(ch_dict):
	#convert  dict to  list 
	ch_list = []
	for key in ch_dict.keys():
		ch_list.append(TreeNode(key,ch_dict[key]))


	#take two nodes at a time and  create a node that is the parent of the two nodes chosen
	temp_ch_list = []
	while(len(ch_list)!=1):
		ch_list.sort(key=lambda node:node.freq , reverse = True)

		i = len(ch_list) -1
		while(i-1 >=0):
			right_node = ch_list.pop()
			left_node = ch_list.pop()

			pnode = create_parent_node(left_node,right_node)
			temp_ch_list.append(pnode)
			i-=2
			if(i ==0):
				node = ch_list.pop()
				temp_ch_list.append(node)
		ch_list = temp_ch_list


	huffman_tree  = HuffmanTree(ch_list.pop()) 
	
	return 	huffman_tree

def get_code_for_character(ch,huffman_tree):
	node  = huffman_tree.root
	code = ""
	while(node.ch != ch):
		if node.left.ch.find(ch) >=0:
			node = node.left
			code +="0"
		else:
			node = node.right
			code +="1"

	return code

def get_code_dict(huffman_tree):
	code_dict = dict()
	#print("characters:{}".format(huffman_tree.root.ch))
	for ch in huffman_tree.root.ch:
		code = get_code_for_character(ch,huffman_tree)
		code_dict[ch] = code
		#print("ch :{} code:{}".format(ch,code))

	#print("Code Dict : {}".format(code_dict))
	return code_dict

def get_encoded_string(data,huffman_tree):
	code_dict = get_code_dict(huffman_tree)
	encoded_data =""
	for ch in data:
		encoded_data+=code_dict[ch]

	return encoded_data

def huffman_encoding(data):
	f_dict = calulate_frequency(data)
	huffman_tree = create_huffman_tree(f_dict)
	encoded_data =  get_encoded_string(data,huffman_tree)
	return (encoded_data,huffman_tree)

def get_character(code_list,string):
	for obj  in code_list:
		if string.find(obj["value"]) == 0:
			return obj["key"]

def huffman_decoding(data,tree):
	code_dict = get_code_dict(tree)
	decoded_data = ""
	i = 0  
	encoded_data_len = len(data)
	code_list =[]
	for key in code_dict.keys():
		obj = {}
		obj["key"] = key
		obj["value"] =code_dict[key]
		code_list.append(obj)

	code_list.sort(key =lambda obj:len(obj["value"]) , reverse=True)
	#print("Code List:{}".format(code_list))

	while (i < encoded_data_len):
		ch = get_character(code_list,data[i:])
		decoded_data+=ch
		i += len(code_dict[ch])

	#print("Decoded Data : {}".format(decoded_data))
	return decoded_data



if __name__ == "__main__":

    a_great_sentence = "The bird is the word"

    print ("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence)))
    print ("The content of the data is: {}\n".format(a_great_sentence))

    encoded_data, tree = huffman_encoding(a_great_sentence)

    print ("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
    print ("The content of the encoded data is: {}\n".format(encoded_data))

    decoded_data = huffman_decoding(encoded_data, tree)

    print ("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
    print ("The content of the decoded data is: {}\n".format(decoded_data))	
