"""
Implement binary search both recursively and iteratively 

[1,2,3,4]  and key 2 , mid is 2(element 3), rp = 3 and lp = 0,
    1. upon comparing 2 and mid(element 3) - chose left half of the array
    2. new lp = 0, rp = old_mid and find new mid and comapre it again

[1,2,3,4,5] and key 4 
        here lp = 0 , rp = n-1 and mid = 2(element 3)
    1.  compare mid and key and chosing the right half 
    2.  updating lp = mid , rp as it is and caculate mid again


    
    [0,1,2]  ->3

    - so one guard rail will be if element is out of bouds we will check that condition first 
    SO IF NUMBER OF ELEMENTS ARE EVEN TAKING ANY OF THE MID ELEMENT IS ACTUALLY FINE AND YOU DONT HAVE TO DO HOOPS LIKE HERE TO FIND MID    
    """

class BinarySearch:
        def binarySearch(self,arr,target):
                n = len(arr)

                  
                lo = 0 
                hi = n - 1
                if target >arr[hi] or target <arr[lo]: 
                    return -1
                
                while(lo <= hi):
                    mid = (lo + hi) // 2

                    if arr[mid] == target:
                          return mid
                    elif (arr[mid]>target):
                          hi = mid - 1
                    else:
                          lo = mid + 1        

                return -1 

    


        #if left pointer has crossed right pointer then no match is found and return -1
 
    

soln = BinarySearch()
print("The index where target is found is  : ",soln.binarySearch([1,2,3,4],-1)) # the answer should be 2
