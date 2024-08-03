"""
Leetcode Link -  https://leetcode.com/problems/find-numbers-with-even-number-of-digits/description/

Basically return the number of digits that has even number of digits.
so, 
[12,345,2,6,7896]
should return 2 

Time complexity - Since at max we can divide by 5 times for each element at worse it can be 5* O(n) == O(n)
Space Complexity is O(1) - No extra space required
"""

def evenNoDigits(arr):
    n = len(arr)
    evenDigits = 0 
    for ele in arr:
        currentEle = ele
        noDivisions = 0
        while(currentEle != 0):
            currentEle = currentEle // 10
            noDivisions += 1
        if noDivisions % 2 ==0:
            evenDigits += 1

    return evenDigits

print(evenNoDigits([1,100,11,1234,1111]))            