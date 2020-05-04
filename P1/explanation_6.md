# Problem 6 : Union and intersection of  lists

**Time Complexity** :
Creating a linked list: O(n) where n is length number of elements in the list.
Display the elements : O(n) where  n in the number of elements in the list  
Union :O(n1 + n2) to create two dictionaries from  linked list with n1 elements 
and linked list with n2 elements . 
It also takes O(n1+n2) to do the union of two list.  
Intersection : O(n1+n2) to do the intersection operation of two list.

**Space Complexity**: 

Insert a path: O(n1)  to create  linked list with num elements n1  
O(n2) to create linked list with num elements n2 
O(n1+n2) to create linked list of  union operation. 
Worst case O(Max(n1,n2)) to create linked list of  intersection operation.
O(n1) to  create dictionary from list1 
O(n2) to create dictionary from list2
