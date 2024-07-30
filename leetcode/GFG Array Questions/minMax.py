"""
Find Min and Max of an array.
Given an array arr. Your task is to find the minimum and maximum elements in the array.

Note: Return an array that contains two elements the first one will be a minimum element and the second will be a maximum of an array.

basically create 2 functions getMin and getMax and add the to array like [min,max]

Approaches:
    1. You can sort the array but that is O(nlogn) operation
    2. Do a linear scan, and keep track of min and max variable. TC -O(n), space complexity - O(1)
    ** easy question
    """

class Solution():
    def getMinMax(self,arr):
        n = len(arr)

        maxEle,minEle = float('-inf'),float('inf') # assigning max to -ve infinity and assigning positive infinity to minEle
        for ele in arr:
            if ele > maxEle:
                maxEle = ele
            if ele < minEle:
                minEle = ele 
        return [minEle,maxEle]



soln = Solution()
print("min and max ele in this array is: ",soln.getMinMax([1,2,4]))               