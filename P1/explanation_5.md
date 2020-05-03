# Problem 5 : Block Chain 

Implemented the code as per the problem specification 
* Each block contains a cryptographic hash of the previous block, a timestamp, and transaction data.
 * For the  blockchain implemented  SHA-256 hash, the Greenwich Mean Time  is used when the block was created, and text strings as the data.

A block node has four members  
1. hash value of the string is calculated in function calc_hash using SHA256 algorithm implemented by the python library hashlib 
2. timestamp is calculated  in GMT format using the time module 
3. data : a text string  
4. prev_hash : the hash value of the previous node . For the headnode the prev_hash is set to None.

The block chain implements the function  called append that add a Blocknode in O(n) . The block chain in implemented as a single linked list.
