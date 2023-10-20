## Free Response Questions

### Hashmaps

1. What does a hashmap do? What are the functions a hashmap class provides?
A. A hash map stores key value pairs allowing quick operations in constant runtime. The keys are hashed to allow finding the index in the array. A hash function takes in a key and returns an integer between 0 to M (large prime number to modulo)

get(key) -> get value based off key, put(key, value) -> insert or update key value pair, contains(key) -> if key is in hash map. There can also be delete(key) -> delete the key value pair and _hash(key) -> get the hash value from key


2. What is the benefit of using a hashmap over an array or linked list?
A. Store a key value pair vs just a value. Runtime complexity for most operations is constant vs linear. Hashmaps have collision control where multiple keys can point to the same index. Hashmap efficiency and benefits also help if ordering of elements doesn't matter. Hashmap order doesn't matter.
Specifically over arrays, hashmaps aren't necessarily a set size. Over linked lists, space complexity is less with it being an array vs linked list data structure


3. What are the runtimes of the get/set functions in a hashmap? Best, average, and worst-case?
A. get and set both have the same runtimes. Best and average is O(1). Worst case is O(n) because all key collisions could be in one index.


4. What type of input gives the worst case for hashmap? How can we prevent this from happening?
A. An input with a lot of collisions because of a poor hash function.
Have a good uniform hash function. Hash function should repeat hashes pointing to same index as infrequently as possible.


5. Here are some hash functions: Which one(s) of them are good and why? How would you improve the bad ones?
  a. Hashing a phone number - use the area code. 
  A. Not good. Area code is a really short thing to hash. Tons of collisions with so many numbers having the same area code. Some area codes are maxed out and every number is used. Some area codes are going to be in the hash map more like a metro/city area code. This allows for more collision.
  Could be better by hashing the whole number, salting, or using SHA-2.

  b. Hashing a social security number - use the last four digits. 
  A. Same issues as area code's collision issues. Last four of social as hash won't be as bad as area code, but it will still cause needless collisions and it's not uniform.
  Could be better by hashing the whole number, more of it, and/or salting or using SHA-2.

  c. Hashing a string - use the sum of each of the character's ASCII codes
  A. Not good. This doesn't care about the order of characters. That will cause collisions. "saadh" and "hdaas" would be the same hash. This is better than the rest, but the uniformity issue of bad distribution in the array should still happen.
  Could be better by salting or using SHA-2. Hashing the whole string is not as effective here because of duplicates.

  d. Hashing a Person object - using the Person's age
  A. The collisions would be enormous. Every one in the world is only up to 120 years. The distribution and uniformity of the hash map would be awful.
  Something else entirely has to be used. This is even worse than area codes. A combo of 2-3 attributes of the person, and/or salting, and/or using SHA-2 works better.


6. How are collisions handled in linear probing? How are collisions handled in separate chaining? Describe the differences in detail.
A. Linear probing looks at following array index values to see if there is any empty one. Add the colliding hash value in the next empty one. When retrieving a value, keep checking for the value after the index it resolves to. Stop searching if an empty index value comes up.
Separate chaining creates a linked list in the index value spot. The get operation will go through the linked list until the value is retrieved or the whole linked list is traversed.
They are completely different approaches. Separate chaining seems to make more sense to use. Linear probing seems like it would fine for small scale or quick algo or code. Otherwise runtime can start getting long.


7. Suppose I implement a hashmap with the hash function h(x) = x mod 10, a list of length 10, and with linear probing. I insert the elements 32, 47, 42, 43, 15, 19, 16, 27 in that order. Write out what the list of the hashmap looks like after each insert. 
A. 
OG
[0: , 1: , 2: , 3: , 4: , 5: , 6: , 7: , 8: , 9: ]

Insert 32
[0: , 1: , 2: 32, 3: , 4: , 5: , 6: , 7: , 8: , 9: ]

Insert 47
[0: , 1: , 2: 32, 3: , 4: , 5: , 6: , 7: 47, 8: , 9: ]

Insert 42
[0: , 1: , 2: 32, 3: 42, 4: , 5: , 6: , 7: 47, 8: , 9: ]

Insert 43
[0: , 1: , 2: 32, 3: 42, 4: 43, 5: , 6: , 7: 47, 8: , 9: ]

Insert 15
[0: , 1: , 2: 32, 3: 42, 4: 43, 5: 15, 6: , 7: 47, 8: , 9: ]

Insert 19
[0: , 1: , 2: 32, 3: 42, 4: 43, 5: 15, 6: , 7: 47, 8: , 9: 19]

Insert 16
[0: , 1: , 2: 32, 3: 42, 4: 43, 5: 15, 6: 16, 7: 47, 8: , 9: 19]

Insert 27/Final
[0: , 1: , 2: 32, 3: 42, 4: 43, 5: 15, 6: 16, 7: 47, 8: 27, 9: 19]


### Recursion

1. What is recursion? How do you make sure recursion does not run infinitely?
A. When a function calls itself. The code repeats the recursive calls until a base case terminates the code.


2. How do you convert a function with iteration (e.g., a for loop) to a recursive function? For example, how can I loop through numbers in a list using recursion?
A. Add a base case at the start of the function for the first stack call^ and to stop the recursion from going any deeper. The iteration/loop logic has to be converted to a recursive call.

