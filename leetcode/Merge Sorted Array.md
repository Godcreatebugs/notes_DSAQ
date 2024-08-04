Leetcode link - https://leetcode.com/problems/merge-sorted-array/description/
#mergesortedarr
#no88

# Question Explanation
Given 2 arr where one arr has m+n len and second has n len , both of them are sorted,
merge them and return sorted arr
- Do in place substitution and hence arr has m+n len and n zeroes are attached to it 

e.g **Input:** nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
    **Output:** [1,2,2,3,5,6]

# Approach
- 1. Naive approach would be to replace last n elements of arr with Array B and sort the array
- Time complexity in that case would be O(m+n * log(m+n)) - depending on sorting algo
- No extra space is used so O(1) space complexity
- Implementation - [solution](mergeSortedArr.py)

2. **A better approach**
- In this approach make two pointers i , j and compare element each time , 
- if arr[i] > arr[j] then place i there and move i forward and same with j as well
- do this process (m+n) times to reach to results
- We can do this process in reverse as well , where we can put a bigger element at the end 
- If i is exhausted then just adjoin the whole remaining arr2 and viceversa
- **Doing in reverse helps with in place substitution**
- Very important factor is its edge cases

Time complexity (O(m+n)) - since we are iterating m+n times
Space Complexity O(1) - since no extra space was used here