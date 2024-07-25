- definition of array [[What is Array?]]
- Memory representation of an array.![[Pasted image 20240724163953.png]]
- as seen the array size of each block to block is increased by 4, common way to store integer you knw!
- declaration of an array can be different for diff language but common examples are 
	- **int arr[5];**
- intialization cab=n be done like 
	- **char arr[] = { 'a', 'b', 'c', 'd', 'e' };**

#importanceofarray 
# Importance of an array 
wll, in short array offers a DS where a same type of data can be stored and retrived easily, take below example where it would have been hard to store marks of student using different variable, so rather we can store it in array easily
![[Pasted image 20240724184050.png]]

# types of Array #arraytype
We can define array 2 ways basically.
1. one with how memory is allocated 
2. one with dimension 

A picture to explain classification: 
![[Pasted image 20240724200855.png]]

# 1. Memory allocation type 
this is discussed earlier but its basically
1. Static Array [[static memory allocation]]
2. Dynamic Array[[Dynamic Memory Allocation]]

- Static array is basically an array where memory is allocated before hand, there are multiple(mostly) compiled language where memory is allocated before hand 
	- e.g int array[10] - 10 integer <u>*will be assigned in memory before running program *</u>

- Dynamic memory allocation is an array which shrinks and expands as need arises, a vector in C++ is an example of that.  python has dynamic memory allocation implemented for array itself
	- e.g. **vector `<`int`>` v**; <u></u> <u>this shrinks and expands</u>
	

**an intersting example is :**
int *arr = new int[5]; here the memory will be allocated at run time. now technically you can add more than 5 numbers but the behavior would be unpredictable and it would lead you to some garbage value 


# 2.  Dimension wise
stacking array gives you variety of arrays including 1-d which **row**, 2-d which is **matrix** and then 3-d array which can be **array of matrix**
e.g as below 
| ![[Pasted image 20240724202756.png]] 
![[Pasted image 20240724203254.png]]



# Advantages 
- can be used to implement other data type like [[stack]],[[ques]],[[trees]],[[graphs]]
- makes easy to access element based on index 
- better  [[cache locality]] 

# Disadvantages 
- memory not used to store elements is memory wasted 
- cant shrink and expand(again we can use vector to address this )
- its homogenus (so it can store just one type of data, again not in case of python)
- certain operation like like deletion and insertion is hard as we have to re-arrange elements, but we avoid this problem by implementing linked list

# Application of Array
- database is usually implemented as arrays
- look up tables are array 
- other ds heap, ques , vector , matrix can be made via array

# Operations and time complexity

1. Array Traversal
	 - the time complexity is O(n) because every element has to be visited once 
2. Insertion in Array
	 - inserting an element at given index requires you to re- do all the elemets
	 - e.g[1,2,3] and you want to add -1 at index 0 the [-1,1,2,3], you have to readjust all the elements
	 - time complexity is O(n)
	  
3. Deletion or find an element
	  - just like insertion we have to re- arrange all the elements and hence we have time- complexity O(n)
	  - same goes for finding an element as well 


  # [[Time Complexity]] and [[space complexity]]

### Time Complexity:

| Operation         | Best Case        | Average Case | Worst Case |
| ----------------- | ---------------- | ------------ | ---------- |
| ****Traversal**** | Ω(N)             | θ(N)         | O(N)       |
| ****Insertion**** | Ω(1)(last ele)   | θ(N)         | O(N)       |
| ****Deletion****  | Ω(1)(last ele)   | θ(N)         | O(N)       |
| ****Searching**** | Ω(1) (first ele) | θ(N)         | O(N)       |

### Space Complexity:

| Operation         | Best Case                  | Average Case | Worst Case |
| ----------------- | -------------------------- | ------------ | ---------- |
| ****Traversal**** | Ω(1)                       | θ(1)         | O(1)       |
| ****Insertion**** | Ω(1)                       | θ(N)         | O(N)       |
| ****Deletion****  | Ω(1)                       | θ(N)         | O(N)       |
| ****Searching**** | Ω(1) - not storing element | θ(1)         | O(1)       |
  