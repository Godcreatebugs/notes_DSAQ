"""
Link - https://leetcode.com/problems/squares-of-a-sorted-array/
No -977
GFG Link - https://www.geeksforgeeks.org/sort-array-converting-elements-squares/
Naive approach TC - O(nlogn) and SC - O(1)

[-4,-1,0,3,10]
"""

def squaresSortedArrNaive(arr):
    # square all the elements
    n = len(arr)
    for i  in range(n):
        arr[i] = arr[i]**2
        print(arr[i],' ')
    
    return sorted(arr) 


def squareSortedArr(arr):
    n = len(arr)
    if n ==1:
        return [arr[0] ** 2]
    res = [0] * n

    left = 0 
    right = n - 1
    i = 0 # counter to add elements at the end of res arr
    while(left <= right ):
        # if absoluet value of left > right
        if abs(arr[left]) >= abs(arr[right]):
            res[n-1-i] = arr[left] ** 2
            left += 1
            i += 1

        #if absolute value of right is greater than
        else:
             res[n-1-i] = arr[right] ** 2
             right -= 1
             i += 1     

    #return an arr
    return res    


print('the sorted arr of [-3,2,-1] would be : ',squaresSortedArrNaive([-3,2,-1]))
print('the sorted arr of [-3,2,-1] would be : ',squareSortedArr([-3,2,-1]))
print('the sorted arr of [1] would be : ',squareSortedArr([2]))