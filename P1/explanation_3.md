# Problem 3: Huffman Coding. 

**Design Decision and Data structure** :
In Huffman coding , it it required to create a dynamic dictionary having the encoded bitstream for a particular symbol based on the frequency of its occurrence in the  sequence of data. 

The logic defined by the algorithm to build the dictionary requires building the Huffman Tree using a bottom-up approach . 
The leaf nodes represent the unique symbol that occur in data sequence . Any node in a level contains the sum of the frequency of of two child-nodes . The root node contains the length of the sequence. The tree is built up in such a way that traversing down from the root to the leaf node assigns a unique code to a symbol whose encoded data  does not match as prefix with any other  symbol's encoded data .

**Implementaion and Complexity**:

Huffman coding implements two user functions  
1. huffman_encoding(data) : it takes the sentence to be encoded and returns the huffman tree and the encoded data as a string of bytes. 
Complexity of encoding the data once the huffman tree is created is O(n). Overall complexity is O(n)
2. huffman_decoding(data,huffman_tree): It takes the encoded data and the huffman_tree as the input and returns the decoded data or sentence . 
Complexity of the function is O(n) 


There are helper functions  as below  
* create_huffman_tree() : In order to create the huffman tree a dictionary that contains the frequency of occurence of each character  is required. We have to create the tree using the bottom -up approach where the leaf-nodes are the keys of the dictionary . The complexity to create the character frequecy dictionary is O(n) where n is the num of characters  .  The complexity to create the huffman tree is O(mlogm) when m is the number of unique characters in the data . At every level x of the tree the number of nodes  is approximately half the number of nodes in level x+1. Also at every level the  nodes are sorted based on the  updated frequency so that it will be ensured the most frequently occuring  character gets the least length binary code and increasing compression ratio .

**Time and space complexity**:

Frequency table  : for n characters in data sequence  time complexity is O(n) . If m is the number of unique symmbols then space complexity is O(m)  for creating the dictioanry. 

Huffman Tree : For m unique symbols the time complexity is mlog(m) . Space complexity is O(m) 

