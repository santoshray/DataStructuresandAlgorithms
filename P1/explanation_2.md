# Problem 2 : File Recursion

**Design decision and  data structures**
Files are present in folders and a folder can contain another folder . Once a file is found there it needs to be decided  whether it has a particular extension or not(in this case it is looked of .c). As long as a file is not encountered in a folder , the logic keeps concatenating the folder name to the current path and keeps looking of files in the list of directories present in a current folder  . 

As the algorithm uses recursion , The data structure used is Stack .
**Time Complexity**  
If there are n files  present accross  m folders 
the time complexity is O(n)  to look for all the files in a recurcive manner. 

**Space Complexity**
For m folders are n files  the Space complexity is still O(n+m)  appx O(n)
