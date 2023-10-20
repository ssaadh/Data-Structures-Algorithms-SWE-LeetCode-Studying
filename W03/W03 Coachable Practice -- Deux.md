## Free Response Questions

### Hashmaps

#### 1. What does a hashmap do? What are the functions a hashmap class provides?
A hashmap stores key-value pairs in a data structure, like an array (excluding possible chaining with linked lists). The key value pair get placed into the array at the hashed index of the key.

Function
hash: takes in the key input and converts it to an integer.

put: Places key-value pair in the hashmap based on the key's hashed integer value.
O(1) for separate chaining as it can be placed at the front of the linked list. Up to O(n) for linear probing to go through the array looking for an empty index.

get: Gets a value based on the key. Return None/-1, etc if not found.
O(1) best runtime. O(n) worst if all the keys get hashed to the same index.

contains: Boolean return based on if key is in the hash map.
Same runtime as above

delete: Not always included. Rare to delete key-value pairs.
Would be same runtime as above.



#### 2. What is the benefit of using a hashmap over an array or linked list?
A hashmap is a data structure built on top of an array and possibly linked lists if doing separate chaining. The major benefit above not just those data structures, but in general, is the fast avg runtimes. All the major functions are O(1) in the best case. It also is able to combine the best parts of arrays and linked lists as shown when comparing average runtimes:

Access, Search, Insertion, Deletion
Array: O(1), O(n), O(n), O(n)
Linked list: O(n), O(n), O(1), O(1)
Hashmap: not a function, O(1), O(1), O(1)

Hashmaps have all 3 functions be O(n) runtime at their worst if the key-value pairs are as far from uniformly placed in the array indexes as possible (all keys going to the same index)



#### 3. What are the runtimes of the get/set functions in a hashmap? Best, average, and worst-case?
Best and average are the same which is a primary benefit of hashmaps. The cases are in #1



#### 4. What type of input gives the worst case for hashmap? How can we prevent this from happening?
Inputs that go to the same index in the hashmap causing collisions. A hash function that is able to evenly spread the key-value pairs across   Prevent this with a hash function for the inputs that outputs indexes as distributed/varied as possible. Ideally, the stored data is distributed



#### 5. Here are some hash functions: Which one(s) of them are good and why? How would you improve the bad ones? When identifying one is bad, point out which quality of a good hashing function is not met.

Should I be thinking about these sorts of questions as if modulo is used at some point too?
Does SHA-2 or any hashing functions matter for this or is that for security only?


##### a. Hashing a phone number - use the area code. 
Area codes are the basis of how numbers are given out. They are already organized first by area code. It's too common and overlapping. If there is more of one area code because the phone numbers are more from one specific geographic region, it will make the distribution and uniformity worse

Alternative: Hashing the whole phone number. Not sure if area code should be included for this. Without the area code there will be a number of duplicate 7 digit numbers matching the same index, but it shouldnt be enormous.
2nd Alt: Using the last 4 or 7 phone number digits along with getting the sum of the phone number and combining them.


##### b. Hashing a social security number - use the last four digits. 
Social security is 9 digits. The last 4 are a lot better than using the first K digits of a social security number as that falls into the same issue where numbers are given in some sort of grouping or ordering and that won't be as uniformly distributed

Alt: Add up the individual social security numbers into one sum and do math with that and the last 4 or 6 social security numbers.


##### c. Hashing a string - use the sum of each of the character's ASCII codes
- If this is adding it up to one total sum then that won't be good.
- This will lack uniformity as that single number may lead to lots of collisions.
- The ordering of characters won't matter for the sum of them all.
- That's similar to why the numbers aren't being added up for the integer inputs above.

Alt: Be able to care about the order of characters as well. I'm not  sure how this would be able to happen for a string.
_I can look up more how this can be done better_


##### d. Hashing a Person object - using the Person's age
- There's 8 billion people divided across under 150 ages. Awful collisions
- Even if this were to be about people's ages who are dead so it could allow some people to 10K years old, since so many more people have been alive in modern history, the uniformity for people in the past few hundreds years would be too much.

Alternative: Hash together two different parts of the Person object.



#### 6. How are collisions handled in linear probing? How are collisions handled in separate chaining? Describe the differences in detail.

Collisions happen when two key inputs lead to the same hashed index.

Linear probing:
- For putting: If the index is filled, place the key-value pair into any empty indices that comes up next.
- When getting, either eventually find the correct key or stop if an empty indice comes up or the end of the array is reached.

I believe Coach Tim said that under linear probing if there is no more space available then usually the underlying array is doubled in size and the data is transferred over. The queued remaining key-value pair can be placed into the bigger array empty indices
_Could they be placed in indices that come before as well?_

Separate chaining:
Each array index has a linked list. 
- Getting: Go to the correct hashed index, then iterate through the linked list one by one until the correct key is found
- Putting: Place the key-value pair at the beginning of the linked list in the index. O(1) every time.



#### 7. Suppose I implement a hashmap with the hash function h(x) = x mod 10, a list of length 10, and with linear probing. I insert the elements 32, 47, 42, 43, 15, 19, 16, 27 in that order. Write out what the list of the hashmap looks like after each insert. 