^I'm not sure if this is called the first or last. I think of it as the first because its value gets returned first

Here's an example written out by me of looping through a list:
```
# Iteration
def fn_i(lst):
  totes = ''
  for i in lst:
    totes += str(i)
  return totes

# Recursion
def fn_r(lst, n):
  if n == 0:
    return ''
  return fn_r(lst, n - 1) + str(lst[n])

# Test
arr = [1, 2, 3, 4, 5]
n = len(arr) - 1
print(fn_i(arr))
print(fn_r(arr, n))
```

3. What is binary search? What is the requirement for the thing (e.g., list) that you are doing a binary search on?
A. An efficient way to search a sorted array or list by slicing off half of the array during each loop iteration. The list has to be sorted. Or at least rotated sorted of some kind.


4. What is the runtime and space complexity for binary search?
A. The runtime is O(log n). Every recursive call reduces the elements in half. This is logarithmic. Space complexity is O(log n) because of the number of recursive calls done.


## Runtime Analysis 

### For each of the following code blocks, please answer the following and explain your answer choices.
a. For n=2,4,8,16 compute f(n). 
b. What does the code block return? (In terms of n). Explain your answer.
c. What is the runtime of the code? Explain your answer.

```
# Code Block A
def fn_a(n: int) -> int:
  if n == 1:
    return n
  return fn_a(n - 1) + 1
1. 
a.
f(16) = f(15) + 1 = 16
f(8) = f(7) + 1 = 8
f(4) = f(3) + 1 = 4
# f(3) = f(2) + 1 = 3
f(2) = f(1) + 1 = 2
# f(1) = 1

b. f(n) = f(n) .The base case returns 1. Each number over 1 adds 1
c. O(n)


# Code Block B
def fn_b(n: int) -> int:
  if n == 1:
    return n
  return fn_b(n - 1) + fn_b(n-1)
2. 
a.
f(16) = f(8) + f(8) = 32
f(8) = f(4) + f(4) = 16
f(4) = f(3) + f(3) = 8
# f(3) = f(2) + f(2) = 4
f(2) = f(1) + f(1) = 2
# f(1) = 1

b. f(n) = 2^n-1 (Like Fibonacci)
c. O(2^n)


# Code Block C
def fn_c(n: int) -> int:
  if n == 1:
    return n
  return fn_c(n - 1) * n
3. fn_c
a. 
f(16) = 20.9T
f(8) = 5040 * 8 = 40320
# f(7) = 720 * 7 = 5040
# f(6) = 120 * 6 = 720
# f(5) = f(4) * 5 = 120
f(4) = f(3) * 4 = 24
# f(3) = f(2) * 3 = 6
f(2) = f(1) * 2 = 2
# f(1) = 1

b. f(n) = n!
c. O(n)


# Code Block D
def fn_d(n: int) -> int:
  if n <= 1:
    return 1
  count = 0
  for i in range(n):
    count += i
  return fn_d(n//2) + fn_d(n // 2) + count
4. fn_d
a. 
f(6) = f(3) + f(3) + 15 = 23
f(5) = f(2) + f(2) + 10 = 16
f(4) = f(2) + f(2) + 6 = 12
f(3) = f(1) + f(1) + 2 = 4
f(2) = f(1) + f(1) + 1 = 3
f(1) = 1

b. f(n) = ?
c. O(2^n)


# Code Block E
def fn_e(n: int) -> int:
  if n == 0:
    return 1
  return fn_e(n // 2) + fn_e(n // 2)
5. fn_e
a. 
f(16) = f(8) + f(8) = 32
# f12 = f6+f6 = 16
# f10 = f5+f5 = 16
# f9 = f4 + f4 = 16
f(8) = f(4)+f(4) = 16
# f7 = f3+f3 = 8
# f6 = f3+f3 = 8
# f(5) = f(2) + f(2) = 8
f(4) = f(2) + f(2) = 8
# f(3) = f(1) + f(1) = 4
f(2) = f(1) + f(1) = 4
# f(1) = f(0) + f(0) = 2
# f(0) = 1

b. 2^n-1 (floor power of 2) < f(n) <= 2^n (ceiling power of 2)
c. O(2^n)


# Code Block F
def fn_f(n: int) -> int:
  if n + 1 < 0:
    return n
  return fn_f(n // 2) + fn_f(n // 2)
6. fn_f
a. 
f
f(4) = f(2) + f(2)
f(2) = f(1) + f(1)
f(1) = f(0) + f(0)
f(0) = f(0) + f(0)
**loops infinity**

b. f(n) = infinity
c. O(infinity)


# Code Block G
def fn_g(n: int, m: int) -> int:
    if n <= 0 or m <= 0:
        return 1
    return fn_g(n//2, m) + fn_g(n, m//2)
7. fn_g
a. 
No proper way of calculating. Two arguments
f(4,4) = f(2,4) + f(4,2)

f(2,4) = f(1,4) + f(2,2)
f(4,2) = f(2,2) + f(4,1)

f(1,4) = f(0,4) + f(1,2)
f(2,2) = 

f(2,2)
f(4,1)

b. f(n,m) = ?
c. O(2^n +2^m)
```
