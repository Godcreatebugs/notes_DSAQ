"""
Return how many times a key was repeated

[1,1,2,2,3,3,4]
    - make left = 0 and right = n-1 
    - find middle 
        - if middle is greater than key
            - move right to mid - 1
        -if middle is greater than key
            - move left to mid + 1
        - if mid == key
            - make counter += 1
            - make left += 1 and right -= 1         
"""

class FindOccurance():
    def findOccurenceLinear(self,arr,key):
        counter = 0 
        n = len(arr)
        for ele in arr:
            if ele == key:
                counter += 1
        return counter
    
    def findOccurBinary(self,arr,key):

    
    def printRes(self,arr,key):
        print('the key is repeated : ', self.findOccurenceLinear(arr,key))

soln = FindOccurance()
soln.printRes([1,2,3,4,4,4],4)