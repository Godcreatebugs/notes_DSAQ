"""
Implement selection sort algorithm 
GFG link - https://www.geeksforgeeks.org/selection-sort-algorithm-2/

Leetcode Link - https://leetcode.com/problems/sort-an-array/submissions/1340070533/

Its called selection sort because we select min every time we iterate over the array

"""

class SelectionSort:
    
    def selectionSort(self,arr):
        n = len(arr)

        for i in range(n):
            currIndex = i
            currentMin = float('inf')
            minIndex = 0
            for j in range(i,n):
                if arr[j] < currentMin:
                    currentMin = arr[j]
                    minIndex = j 

            #swap the elements
            arr[currIndex],arr[minIndex] = arr[minIndex], arr[currIndex]

        return arr

    def selectSortDesc(self,arr):
        n = len(arr)

        for i in range(n):
            currentIx = i 
            currentMax = float('-inf')
            maxIx = 0 

            for j in range(i,n):
                if arr[j] > currentMax:
                    currentMax = arr[j]
                    maxIx = j

            #swap the elemnts 
            arr[currentIx], arr[maxIx] = arr[maxIx], arr[currentIx] 

        return arr    
    


soln = SelectionSort()
print("the sorted version of [4,1,2,3] is : ",soln.selectionSort([4,3,2,3]))
print("the descending sort of arr [4,3,2,1] is :", soln.selectSortDesc([1,2,3,4]))