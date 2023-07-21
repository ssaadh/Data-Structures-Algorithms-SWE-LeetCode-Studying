Free Response Questions

Strings

1. a. What is a string?
A data structure of a sequence of unicode characters

b. How is a string created in memory?
Array of unicode characters



2. How can we calculate the frequencies of each character in a string?
We can add counters for each character into an array or dictionary.  If they are only alphabetical letters then the dictionary is size 26. We can loop through the string and this can be done in O(n) time. To place each character into an array, can convert the characters to an integer via Python's ord command.

Simple example without ord:
```
def freq(s):
  my_dict = dict()
  for c in s:
    if c in my_dict:
      my_dict[c] += 1
    else:
      my_dict[c] = 1
  return my_dict
```


3. What is an anagram? How can we check if 2 strings are an anagram?

Anagram is two strings that are able to be the same if rearranged.

Check if 2 strings are anagrams:
- they are the same when sorted
- they have the same frequency of characters



4. What are 2 ways to determine if a string is a palindrome?

Palindrome is same forward and backward
- Reversed string is same as string
- pointers at start and end of string. Iterate each one by one. Characters should be equal at each iteration.



5. What is the runtime to concatenate a string with a character?

O(n). Strings are immutable. A copy of the string with the character has to be made. When the new string is created,  the original string is added before the concatenation of the character is added.



6. What is the difference between substring vs. subsequence?

substring: a consecutive sequence of characters
subsequence: a sequence of characters that are not consecutive/back to back


7. Let s = 'coachable rocks'​. Can you give an example of a subsequence of s that is not a substring s? What about a substring that is not a subsequence?

subsequence: ces
All substrings are subsequences


8. How many possible substrings are there of a string of length N? 
(N * (N+1))/2

substrings for "hello": "h", "e", "l", "l", "o", | "he", "el", "ll", "lo", | "hel", "ell", "llo", | "hell", "ello", | "hello" (15 substrings in total).



9. How many possible subsequences are there of a string of length N?
2^N - 1
2^N: Every character has two options: to be in the subsequence or not be in the subsequence.
Remove 1 for the empty subsequence

