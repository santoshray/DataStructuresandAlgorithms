# Problem 7 : Request routing in a web server using Trie

**Design decision and  Data structure**
The problem is given to be solved with TRIE data stucture to store  n urls with valid handlers of varied word length the max may be of length m 

**Time Complexity** :
Insert a url: O(m) where m is length of the url. path. Time complexity is O(m) to find the whether there is a valid handler for a url or not  . 

**Space Complexity**: 

Space complexity to store n URL handlers  where m is the worst case length for the URL is  O(n*m)