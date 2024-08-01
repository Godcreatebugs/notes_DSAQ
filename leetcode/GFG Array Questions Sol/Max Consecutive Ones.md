leetcode link - https://leetcode.com/problems/max-consecutive-ones/description/

Question:
if given arr of zeros and ones find maximum time consecutively ones are repeated
[1,0,1,1] - should give you 2 as answer

#maxconsecutiveones
#no485

# thoughts:
- cant do binary search, as array is not sorted neither we can sort it 
- you have to do linear scan and that will result in O(n) - at least
- make 2 counters max_occur and current_occur
- check next element if its one increase counter by 1 
	- if not then reset the current counter to 0 
	- also check if current_counter > max_counter than update max_counter
- return max_counter


Time complexity - O(n)
space complexity O(1)

Implemented solution [solution](maxconsicutiveOnes.py)