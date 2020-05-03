# Problem 3: Huffman Coding

Huffman coding implements two user functions  
1. huffman_encoding(data) : it takes the sentence to be encoded and returns the huffman tree and the encoded data as a string of bytes. 
Complexity of encoding the data once the huffman tree is created is O(n). Overall complexity is O(n)
2. huffman_decoding(data,huffman_tree): It takes the encoded data and the huffman_tree as the input and returns the decoded data or sentence . 
Complexity of the function is O(n) 

There are helper functions  as below  
* create_huffman_tree() : In order to create the huffman tree a dictionary that contains the frequency of occurence of each character  is required. We have to create the tree using the bottom -up approach where the leaf-nodes are the keys of the dictionary . The complexity to create the character frequecy dictionary is O(n) where n is the num of characters  .  The complexity to create the huffman tree is O(mlogm) when m is the number of unique characters in the data . At every level x of the tree the number of nodes  is approximately half the number of nodes in level x+1. Also at every level the  nodes are sorted based on the  updated frequency so that it will be ensured the most frequently occuring  characted gets the least length binary code and increasing compression ratio .