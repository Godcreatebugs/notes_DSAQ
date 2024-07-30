"""
Link GFG- https://www.geeksforgeeks.org/program-to-reverse-an-array/
Link Leetcode - https://leetcode.com/problems/reverse-string/ (Easy)

1. reverse array of given elements 
    {1,2,3} -> {3,2,1}

Thoughts and Approaches
1. make a new array and add n-i th element to new arr -> time complexity O(n) and space complexity is O(n)    
2. make temp variable and swap elements. 
    - if given [a,b,c]
        - temp = a, c->a, temp-> c
        - do this n/2 times 
        ** time complexity is O(n) space complexity is O(1) - doing in place substituion

3. use stack
    - make stack, pop each element from array and add to stack, TC - O(n), SC - O(n)        
"""

class ReverseArr:
    def reverseArrayExtraSpace(self,arr):
        res_arr = []
        n = len(arr)
        # for loop syntax where start is n-1 , -1 because we want to go till o and -1 is step size
        #for i in range(n-1,-1,-1):
        for i in range(n):
            res_arr.append(arr[n-1-i])
        return res_arr
    
    def reverseArrayInPlace(self,arr):
        n = len(arr)
        temp = None
        for i in range(n//2):
            temp = arr[i]
            arr[i] = arr[n-1-i]
            arr[n-1-i] = temp 
        return arr 

    def reverseArrStack(self,arr):
        stack = []

        for ele in arr:
            stack.append(ele)
        
        for i in range(len(arr)):
            arr[i] = stack.pop()

        return arr

    #reverse a string
    def reverseString(self,s: str):
        n = len(s)
        arr_str = list(s)
        res_arr =[]
        temp = None
        for i in range(n):
            res_arr.append(arr_str.pop())
           

        return ''.join(res_arr)    
        



               

        


sol = ReverseArr()
print('the reversed array with extra space is : ' , sol.reverseArrayExtraSpace([1,2,3]))        
print('in plcae subsitution looks like: ',sol.reverseArrayInPlace([1,2,3,4]))
print('reverse result using stack pop for array is: ',sol.reverseArrStack([1,2,3]))
print("The result after the split for a given string is: ", sol.reverseString('piyush'))