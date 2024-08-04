"""
Leetcode Link - https://leetcode.com/problems/merge-sorted-array/description/


"""

class MergeSortedArr:
    def mergeSortedArrNaive(self,arr1,arr2,m,n):
        # subsitute last n element of arr1 with arr2 elements
        for i in range(n):
            arr1[m+i] = arr2[i]

        #return sorted arr
        return sorted(arr1)    

    def mergeSortedArr(self,arr1,arr2,m,n):
        
        #handle edge cases - m+n >= 1 so, in that case m or n has to be 1 and other one can be zero
        # looks like A = [0] , B = [1]
        if (m==0 and n==1):
            arr1[0] = arr2[0]
            return
        #looks like A= [2], B =[]-> return A 
        if (m==1 and n==0):
            return
        
        #if m = 1 and n = 1 A=[1,0] B =[2] 
        
        # do back substituion
        #also once q or p reached to zero dump all the elements of remaining B into A 
        # [4,5,6,0,0,0] , [1,2,3]
        p = m-1
        q = n-1
        # we just have to consider q pointer because if 1 reaches to zero p will still saty sorted 
        pCurr = m +n -1
        while (q >=0):
           #compare the element and if A and B has same element move q pointer
           if(arr2[q] >= arr1[p]):
               arr1[pCurr] = arr2[q]
               q -= 1
               pCurr -= 1
           else:
               """
               The other way could have beeb assiging p to -ve infinity and hence you will always find bigger element in arr2
                if p < 0:
                   arr1[p] = float('-inf')
                   continue    
                   but it will create issue for A= [2,0], B=[1] because it will do [2,2] for second iteration you will subsitute 0th element
               """
               if p<0:
                   while(q >= 0):
                       arr1[pCurr] = arr2[q]
                       q -= 1
                       pCurr -= 1
                   break
               
                           
               arr1[pCurr] = arr1[p]
               p -= 1
               pCurr -=1  
        return arr1      


    
    #print arr 
    def printArr(self,arr):
        for i in range(len(arr)):
            print(arr[i], end =', ')
        print()


soln = MergeSortedArr()
soln.printArr(soln.mergeSortedArrNaive([1,2,3,0,0,0],[2,5,6],3,3))
soln.printArr(soln.mergeSortedArr([2,0],[1],1,1))

