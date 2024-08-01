#sortarr
#selectionsort
Link - https://www.geeksforgeeks.org/selection-sort-algorithm-2/
- It is one of the easiet algorithm to implement
- works based on selecting a minimum element from unsorted part of array and adding it to sorted portion.


# Algorithm
- consider an iterator that streches to n where n i == len(arr)
- with every pass perform:
	- Find minimum element and swap position with where current iterator is so for eg
	- [3,2,1,4] -> with first iteration do [1,2,4,3]
- Do this for all elements 
- At end you have sorted arr

# complexities
- Time complexity would be O(n^2) because for each element we iterate n times hence 2 for/while loop
- Space complexity - since we are doing in place substitution space complexity is O(1)

Examples:
Here swap 64 and 11
![[Pasted image 20240731183320.png]]
For second pass:
![[Pasted image 20240731183356.png]]
Repeating this process over and over again gives us:
![[Pasted image 20240731183432.png]]

**My implementation example [example](selectionSort.py)**

# Advantages
- easy to implement 
- works well with small datasets

# Disadavantages
- due to bad time complexity it dont work well with large datasets
-  Does not preserve the relative order of items with equal keys which means it is not stable.

<u>To avoid this stability issue we can use </u>[[Stable Selection Sort]]

#stabledelectionsort