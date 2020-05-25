# Problem 6 : Union and intersection of  lists
**Design Choice and Data structures** 
set A union set B: Finding the  elements that are present in both set A  and Set B . 
This requires creating a linked list that has the nodes with data present in both A and B . 
List A  and List B are converted to dictionary say dict A and dict B  . dict C is created that has the elements that is either present in List A or List B or both  with the total frequency of occurrence . 
List C is created from  dict C and is returned as result. 

Using intermediate dictionary helps in keeping the frequency of occurence of an element in  List A or List B  and also helps in  linear time complexity. 

set A intersection  set B : Finding the number of elements that are present is both A and B . 

As the List A and List B are converted to dict A and dict B   finding the common elements is easy with linear time complexity . 


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
