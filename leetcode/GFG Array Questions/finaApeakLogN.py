"""
Find a peak solution but implement on O(logn) time.


THOUGHT PROCESS AND ALGORITHM:

 - set left pointer to 0 , right pointer to n-1 (end of arr)
 - until left crosees r 
        - calculate mid
            - if arr[left] > arr[mid]  
                - move right -> mid - 1
            - if arr[right] > arr[mid]
                - move left -> mid + 1
                ** the reason this works is because we know no two adjacent elements are same , so it has to be increasing or decreaseing somewhere
            - if none of this true
                ** do this because it seems sticking to mid gives higher chance to get peak
                - move right -> right -1
                        left -> left + 1             

 - edge cases
    n = 1, return 0 
    n =2, should take care of itseld    

"""

class FindAPeak():
    def findAPeak(self,arr):
        n = len(arr)

        # these are edge cases
        if n == 1:
            return 0
        
        left = 0 
        right = n-1
        while(left<=right):
            mid = (left+right) // 2
            if arr[right] > arr[mid]:
                left = mid + 1
            elif(arr[left] > arr[mid]):
                right = mid - 1
            else:
                left += 1
                right -= 1        
        
        return mid
    
    def findAPeakRecursive(self,arr,left,right):
        n = len(arr)
        if n==1:
            return 0 

        if n ==2:
            if arr[0] > arr[1]:
                return 0
            else:
                return 1  

        mid = (left + right) // 2
        if left >= right:
            return mid
        if arr[left] > arr[mid]:
            return self.findAPeakRecursive(arr,left,mid-1)
        if arr[right] > arr[mid]:
            return self.findAPeakRecursive(arr,mid+1,right) 




soln = FindAPeak()
print('the index at peak found  with iterative binary search is : ',soln.findAPeak([4,2,3,2]))               
print("the solution index returned by recurive solution :", soln.findAPeakRecursive([6,3,2],0,2))

