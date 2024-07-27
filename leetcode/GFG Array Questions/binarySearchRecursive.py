"""
Implement efficient binary search using recursive solution.

[1,2,3,4,6] target 4 

terminate condition if target is found

condition is if we have found mid 

"""

class BinaryRecursiveSearch():
    
    def binaryRecursiveSearch(self,arr,lo, hi,target):
        
        if target < arr[lo] or target> arr[hi]:
            return -1
        mid = (hi+lo) // 2    
        if (lo<=hi):
            if arr[mid] == target:
                return mid
            elif arr[mid] > target:
                return self.binaryRecursiveSearch(arr,lo,mid-1,target)
            else:
                return self.binaryRecursiveSearch(arr,mid+1,hi,target)
        else:
            return -1 
            


soln = BinaryRecursiveSearch()
print('recursive soln to find target 4 , the index is : ', soln.binaryRecursiveSearch([1,2,3,4,5],0,4,6))
        

        