- when implementing selection sort we basically swap the elements.
- but in doing so we might swap the occurance of equal elements index a good example is below 
- I**nput : 4A 5 3 2 4B 1**
	**Output : 1 2 3 4B 4A 5**
- since the first 4 will be swapped at the end we have lost order

By definition stable sorting algorithm would preserve the ***occurance key*** if elements

- The way selection sort achieve this is by swapping elements to the nearby elements , more like adjusting it to adjacent side.

An example of that could be as below:
		**4A 5 3 2 4B 1**
         First minimum element is 1, now instead
         of swapping. Insert 1 in its correct place 
         and pushing every element one step forward
         i.e forward pushing.
         **1 4A 5 3 2 4B**
         Next minimum is 2 :
         **1 2 4A 5 3 4B**
         Next minimum is 3 :
         **1 2 3 4A 5 4B**
         Repeat the steps until array is sorted.
         **1 2 3 4A 4B 5**

It has same time complexity - O(n^2) since we are using 2 for loops and constant space complexity because we are using no extra space.

**The second for loop we use should be used to adjust elements on the sideways**
Implementation of this algorithm looks like: [solution]()


**Important Note:**
first for loop used to compare the element

second for loop to move elements on the right side

we only wants to move elements b/w where we found min element and where we are currently in sorted array

  

For example:

- [1,2,x,4,3,y,6] - once you at 1 after sorting and , y is where you found min next step should do

[1,2,y,x,4,3,6] - so arr[min_index-1] should go to arr[min_index] and do that until min_index reach to i