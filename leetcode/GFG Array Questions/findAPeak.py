"""
Given an 0-indexed array of integers arr[] of size n, find its peak element and return it's index. An element is considered to be peak if it's value is greater than or equal to the values of its adjacent elements (if they exist).

Note: The output will be 1 if the index returned by your function is correct; otherwise, it will be 0.

Examples :

Input: n = 3, arr[] = {1, 2, 3} 
Output: 1
Explanation: If the index returned is 2, then the output printed will be 1. Since arr[2] = 3 is greater than its adjacent elements, and there is no element after it, we can consider it as a peak element. No other index satisfies the same property, so answer will be printed as 0.
Input: n = 7, arr[] = {1, 1, 1, 2, 1, 1, 1}
Output: 1
Explanation: In this case there are 5 peak elements with indices as {0,1,3,5,6}. Returning any of them will give you correct answer.
Your Task:
You don't have to read input or print anything. Complete the function peakElement() which takes the array arr[] and its size n as input parameters and returns the index of the peak element.

Expected Time Complexity: O( log(n) ).
Expected Auxiliary Space: O(1)

Constraints:
1 ≤ n ≤ 105
1 ≤ arr[i] ≤ 106

Expectations:
O(log(n)) - time complexity - I dont know how we will reach here tho
O(1) - space complexity
"""

"""
Understanding of question 
{1,1,,1,2,1,1,1} - peak index is where the value at that index is higher than or equals to adjacent elements

so here first 1 adjustnt is just 1 so just like that you will get 
[0,1,3,5,6] and returning any of this will give you right answer

Approach 1: 
    
    - make a variable pivotIndex and start with 0 , check the edge case where there is only 1 element then return 0 else move on 
    - make an iterator which update pivorIndex by going over loop
     - if its not first and last element 
        - check ele on both the sides and check if its greater or equals to ele then return pivotIndex
    -if pivotIndex is 0 and n > 1 then compare it to next ele
    - if pivotIndex is n-1 then compared to n-2 ele 

    if anywwhere the conditions are matched just break the function and return the pivotIndex    

    
EDGE CASES:
    what if array has only 1 element - does that mean it is the peak. - seems to be yes, so return only that element    

THOUGHTS on QUESTIONS:
        will there always be a a peak element.
        you know I think it is. because in integer array you can be always ascending in that case last element is peak, first element in just descending and 
        otherwise you will find peak in b/w. so there always will be one peak hence no else condition at all      
            """

class Solution:
    """
    first approach has passed all the solution.
    Time complexity is O(n) - since iteration happens all the elements
    Space complexity iis O(1) - no xtra space was used 
    """
    def peakElement1(self,arr,n):
        pivotIndex = 0 
        #if there is one element
        if n == 1:
            return 0 
        
        #if there are 2 element
        if n == 2:
            return 1 if arr[1] >= arr[0] else 0 
            
        # iterating over while pivot is less than n 
        while(pivotIndex < n):
            #if iterator is at beginning or end
            if (pivotIndex == 0 and arr[0] >= arr[1]) or (pivotIndex == n -1 and arr[n-1] >= arr[n-2]):
                return pivotIndex
            
            #if the elements are in the middle 
            if (pivotIndex > 0 and pivotIndex < n-1):
                if arr[pivotIndex] >= arr[pivotIndex-1] and arr[pivotIndex] >= arr[pivotIndex+1]:
                    return pivotIndex
            
            pivotIndex += 1

    def peakElementFor(self,arr,n):
        #if there is only one element 
        if n == 1:
            return 0 
        
        if arr[0] >= arr[1]:
            return 0
        elif arr[n-1] >= arr[n-2]:
            return n-1


        for i in range(1,n-1):
            if (arr[i] >= arr[i-1]) and (arr[i] > arr[i+1]):
                return i 
            



question_arr = Solution()
print("the answer is : ", question_arr.peakElement1([1,2],2))
print("the answer with for loop is : ", question_arr.peakElement1([1,1,1],3))


