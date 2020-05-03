# P1 : LRU Cache 
LRUcache is  class . It implements two data structures . 
* Double linked list  . Double linked list is used so that the removing a reference to a node can be done  in O(1) time and adding to the beginning of the list also can be done in O(1) time 
* Dictionary .  It stores key and the value as the reference to the node whose value corresponds to the key . Finding the value of corresponding  key takes O(1) time . 

The class also has  a member variable that initializes the size of the cache when it is instantiated  . 


The LRU cache exposes below public functions  
* get(key) -  returns the item for a given key . If the get is not present then  -1 is returned.

As the cache is implemented as a dictionary
The function returns the  value for a key in O(1) time.
* set(key,value) - The function stores the key value pair as long as there is space in the cache . 
When the cache is full, the least recently used key-value pair is removed and replaced with the new key-value pair . The operations does not return any fail status . 
The function stores the value for a key in O(1)time complexity. 

 



