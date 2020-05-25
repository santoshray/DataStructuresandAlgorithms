# Problem 5 : Block Chain 

**Design decision and data structure**
As specifed in the problem  single linked list is used .Code is implemented as per the problem specification 
* Each block contains a cryptographic hash of the previous block, a timestamp, and transaction data.
 
A block node has four members  
1. hash value of the string is calculated in function calc_hash using SHA256 algorithm implemented by the python library hashlib . 
The hash algo is run on the string resulting from the concatenation of  timestamp and data.
2. timestamp is calculated  in format  'yyyy-mm-dd hh:mm:ss' using the time module in python 
 the time module 
3. data : a text string  
4. prev_hash : the hash value of the previous node . For the headnode the prev_hash is set to None.

**Time Complexity** :
If there are n messages  to be added to the Block chain then it takes time complexity O(n)  to append a block . We can assume that the time complexity to  create the  block is O(1) .
As there are n blocks to be linked to one another as a single linked list . So the overall time complexity will be O(n^2)  [ appx of sumof (1+2+3 ..n)].  If we keep track of the end of the linked list then adding an block could take constant time making the algorithm O(n)

**Space complexity** :
As there are n blocks in the block chain each occupying constant space . So the space complexity wil be  O(n) 
