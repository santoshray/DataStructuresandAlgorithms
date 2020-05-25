# Problem 4 : Active Directory

**Design Choice and Data Structures** : 
In this problem users belong to one or more groups . Also one group can be be subgroup of another group  and so on . In order to find the  whether a particular user belongs to a given group . The logic starts by finding the user in the group given . If he is not present , then the list of subgroups are found and the user is recurcively searched in each sub groups until all the users  added to the group or one of the subgroups are searched.

As recursion is used, the data structure that will be implicity used  is Stack .

**Time Complexity**:
If there are n users added in m groups .The time complexity to find a user is present in a group is O(n) 

**Space Complexity**:
Space required to store the information for m groups and n users will be O(m+n) 
