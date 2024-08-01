"""
Given a binary array nums, return the maximum number of consecutive 1's in the array.

 

Example 1:

Input: nums = [1,1,0,1,1,1]
Output: 3
Explanation: The first two digits or the last three digits are consecutive 1s. The maximum number of consecutive 1s is 3.
Example 2:

Input: nums = [1,0,1,1,0,1]
Output: 2

Link - https://leetcode.com/problems/max-consecutive-ones/
"""

def MaxonsecutiveOne(arr):
    n = len(arr)

    maxCounter = 0 
    currentCounter = 0 
    for i in range(n):
        if arr[i] == 1:
            currentCounter += 1
        if currentCounter > maxCounter:
            maxCounter = currentCounter
        if arr[i] != 1:
            currentCounter = 0                
    return maxCounter       


print(MaxonsecutiveOne([1,0,1,1,1]))