[ 0: , 1: , 2: 32, 3: 42, 4: 43, 5: 15, 6: 16, 7: 47, 8: 27, 9: 19 ]

32 goes in normally to index 2
47 goes in normally to index 7
42 tries going into index 2, but that's filled w/ 32. It goes to the next empty index, index 3
43 tries going into index 3, but that's filled w/ 42. It goes to the next empty index, index 4
15 goes in normally to index 5
19 goes in normally to index 9
16 goes in normally to index 6
27 tries going into index 7, but that's filled with 47. It goes to the next empty index, index 8



### Recursion

#### 1. What is recursion? How do you make sure recursion does not run infinitely?
Recursion is when a function calls itself and is able to terminate the code with a base case, a conditional statement.
When the recursive function call itself, there is a reduction step where the input changes while passed to the function calling itself. Once the input reaches a certain amount, a conditional called the base case, will terminate the code

_Q: why is it called a reduction step? The input can get bigger no? The base case can be conditional for a big value_



#### 2. How do you convert a function with iteration (e.g., a for loop) to a recursive function? For example, how can I loop through numbers in a list using recursion?

```
def iteration(lst):
  sum = 0
  for num in lst:
    sum += num
  return sum

def iteration2(lst):
  sum = 0
  for num in range(len(lst)):
    sum += lst[num]
  return sum
```

```
def recursion(lst, num):
  if num < 0:
    return 1
  return recursion(lst, num - 1) + lst[num]

def recursion_slice(lst):
  if len(lst) == 0:
    return 0
  return recursion1(lst[:-1]) + lst[-1]

lst = [1,2,4,8,16]
recursion(lst, len(lst) - 1)
```
EDIT: After going through week 4 I see I could slice the array each time too without passing in a counter

See the base case which is sum = 0 and turn that into a conditional or base case. Take the smallest part of what needs to be solved or iterated on and turn that into the recursion steps. The next number in the list is added to the previous sum each time in iteration. This can be turned into adding the current counter which starts at the length of the array and goes down until 0.

Or can take each part of the array and go line by line in the recursion and add it to the previous sum which would started at the base case. So it would do the same thing as the iteration except with recursion.



#### 3. What is binary search? What is the requirement for the thing (e.g., list) that you are doing a binary search on?
#### 4. What is the runtime and space complexity for binary search?

Binary search goes through a _sorted_ array to return an index based on a target. It does this in O(log n). Splitting what needs to be looked at in half each time. This makes the space O(log n) too due to each split being recursive and going on the call stack.

The core algo is:
target < value: Left Half
target > value: Right Half
target == value: return Index



### Runtime Analysis 

For each of the following code blocks, please answer the following and explain your answer choices.

#### 1. For n=2,4,8,16 compute f(n).  For large values with exponents or factorials, you can leave them in the form a^b or c! you do not need to compute them. In code block G, please compute for m=n i.e. (m,n) = (2,2),(4,4),...(16,16)

#### 2. What does the code block return? (In terms of n) You may use asymptotics (big O), but we encourage you to find an exact answer when you can. Explain your answer.

#### 3. What is the runtime of the code? Explain your answer.

Select from the following options: 0, 1, ~n, ~2n, ~log n, ~n log n, ~n^2, ~2^n, ~n!, ∞/infinity

Note: When describing the runtime, please describe qualitatively why the code would give that runtime. Do not use empirical data to justify a runtime. For examples 

