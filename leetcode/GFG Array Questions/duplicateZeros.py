"""
Double the zeroes when found:
Input: arr = [1,0,2,3,0,4,5,0]
Output: [1,0,0,2,3,0,0,4]

- Do in place substituion
"""

class DuplicateZeroes:
    def printArr(self,arr):
        n = len(arr)
        for i in range(n):
            print(arr[i],' , ')
        print()

    def duplicateZeroesNaive(self,arr):
        n = len(arr)
        res = [0] * n
        ix = 0 # counter for res
        i = 0 #counter for arr     
        while(ix < n):
            if arr[i] == 0:
                ix += 2
                i += 1
            else:
                res[ix] = arr[i]
                ix += 1
                i += 1            

        #do in place substituion
        for i in range(n):
            arr[i] = res[i]
        print(arr)
        return arr
    
    def duplicatZeroesInPlace(self, arr):
        n = len(arr)
        #count zeroes
        countZeros = sum(1 for num in arr if num ==0) 
        

        #back substition 

        pfrom = n - 1 #from where ele should taken to copy
        pto = n + countZeros -1 #where we should copy ele
        
        while(pfrom >=0):
            #do subsitution only if pto is in range of n-1
            if pto < n:
                arr[pto] = arr[pfrom]
                #if the ele is 0 do subsitution twice
                if arr[pfrom] == 0:
                    pto -= 1
                    if pto < n:
                        arr[pto] = 0

            pto -= 1
            pfrom -= 1             

        print(arr)
        return arr             

    def duplicateZeroesNew(self,arr):
        n = len(arr)

        # add zeroes at the end of arr
        countZero = sum(1 for ele in arr if ele==0)

        for i in range(countZero):
            arr.append(0)

        #start back subsitution
        pfrom = n - 1
        pto = n + countZero -1 

        while(pfrom >=0):
            if arr[pfrom] != 0:
                #if element is not zero do regular element swap
                arr[pto] = arr[pfrom]
                #decrease both by one 
                pto -= 1
                pfrom -= 1
            else:
                arr[pto] = 0
                arr[pto-1] = 0 
                pfrom -=1
                pto -= 2
        print(arr[:n])
        return arr[:n]
                


soln = DuplicateZeroes()
# soln.duplicateZeroesNaive([1,0,2,3,0,4,5,0]) 
# soln.duplicatZeroesInPlace([8,4,5,0,0,0,0])   
soln.duplicateZeroesNew([1,0,0,7]) 



