# Strings, Sorting Algorithms

## Free Response Questions

### Strings

1. What is a string? How is a string created in memory?
A. A string or sequence of characters. A string is a core data type in most languages. I believe a string has to be UTF8. That probably doesn't include every language.
String is created in memory as an array of characters.

2. How can we calculate the frequencies of each character in a string?
A. Make an array/list to cover all the unicode characters. Each value will represent that character's unicode code

3. What is an anagram? How can we check if 2 strings are an anagram?
A. An anagram is a string of characters that when rearranged is the same as another string of characters. Check the frequency of characters. They should be the same. Sort the characters. They should be equal.

4. What are 2 ways to determine if a string is a palindrome?
A. The string and a reverse of it should be equal.
Have pointers at head going forward and at tail going backward. Both one character at a time. The characters should be the same at each interval.

5. What is the runtime to concatenate a string with a character?
A. O(n). Strings are immutable. A copy of the string has to be made, aka `n` length before the character is added to the string

6. What is the difference between substring vs. subsequence? 
A. Substring is a sequence of consqecutive characters in a string. A subsequence is a sequence of characters that don't have to be consecutive

7. Let s = 'coachable rocks'​. Can you give an example of a subsequence of s that is not a substring s? What about a substring that is not a subsequence?
A. A subsequence that is not a substring is che. All substrings are subsequences


### Sorting

1. What does it mean to sort an array? 
A. Having all the elements in some ascending or descending order based on some comparison.


2. How does sorting work for strings? 
A. Check the `ord` or unicode value of each character. Arrange these in ascending or descending numerical order.


3. What do you need to do if you are sorting objects? How is it different from strings, integers, etc?
A. Objects aren't inherently greater or less than any other objects. A comparison has to be coded to determine what logic should be used for object. Objects are about abstraction so they will include different data types. While integers, floats, strings, bool all are compared based on their values. Objects don't have one value.


4. Describe how selection sort works and its runtime and space complexity
A. Selection sort compares each value starting from the head with the rest of the remaining elements to the right to find the smallest value and swap it to its place at the front. The same process is repeated for each value to the right and only checking for lowest value with remaining values to the right.
Runtime: O(n^2). Nested loops going through the entire length
Space: O(1)


5. Describe how insertion sort works and its runtime and space complexity
A. 
Runtime: O(n^2). 
Space: O(1)


6. Describe how merge sort works and its runtime and space complexity
A. 
Runtime: O(n^2). 
Space: O(1)


7. Describe how quick sort works and its runtime and space complexity
A. 
Runtime: O(n^2). 
Space: O(1)


8. Suppose we have applied quicksort to a list, and we have [1,0,2,3,5,4] as an intermediate stage. Which elements could have been the pivot element in a previous iteration?
A. I'm not sure I understand this. 2 or 3?


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
(a) Selection sort -- 5 outer loops in. the array 0,2,3,4, 5 contains the smallest elements of the array in order - they are in the final positions for the sorted array. The other elements are primarily untouched, except for those that had 0,2,3,4,5 in their original positions.
(b) Quick sort -- 7 is the partition. 6 numbers 2,0,4,6,5,3 are smaller than 7. 8 numbers 15,27,17,10,16,8,24,18 are greater
(c) Insertion sort -- 12 outer loops in. All but last four items -- 4,6,18,5 have been sorted
(d) Merge sort -- More than half way done. There's four 4 item sorted sequences within the 16 items. 2 more sorts are left. Merge into 2 sorted sequences then one final sort.