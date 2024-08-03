Leetcode lInk - https://leetcode.com/problems/find-numbers-with-even-number-of-digits/description/

#evennodigits
#no1295
# Explanation
- Given an array find no of elements which has even number of digits

# Approaches and Thoughts
- we have to iterate all the elements , since its not sorted(Not that it matters)
- And we can make counter variable so 
	- Time complexity to shoot for is O(n) and space complexity to shoot for is O(1)

- we need to divide every element by 10 until remainder is 0 
	- if the number of division we did on this one element is odd to reach there then number has odd no of digits 
	- if the number of divisions we did to reach at 0 - is even than it has even number of digits
		- we keep a counter where we increase that number by 1 

- Time complexity , since the highest number can go is 10^5 - considering all elements this we do this operation at max 5*n where n is number of element
- Hence time complexity will be basically O(n) and space complexity will be O(1)

	Link - https://leetcode.com/problems/find-numbers-with-even-number-of-digits/solutions/5582689/easy-python-solution/ 
- Implementation [solution](evenNoDigitts.py)
	

	