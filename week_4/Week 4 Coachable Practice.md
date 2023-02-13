# Strings, Sorting Algorithms

## Free Response Questions

### Strings

1. What is a string? How is a string created in memory?
A. 

2. How can we calculate the frequencies of each character in a string?
A. 

3. What is an anagram? How can we check if 2 strings are an anagram?
A. 

4. What are 2 ways to determine if a string is a palindrome?
A. 

5. What is the runtime to concatenate a string with a character?
A. 

6. What is the difference between substring vs. subsequence? 
A. 

7. Let s = 'coachable rocks'​. Can you give an example of a subsequence of s that is not a substring s? What about a substring that is not a subsequence?
A. 


### Sorting

1. What does it mean to sort an array? 
A. 


2. How does sorting work for strings? 
A. 


3. What do you need to do if you are sorting objects? How is it different from strings, integers, etc?
A. 


4. Describe how selection sort works and its runtime and space complexity
A. 


5. Describe how insertion sort works and its runtime and space complexity
A. 


6. Describe how merge sort works and its runtime and space complexity
A. 


7. Describe how quick sort works and its runtime and space complexity
A. 


8. Suppose we have applied quicksort to a list, and we have [1,0,2,3,5,4] as an intermediate stage. Which elements could have been the pivot element in a previous iteration?
A. 


9. What's different between quicksort and mergesort? What are the tradeoffs between the two?
A. 


10. What does divide and conquer mean? Which sorting algorithms use this approach?
A. 


11. What is the difference between 3-way quicksort and standard quicksort? 
A. 


12. Describe one specific input where you'd prefer to use 3-way quicksort over standard quicksort. Why is it faster here?
A. 


13. Suppose you have an array with only 5 distinct elements (only the numbers 1-5). 
A. 
A.  What is the worst-case runtime of quicksort? Why?
b. What is the worst-case runtime of 3-way quicksort? Why?

## Match Sorting Algorithms

Here is an array that we're trying to sort several different ways. We'll provide the intermediate sorting stage, and you'll need to determine which sorting algorithm was used. We'll give you the first one as an example.

For some of them, multiple algorithms might apply. List as many as you can. 

#### Initial and Sorted Input
(initial) [3, 8, 2, 15, 27, 21, 17, 10, 16, 7, 24, 0, 4, 6, 18, 5]
(sorted)  [0, 2, 3, 4, 5, 6, 7, 8, 10, 15, 16, 17, 18, 21, 24, 27]

#### Intermediate Stages To Identify
a) [0, 2, 3, 4, 5, 21, 17, 10, 16, 7, 24, 8, 27, 6, 18, 15]
b) [2, 0, 4, 6, 5, 3, 7, 15, 27, 21, 17, 10, 16, 8, 24, 18]
c) [0, 2, 3, 7, 8, 10, 15, 16, 17, 21, 24, 27, 4, 6, 18, 5]
d) [2, 3, 8, 15, 10, 17, 21, 27, 0, 7, 16, 24, 4, 5, 6, 18]

A. 
(a) is selection sort because the array  0,2,3,4, 5 contains the smallest elements of the array in order - they are in the final positions for the sorted array. The other elements are primarily untouched, except for those that had 0,2,3,4,5 in their original positions.
(b)
(c)
(d)