#duplicatezeros
Leetcode link- https://leetcode.com/problems/duplicate-zeros/description/

## Question statement
Given an array with size n when 0 occurs double the 0's and return array with same size where order of elements should remain the same 

example :
**Input:** arr = [1,0,2,3,0,4,5,0]
**Output:** [1,0,0,2,3,0,0,4]

## Approaches:
Naive Approach:
- One approach I can think of is basically create res arr with same size as current arr.
- Loop through original array
	- if element is non zero add that element to the res
	- if its zero then add 2 zeros and jump twice
- Time complexity in this case would be O(n) and space complexity also O(n), becuase we iterate one time and use extra arr to store res
- The implementation [solution](duplicateZeros.py)

A better approach to avoid O(n) space complexity:

- We can know how many elements on the right will be eliminated by checking number of zeroes in arr. 
	- we can calculate this by traversing array and find number of zeroes
	- lets say we have 2 zeroes that means that last 2 elements of arr is something we can cut off 
- After that we can start doing this process: from n-p element where p is number of zeroes we have 
	-  we will start checking n -p element and:
		- if its non zero we will place it at n-1 position
		- if its zero we will place 2 zeroes on n-pth and move one pointer backward
	- repeat the process until we are at start of the arr

This way we are doing in place substitution and we end up with 
Time Complexity O(n) - because we are traversing once
Space COmplexity O(1) - becuase of in place substituion


Example:
[1,0,2,3,0,4,5,0] - the result here would be [1,0,0,2,3,0,0,4]
**this is edge case**
- if the last element is zero those wont be replicated twice because they are at end anyway and last element wont be replicated anyway 
	- e.g [1,2,0] would be [1,2,0] anyways

- so count zeroes until n-2 len 
- in this case it is 2 so last 2 elements will be deleted anyways 
	- the array of interest is [1,0,2,3,0,4]
- so 4 will be placed at n-1 position
- then 0 will be placed twice on n-2 and n-3 position
- then substitute n-4, n-5 to 2 and 3 respectively 
- again 0 do it twice
- and like that reach end of arr

A picture to represent this would be 
![[Pasted image 20240802004507.png]]


**The other Approach**
- I can add m zeroes at the end of an arr, where m is number of zeroes found
- now iterating over arr where pfrom >=0 condition:
	- move pfrom to pto if arr[pfrom ] is not zero
		- decrease pfrom and pto both to -1
	- if its zero:
		- do arr[pto] and arr[pto] = 0 
		- decrease pto by 2 
		- decrease pfrom to 1 

- at the end return arr[:n] - we have done in place modification - This approach actually worked in the first shot.