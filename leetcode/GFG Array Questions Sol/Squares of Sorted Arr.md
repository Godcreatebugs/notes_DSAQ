#squares_of_sorted_arr
#no977
GFG Link - https://www.geeksforgeeks.org/sort-array-converting-elements-squares/
Leetcode Link - https://leetcode.com/problems/squares-of-a-sorted-array/
## Question
- Given sorted arr return return sorted arr with squared elements
- e.g [-4,-1.0,3,10] should return [16,1,0,9,100]

## Thoughts and explanation
- Naive Approach - square all the elements and sort them afterwards 
	- Time complexity O(nlogn) - to sort and space complexity O(n) (depending on implementation)
	- **a good point is I was considering space complexity to be O(1) when sorting was done**
	- Implementation [solution](squaresSortedArray.py)

- better approach would be:
	- make new arr with all zeros same size as original arr
	- Make left pointer at 0 and right pointer at n-1
	- compare absolute values of left and right.
		- if left > right , put square of left at the end of result  arr
			- move left to left + 1
		- if right > left , put square of right at the arr[n-i] place, where i is counter (this should not go beyond n)
			- move right to right - 1
	- return this new arr when left > right	
	- edge case is n == 1, no left and right would be found and hence we would just return squared of one element 
- Time complexity would be O(n) - we are doing in one loop 
- Space complexity wold be O(n) - storing it as a new arr
- Implementation [solution](squaresSortedArray.py)
			