Question: 
Given a sorted arr find how many times a given key was repeated
so [1,2,3,4, 4] key =4 should return 2

# linear search
- you could have made a dictionary to store occurence like 1:1, 2:1 ...4:2 and then traverse it to find value of key 4
- The other way is to simply make counter and do linear search
	- once you hit the key increase counter by 1 and return counter at the end 
- The solution is [solution](findOccurence.py)
- 