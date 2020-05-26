# Problem 5 : Auto-complete using TRIE

**Design decision and  Data structure**
The problem is given to be solved with TRIE data stucture to store  n words  of varied word length the max may be of length m .

 **Time complexity** : 

 Insert a word :To insert a word of length of m the time complexity is O(m) where m is the length of the word. To create  the  trie data structure to store n words the time complexity is O(m+n)

 Find a word of length m: O(m) 

Find the list of words with prefix:Time complexity is O(m+n) where n in the number of words that match with prefix with length m.

 **Space complexity** :
 To maintain the Trie structure where we are storing the information for n words with worst case length m the space complexity is  O(n*m)