(i dont totally understand how i'm supposed to be able to know 8 (maybe 9) on my own without having looked it up)


Sorting

1. What does it mean to sort an array? 
To place the array items in ascending or descending order based on some comparison between the items. Like things being sorted in alphabetical order


2. How does sorting work for strings? How is different than sorting arrays?
Sorting between whole strings can be done in different ways. Like looking at the initial individual characters or comparing whole strings in some way.
Sorting an array is like sorting a single string. A single string can be thought of as an array of characters. Sorting an array is like sorting the characters in a string.



3. What do you need to do if you are sorting objects? How is it different from strings, integers, etc?
There's no way to sort objects by default. Data types can be compared with equal, greater than, greater than or equal to, less than, less than and equal by default. So can objects but those methods need to be created. Objects are data structures containing data types (strings, integers/numerics, boolean).



--

in-place: no extra space required. input array is sorted without any extra data structures or memory.

4. Describe how selection sort works and its runtime and space complexity. 
Is this a stable sorting algorithm? Explain why or why not.

Iterates through the array of length N finding the smallest value. It swaps that value with a swap index. swap index starts at the beginning of the array and increments by 1 after each swap. So N iterations and each iteration goes through the array, which is N length.

runtime: O(N^2)
space: O(1), in-place

Not stable because, during the swapping step, no consideration for relative ordering of elements. Swaps happen even if elements are the same value.



5. Describe how insertion sort works and its runtime and space complexity.
Is this a stable sorting algorithm? Explain why or why not.

Elements are inserted amongst already sorted elements. Sorted elements bigger than the current element get moved one to the right to make space for where the current element is inserted.

runtime: O(N^2). avg and worst case. The algo goes through all N array elements and each time it takes up to N swaps to get that current element sorted.
The worst run time happens when the array is sorted backwards with the highest value elements being first. This creates the most amount of swaps. Best case, the array is already sorted. O(N) run time since no or minimal swaps are needed.

space: O(1), in-place.

Stable: when two equal elements come up, the algo keeps the first one in its original place and inserts the second one after it. The algo does not move elements past other equal elements. Original relative order is preserved.



6.Describe how merge sort works and its runtime and space complexity.
Is this a stable sorting algorithm? Explain why or why not.

Divide and conquer algo. Divide array items up as much as possible normally down to a size of 1 element. Conquer by merging halves back together as sorted.
During merging, the algo repeatedly takes the smallest element from the front of one of two sorted subarrays. This continues until both subarrays are processed.

An odd array length will have one length 2 subarray.

The algo order is:
-- Find mid
-- Recursively divide into 2 halves
-- Sort and merge each half

Runtime: O(N log N).  The logarithmic log N comes from the recursive division of the array into halves. The number of levels is logarithmic with respect to the input size N. In each level, merging the divided subarrays takes linear O(N).

Space: O(N). A copy of the original unsorted array is needed in order to do sort the original array.

Stable: Elements that are equal have the left element be sorted first. Keeping relative order in place.


7. Describe how quick sort works and its runtime and space complexity.
Is this a stable sorting algorithm? Explain why or why not.

Divide and conquer algo. With a selected pivot element from the array, partition the other elements into two subarrays for less than or greater than the pivot. The two sides recursively have the pivot and partition step done until there are no more elements that have not been the pivot at any point.
There isn't a conquer step since the algo does everything in place.
Runtime: on average O(n log n). The pivot chosen divides the array into nearly two equal halves (depends) so there are a logarithmic number of partitions. Each partition performs linear work (n), visiting each item once.
In the worst case, it is O(n^2) when the smallest or largest elements are always chosen as the pivot. One side will have all the elements which is the most swaps each time.
In-place algo.
Not stable algo: During partition, items that are equal to the pivot are moved to the right without staying in relative order with the pivot.



8. Suppose we have applied quicksort to a list, and we have [1,0,2,3,5,4] as an intermediate stage. Which elements could have been the pivot element in a previous iteration?

2 and 3 because everything to the left of each is smaller and greater to the right



9. What's different between quicksort and mergesort? What are the tradeoffs between the two?

Quicksort is in-place without extra space. Mergesort has space complexity of O(n) with a copy of the original unsorted array being made
Mergesort has a worst case of O(n log n) while that's only the average and best case for quicksort.
Quicksort's worst case runtime is O(n^2). When the smallest or largest element is the pivot every time.



10. What does divide and conquer mean? Which sorting algorithms use this approach?

Involves breaking down complex problems into smaller/smallest sub-problems, solving them, then combining the solutions together.

mergesort, quicksort, [binary] heap sort


11. What is the difference between 3-way quicksort and standard quicksort? 
3-way quicksort is good for duplicate values. 3-way quicksort partitions elements less than, equal to, and greater than the pivot.
While standard does not handle duplicates on its own ever. Duplicates lead to worse runtime. Standard is less than to one side and greater than or equal to the right.

3-way quicksort psuedocode:
```
def quicksort(arr):
  if len(arr) <= 1:
    return arr
  pivot = arr[len(arr) // 2]
  left = [x for x in arr if x < pivot]
  middle = [x for x in arr if x == pivot]
  right = [x for x in arr if x > pivot]
  return quicksort(left) + middle + quicksort(right)
```


12. Describe one specific input where you'd prefer to use 3-way quicksort over standard quicksort. Why is it faster here?
One specific input is when there are only a few values with lots of duplicates. For example:
[1, 3, 2, 2, 1, 3, 2, 2, 3, 2]
If 2 is picked as the pivot then it will be sorted after one partition:
[1, 1, 2, 2, 2, 2, 2, 3, 3, 3]



13. Suppose you have an array with only 5 distinct elements (only the numbers 1-5). Note the array is still of arbitrarily large size N so it could be [1,2,3,4,1,2,3,4,4,4,4,3,2,3,2,....] with many duplicates. For an array like this.
a. What is the worst-case runtime of quicksort? Why?
b. What is the worst-case runtime of 3-way quicksort? Why?

Worst case runtime for quicksort will be O(N^2). If the smallest or largest pivots are used each time. Duplicates are not accounted for and with only 5 distinct elements, 

For 3-way quicksort because there are only 5 distinct numbers, the worst case run time will be closer to O(N log N) as the number of swaps will go down a lot each time a partition sorts all the duplicate pivots in their correct position in the array.


3.  #### Quicksort (No Shuffle)

psuedocode
```
mid = partition(lo, hi)
LeftHalf(lo, mid-1)
RightHalf(mid+1, hi)

partition(lo,hi)
  pivot = a[lo]
  swap = lo+1

  loop i++ in range(lo+1, hi+1):
    (a[i] < pivot): exchange a[i] with a[swap]; increment swap
  swap a[lo], a[swap-1]
  return swap-1 as mid
```


length = 14
s = swap
C  O  A  C  H  A  B  L  E  R  O  C  K  S

lo                                                  hi
00   01  02  03  04  05  06  07  08  09  10  11  12  13
[C]   O   A   C   H   A   B   L   E   R   O   C   K   S 
p     s
      i

this is how it starts off. No change. index 1 is not less than pivot

--

[C]   A   O   C   H   A   B   L   E   R   O   C   K   S 
p     s   i

index 2 is less than pivot. swap index 1 and index 2. Increment swap. i++ will happen because of loop like every step.

--

C   A   O   C   H   A   B   L   E   R   O   C   K   S 
p       s   i

this is where the next step is. index 3 (C) is not less than C. Neither will H.

--

C   A   A   C   H   O   B   L   E   R   O   C   K   S 
p       s           i

index 5 is less than pivot. Exchange with swap index at 2. incremement swap.

--

C   A   A   C   H   O   B   L   E   R   O   C   K   S 
p           s           i

this is how it'll be during the next check.


C   A   A   B   H   O   C   L   E   R   O   C   K   S 
p               s           i

B and C have been swapped (index 3 and index 6)
swap i with s and both increment. This will be done in one step above this time.

No other swaps happen for the loop.

--

B   A   A   C   H   O   C   L   E   R   O   C   K   S

final swap.
exchange swap index - 1 with pivot. So swap index 3 (swap - 1) with index 0 (pivot)
Return 3 as the new mid-point
pivot is in the correct spot.

--

Next recursive conquering is first 3 indexes only because of being lo to the mid-point (LeftHalf)

lo      hi
00   01  02  03  04  05  06  07  08  09  10  11  12  13
[B]   A   A   C   H   O   C   L   E   R   O   C   K   S

--

There will only be 3 final swaps doing a smaller part of the LeftHalf each time and making sure the pivot is in the correct final spot. The first four elements are fully sorted with pivot put in its correct place for each

A   A   B   C   H   O   C   L   E   R   O   C   K   S

--






### Substring Matching Algorithms

#### Knuth Morris Pratt

##### Consider the input string S = 'ABCABDABCA' and the substring P = 'ABCA'. Walk through the steps of the Knuth-Morris-Pratt algorithm to find all occurrences of P in S. Show the intermediate values of the failure function and the table used to match the characters in P against S. Indicate the starting index of each occurrence of P in S, and explain how the algorithm identifies each occurrence.

Prefix Table:
index: 0  1  2  3
Char:  A  B  C  A
prefix (PX): 0  0  0  1
Explanation: The final A is the suffix and the prefix of A at the beginning is the same. The number put into the prefix table for P[3] is 1 because it matches the suffix and we do index + 1 to know where to stat from.

Tracing:

S[0] == P[0]. Continue both pointers
S[1] == P[1]. Continue both pointers
S[2] == P[2]. Continue both pointers
S[3] == P[3]. Complete match from index S[0].
Move to next S string char, S[4], but for P we have to consider the prefix table. The last match means that the prefix and suffix are a match. Looking at PX[3] we can see that we should move up by 1 index instead of starting P over. We start from P[1]

S[4] == P[1]. Continue both pointers. 
S[5] != P[2]. No match
The matching pattern is reset to the beginning and the first P substring letter, P[0] will attempt to be matched with same S string letter as this time.
S[5] != P[0]. No match. Only continue the S string pointer to next index. Try to begin a match again with the prefix of substring P, P[0]
S[6] == P[0]. Continue both pointers
S[7] == P[1]. Continue both pointers
S[8] == P[2]. Continue both pointers
S[9] == P[3]. Complete match from S[6].

Matches at index 0 and 6





#### Rabin Karp

##### Consider the input string S = 'ABCCABCABCA' and the substring P = 'ABC'. Walk through the steps of the Rabin-Karp algorithm to find all occurrences of P in S, using a hash function that maps each character to its ASCII code. Assume a prime base number of 101. Show the intermediate hash values for each P window in S, and explain how the algorithm identifies each occurrence. Note any false positives the algorithm might produce, and explain why they occur.

Hashing Algo:
The formula is the number of the char * prime number to where the character is in the substring length.
So below for A B C with a prime base number of 101, the hash is:
A*101^0 + B*101^1 + C*101^2
Then to switch to be able to compare to a different hash that is based off sliding one character to the right and thus removing the first character and adding a new last character is by modifying the hash above:

A*101^0 + B*101^1 + C*101^2
subtract A
divide by the prime number (101). This leaves you with:
B*101^0 + C*101^1
Now the next character can be added with prime number to power of its position which is index 2 in this case
B*101^0 + C*101^1 + C^101^2

Saadh remember: This can be seen as sliding things one to the right each time and you can do this in your head/with quick jotting. When i did each hash i copy pasted the current hash for the next one. And shifted each thing to the left. I have a quick video I'll do and show for this asap. It'll take 1 min to show and remind myself.


P substring hash:
A B C
1*101^0 + 2*101^1 + 3*101^2

Going through S string:

ABC - match (S[0])
1*101^0 + 2*101^1 + 3*101^2
30806

BCC - no match
2*101^0 + 3*101^1 + 3*101^2

CCA - no match
3*101^0 + 3*101^1 + 1*101^2

CAB - no match
3*101^0 + 1*101^2 + 2*101^2

ABC - match (S[4])
1*101^0 + 2*101^1 + 3*101^2

BCA - no match
2*101^0 + 3*101^1 + 1*101^2

CAB - no match
3*101^0 + 1*101^1 + 2*101^2

ABC - match (S[7])
1*101^0 + 2*101^1 + 3*101^2

BCA - no match
2*101^0 + 3*101^1 + 1*101^2

Matched S[0], S[4], S[7]



#### Boyer-Moore

##### Consider the input string S = 'ABCBACBABCA' and the substring P = 'ABC'. Walk through the steps of the Boyer-Moore algorithm to find all occurrences of P in S. Show the tables used to implement the 'bad character' and 'good suffix' rules, and indicate the starting index of each occurrence of P in S. Explain how the algorithm identifies each occurrence and how it uses the 'bad character' and 'good suffix' rules to skip unnecessary comparisons. Note any edge or corner cases the algorithm needs to handle, and explain how it handles them.

__I missed having to study for this. Working on it now__

Learn from character comparisons to skip pointless alignments.
Try alignments in left-to-right order. Try character comparisons in right-to-left order.

##### Bad Character Rule: 
Upon mismatch, skip alignments until (a) mismatch becomes a match, or (b) P moves past mismatched character

If there is no occurences in the string S, then P has to be moved all the way over past the mismatched character

step 1
T: G C T T C T G C T A C C T T T T G C G C G C
P: C C T T T T G C

going from right to left: C, then G, T match, but T[4], C, and P[4], T, are mismatches

step 2
T: G C T T C T G C T A C C T T T T G C G C G C
P:       C C T T T T G C

T[4] and P[1] match now. Going from right to left we see C match, but then T[9], A, and P[6], G, don't match.

step 3:
T: G C T T C T G C T A C C T T T T G C G C G C
P:                     C C T T T T G C

Move P past T[9], A, and now the string matches up

-----

##### Good Suffix Rule:
Let t = substring matched by inner loop; skip until (a) there are no mismatches between P and t or (b) P moves past t
aka: t is what is currently matched

Example:

step 1:
               t<->t
T: C G T G C C T A C T T A C T T A C T T A
P: C T T A C T T A C

Move P over to match another substring where the substring currently matches up with where t is (T[6] to T[8]). That would be moving P[2] along T[6]

step 2
               t    <->    t
T: C G T G C C T A C T T A C T T A C T T A
P:         C T T A C T T A C

now t covers a lot more matching. T[6] to T[12].
Move P over 3 alignments. It started at T[4] and now will begin at T[8]

step 3
T: C G T G C C T A C T T A C T T A C T T A
P:                 C T T A C T T A C

A match


bad match table:


Value = max(1, lengthOfPattern - indexOfActualChar - 1)

letters: A B C
values:  2 1 1

But the last character is a wildcard:

letters: A B *
values:  2 1 1


good suffix table:

--


S = 'ABCBACBABCA'
P = 'ABC'

S = A B C B A C B A B C A
P = A B C

S[0] is a match. Move it over...

S = A B C B A C B A B C A
P =       A B C