f(4) = 4, f(8) = 5, f(16) = 6 so it's O(log n)
Is not an acceptable answer. What we're looking for is something like:
The recursive call return f(n /// 2) + 1 reduces the input in half each time until the function terminates with a base case of n=0. Therefore the runtime is O(log n)

Many different functions could be O(log n) - we want you to identify what types of code lead to O(log n) runtime. This way you won't need to calculate f(n) for several values to identify the runtime. We encourage computing a few cases of n manually to get intuition, but after that you should look for what about the code makes that runtime happen.

Hint: If you're having trouble identifying the runtime, try the following.

Think of functions you are already familiar with. Can you see any clear pattern between what you know and what is there? Ones you know are Fibonacci, factorial, etc.

Look at how n is being reduced. Then try some sample values of n and see what happens. You may want to try 5,6,7,8...  and see how it grows. Or perhaps try 2,4,8,16,32,... depending on the problem.

(2) will help you see the pattern. Once you see the pattern, it can be easier to try and describe it.

#### Code Block A
def fn_a(n: int) -> int:
  if n == 1:
    return n
  return fn_a(n - 1) + 1

1. 
a(1) = 1
a(2) = 2
a(4) = 4
= a(3) + 1 = (a(2) + 1) + 1 = (a(1) + 1) + 1 + 1
a(8) = 8
a(16) = 16

2. a(n) = n. The recursive part does n calls subtracting input by 1 each time and each call adds 1.

3. O(n). The recursive part does n calls subtracting input by 1 each time and each call adds 1.



#### Code Block B
def fn_b(n: int) -> int:
  if n == 1:
    return n
  return fn_b(n - 1) + fn_b(n-1)

1. 

_how was i supposed to know the relation is *2. I know it's f(x-1) + f(x-1) but i wouldnt have called it's just 2 * f(x-1) without being used to this problem_

b(1) = 1
b(2) = b(1) + b(1) = b(1) * 2 = 2
b(3) = b(2) + b(2) = b(2) * 2 = 4
b(6) = b(5) * 2^1 = b(4) * 2^2 = b(3) * 2^3 = b(2) * 2^4 = b(1) * 2^5
b(8) = b(7) * 2 = b(6) * 2^2 = b(5) * 2^3 = b(4) * 2^4 = b(3) * 2^5 = b(2) * 2^6 = b(1) * 2^7
b(16) = 2^15


2. b(n) = 2^(n-1) because the input goes down by one but is adding to itself which is the same as multiplung by 


3. O(~2^n) because 


#### Code Block C
def fn_c(n: int) -> int:
  if n == 1:
    return n
  return fn_c(n - 1) * n

1.
c(1) = 1
c(2) = c(1) * 2 = 1 * 2 = 2 = 2^1
c(3) = c(2) * 3 = c(1) * 3 * 3 = 3^2 = 9
c(4) = c(3) * 4 = c(2) * 4 * 4 = c(1) * 4 * 4 * 4 = 4^3 = 64
c(8) = c(7) * 8 = c(6) * 8^2 = c(5) * 8^3 = c(4) * 8^4 = c(3) * 8^5 = c(2) * 8^6 = c(1) * 8^7
c(16) = 16^15

2. c(n) = n^(n-1)

3. O(~>n!) or O(~n^(n-1))


#### Code Block D
def fn_d(n: int) -> int:
  if n <= 1:
    return 1
  count = 0
  for x in range(n):
    count += x
  return fn_d(n//2) + fn_d(n // 2) + count

1. 
d(1) = 1
d(2) = (d(1) * 2) + 2 = (1 * 2) + 2 = 2^1 + 2 = 4
d(3) = (d(1) * 2) + 2 = 2^1 + 2 = 4
d(4) = (d(2) * 2) + 4 = (d(1) * 2 * 2) + 4 = 2^2 + 4 = 8
d(8) = d(4) * 2 + 8 = (d(2) * 2 * 2) + 8 = (d(1) * 2 * 2 * 2) + 8 = 2^3 + 8 = 16
d(16) = (d(8) * 2) + 16 = (d(4) * 2 * 2) + 16 = (d(2) * 2 * 2 * 2) + 16 = (d(1) * 2 * 2 * 2 * 2) + 16 = 2^4 + 16 = 32
assumption:
d(32) = 2^5 + 2^5 = 64

2. d(n) = n + n

3. 
O(n log n) because the input divides in half each time which should be some sort of log n and the additional O(n) for the summing up of the count 

  
#### Code Block E
def fn_e(n: int) -> int:
  if n == 0:
    return 1
  return fn_e(n // 2) + fn_e(n // 2)

1. 
e(0) = 1
e(1) = e(0) + e(0) = e(0) * 2 = 1 * 2 = 2
e(2) = e(1) * 2 = e(0) * 2 * 2 = 1 * 2^2 = 2^2 = 4
e(3) = e(1) * 2 = 2^2 = 4
e(4) = e(2) * 2 = e(1) * 2 * 2 = e(0) * 2 * 2 * 2 = 1 * 2 * 2 * 2 = 2^3 = 8
e(6) = e(3) * 2 = e(1) * 2 * 2 = 2^3
e(8) = e(4) * 2 = e(2) * 2 * 2 = e(1) * 2 * 2 * 2 = e(0) * 2 * 2 * 2 * 2 = 2^4 = 16
e(16) = e(8) * 2 = (e(4) * 2) * 2 = 2^5 = 32
assumption:
e(32) = 2^6 = 64

2. e(n) = 2n

3. O(~2n)


#### Code Block F
def fn_f(n: int) -> int:
  if n + 1 < 0:
    return n
  return fn_f(n // 2) + fn_f(n // 2)

this is infinity when n > -1


#### Code Block G
def fn_g(n: int, m: int) -> int:
    if n <= 0 or m <= 0:
        return 1
    return fn_g(n//2, m) + fn_g(n, m//2)

1. 
g(0,0) = g(0,0) + g(0,0) = 1 * 2 = 2
g(1,1) = g(1,1) * 2 = 

g(2,2) = g(1,2) * 2 = 

g(4,4) = g(2,4) * 2 = 

g(8,8) = g(4,8) * 2 = 

g(16,16) = g(8,16) * 2 = 

2.
The recursive relation is:
g(n//2, m) + g(n, m//2)
this can be simplified to using n for m:
g(n, n) = g(n/2, n) + g(n, n/2)
this can be simplified to:
g(n, n) = 2 * g(n/2, n)


3. O(~2*log n) or O(~log n). The final simplified value of the value of n appears to be close to the example given for merge sort in recursive relations curriculum text but without the extra addition of n.
