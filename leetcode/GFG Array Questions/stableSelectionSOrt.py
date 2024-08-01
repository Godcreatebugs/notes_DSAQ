"""
Implement the stable selection sort algorithm.
Time complexity is O(n^2) and space complexity is O(1)

    - stable selection sort should preserve the order in which this elements do occur 
GFG Link - https://www.geeksforgeeks.org/stable-selection-sort/

"""

class StableSelectionSortClass():
    def stableSelectionSort(self,arr):
        n = len(arr)
        """
        first for loop used to compare the element 
        second for loop to move elements on the right side
        we only wants to move elements b/w where we found min element and where we are currently in sorted array

        For example:
         - [1,2,x,4,3,y,6] - once you at 1 after sorting and , y is where you found min next step should do 
            [1,2,y,x,4,3,6] - so arr[min_index-1] should go to arr[min_index] and do that until min_index reach to i  
        """
        
        for i in range(n):
            currentIx = i 
            currentMin = float('inf')
            minIx = 0
            # find minimum ele

            for j in range(i,n):
                if arr[j] < currentMin:
                    currentMin = arr[j]
                    minIx  = j 

            #now shift element b/w i and minIx
            """
            Just a note: this will wipe out the next ele, arr[k+1] shifted would be same 
            e.g [1,2,3] - with this approach would be [1,1,1]
            for k in range(i,minIx-1):
                arr[k+1] = arr[k] 
                [1,2,x,5,4,y,16]       y = 5(min_index) and x at 2 and we are swapping until 
            """
            while(minIx > i):
                arr[minIx] = arr[minIx-1]
                minIx -= 1
            #assigned min element to current index
            arr[i] = currentMin    
        
        return arr
    
    def printArr(self,arr):
        n = len(arr)
        for ele in arr:
            print(ele, end =' ')
        #print new line 
        print()    
    
soln =  StableSelectionSortClass()
arr = [4, 5 ,3 ,2 ,4 ,1]
soln.printArr(arr)
soln.stableSelectionSort(arr)
soln.printArr(arr)
