#binarysearch [explanation](https://www.geeksforgeeks.org/binary-search/) [implementation](binarySearch.py)[recursive_sol](binarySearchRecursive.py)


# What is binary search?
- Binary search is a affective algorithm to find a a given key in sorted array.
- Time complexity is O(log n) - the base is usually 2, constant space complexity
- faster than linear search

**To apply  binary search** 
- data has to be sorted 
- elements has to be stored in continuous manner(wont work on linkedlist)
- the elements has to be compare, apples to apples 

# How does binary search work??
- Always take the middle element of a list. 
- compare that ele to key we want to find.
	- if key is found - terminate the program
	- if not than compare it with key. 
		- if key is less than middle element now just repeat the process taking middle element as last pointer, first ele as first pointer on the left half of the array
		- if key is greater than middle element then, take first pointer to middle element, last pointer to end of array and repeat the process again
- Do this process until you found the element
## visual explanation 

![[Pasted image 20240725201914.png]]

You can do this either
- Recursively[example](binarySearchRecursive.py)
- Iteratively[example](binarySearch.py)

Again time complexity is O(log n) and space complexity is O(1) since we dont store anything

# Advantages of Binary Search
- faster than linear search
- more efficient to search cloud or hard drive

# Disadvantages of Binary Search
- works only on sorted array
- Data has to be stored continues location(e,g wont work on *<u>linkedlist*</u>)
- data has to be comparable, apples to apples, wont work on heterogeneous array

# Applications
- building block for complex algorithm to find weights
- well -sited for searching large database


