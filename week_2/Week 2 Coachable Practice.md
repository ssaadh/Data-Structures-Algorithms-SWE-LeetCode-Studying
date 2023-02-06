# Week 2 Coachable Practice

## Free Response Questions

### Logarithms and Exponents

#new
1. Compute all powers of 2 up to 10. I.e. write 2^0, 2^1, 2^2, ..... 2^10 
A. 1, 2, 4, 8, 16, 32, 64, 132, 256, 512, 1024

2. What does logarithm mean? If you were given log(n) = x, describe in plain English the relationship between n​ and x  
A. The power to which a number must be raised to get a value. "n" is a number. It is to base "b" which defaults to 2. The base being raised by a power is the logarithm.

3. How much larger is 2^31​ than 2^28? Hint: Do not compute them each.
A.
2^31 - 2^28
2^3
8x larger

4. How much larger is 1 billion than 1 million ?
A. 1000x larger

5. How much larger is log(1 million) than log(1 billion) ?
million^ is largesr. subtract
A. 3 units larger. 10^3 (1000x) is the difference

6. If log(64) = y  , write log(128) in terms of y   
Add one to y. Base is 2. 64*2=y + 1. Add 1

log(64) = y
log(2^6) = y

log(2^7) = log(128)
log(2^7) = x

6 = y
7 = x
6 + 1 = x
**y + 1 = x**


7. If log(x) = 128  , write 128 in terms of x without using the logarithm.
A. log(x) = log(2^128) = 128
x = 2^128
2 raised to log of anything is that thing. like: 2^log(x) = x
log of something asks log(x) = 128 then e  = 2^128



8. If log(x / y) = 4 , write a relationship between x/y without using the logarithm.
A. x / y = 2^4
x = 16y


9. If log(x * y) = 8 write a relationship of x,y without using the logarithm. 
A.
x * y = 2^8 = 256


10. If the x = 2^8​. Rewrite x using base 4. If x = 4^y what is y? 
A. 
log(x) = 8
log(4^y) = 8
4^y = 2^8
2^2y = 2^8
y = 4


### Runtime Analysis 

1. What is the runtime to iterate through a list of size n.
A. O(n)


2. Write a function that runs in each of the following runtimes O(1), O(log n), O(n), O(n log n), O(n^2), O(n^2 log n), O(n (log n)^2), O(2^n).
A. code_segments.py


3. What does logarithm mean? Rigorously.
A. The opposite of exponential. The most common is base 2. The base 2 log of 16 is 4. 2^4 is 16.


4. What happens to the runtime when operations are nested? What relationship is that to the runtime?
A. The operations are exponential.


5. Given a table of code runtime (input size/runtime), can you determine what order of growth these functions have? Hint: Applying the doubling principle.
A. Code A: O(n). Code B: O(1). Code C: O(n log n).


### Explain and Analyze Code
Please answer the following for each block of code. You can assume nums is an integer array of size n​
a. Determine the function for nums = [1,1,1,1,1]
b. Determine the function for nums = [1,2,3,4,5]
c. What does this function do?
d. What is the runtime complexity? And why?
e. What is the space complexity? And why?

01. (a) 25  (b) 75  (c) All the elements of the nums parameter are added to all_nums. This is repeated n times. The long array is length n*n or n^2. The values of all the elements in the list are added together.  

(d) O(n^2). Nested loop  (e) O(2 + n^2). ~O(n^2). all_nums

# 1. func_one([1,1,1,1,1]) = 15
# 2. func_one([1,2,3,4,5]) = 25
# 3. This function takes a list of numbers and adds them all together
# 4. O(n^2) because there are two for loops
# 5. O(n) because the output is the same size as the input

02. (a) 25  (b) 75  (c) The same thing as before except the aadding up of values is done in the nested loop. There's no list. 

(d) O(n^2) nested loop (e) O(2). ~O(1).  2 variables

03. (a) 3  (b) 12  (c) Looping while n, length of nums argument, is greater than 0. It is greater than zero while n is being divided by n - 1 index in nums argument. Adds the value of the top half of numbers in an array of integers 

(d) O(log n). One loop dividing in half (e) O(1). 2 variables.

04. (a) 10  (b) 30  (c) loop for the sum of the value by itself. Then get sum of the new array.  

(d) O(2n) = ~O(n). one loop and sum.  (e) O(n). double_nums is size n.

05. (a) 32  (b) 98  (c) Nested loop. First loops as long as nums length. Inner loop does as many loops as that current array element value. Loop gets the value of power_sum. Return remainder of dividing by 99.  

(d) O(n^2) = ~O(n*n^2). Inner loop is n^2. Separate loop is n.   (e) O(1). 2 variables

06. (a) 3  (b) 2  (c) Loop skips 0. To length of array. Checks if current value is less than previous index value times 2 and current value is more than the next value divided by 2. If so, iterate count. Return count.  

(d) O(n). Loop in range N-2  (e) O(1). 1 variable 

#new
07. (a) 8  (b) 19  (c) n and N is length of list argument. While n is greater than 0, loop through range of length of array. total is total plus current arr value. Inside while loop, n is floor of dividing by 2. Return total. 

(d) O(n log(n)). log(n) is while loop. for loop uses same variable, n, which is being cut in half rounded down. I don't know why its run time isnt what 7 or 8 is. (e) O(1). N, total, n are simple variables.   

08. (a) 7  (b) 14  (c) Same initial as before. While loop for i being less than length of argument. range 0 to i. Add the current value to total. Multiply i by 2. Return total.  

(d) O(log(n)^2). The outer loop is log N. The inner loop is dynamic but ends up being close to log N. Not sure about this.  (e) O(1). N, total, i, j are single variables only. 

09. (a) 15  (b) 45  (c) Same initial as before. Same while loop for i being less than the length of the argument. Range 0 to set length of argument. Add current arr value to total. Iterate by multiplying i by 2. Return total.  

(d) O(n log(n)). The outer and inner loop are the same every time based on input length. Not sure what that makes this specifically. Outer loop is log N. Inner loop is always input length or n.  (e) O(1). N, total, i, j are single variables only  

10. (a) [2, 2, 2, 2, 2]  (b) [6, 6, 6, 6, 6]  (c) Dunction takes in a list of integers. Sorts ascending by default. Reverses the array. Creates empty array for complements var. Loops through both array and reversed array adding both numbers to the end of complements array. 

(d) O(n log(n) + 2n) = ~O(n (log (n)))). first sort is biggest time sink.  (e) O(2n) = ~O(n). reverse_arr and complements

11. (a) Incorrect input?  (b) Incorrect input?  (c) run helper_func() without argument. O(1). Loop i in range N. Run helper_func(i). another loop then helper_func(). The inner loop runs helper_func(j) for 0 to N. Return.  

(d) O((n^2)(log(n))). nested loop in range N and helper_func(j) in nested loop which is log(n)  (e) O(1)


## Linked List
1. What is a linked list? How is it built? What is the underlying data structure used?
A. A data structure of a sequence of nodes that link to the next element at the very least. It's built with nodes starting off with a head node. The underlying DS is a sequence of nodes?


2. What is the runtime to insert an element to the front of a linked list?
A. O(1).


3. What is the runtime to search if a specific element is in a linked list?
A. Worst case is O(n).


4. What is one example of when a linked list is preferred over an array of a fixed size?
A. Browser history. The last site added in the browser history is the first to be used (last in, first out)


5. What is one example of when an array of fixed size is preferred over a linked list?
A. Grades or scores for the Coachable curriculum. The number of exams, LC, and (maybe) mock interview practices are known.


6. Describe how you would insert an element into the front of a linked list. How is this different from inserting to the end of one?
A. Need access to the head. With head, point element's next node to head. Now the element is head. O(1). Inserting to the end requires iterating from head until there is no next node. Have the last node point next node to the inserted element. O(n).


7. How would you identify if there is a cycle in a linked list?
A. Using "slow and fast" algo. Slow pointer moves one node and the fast pointer moves two nodes per interval. Each time, check if both pointers are at the same node. The fast pointer will eventually catch up to the slow pointer if there is a cycle. Or the fast pointer will reach the end of the linked list determing there is no cycle. This would take at most O(n).


8. Please walk through your approach using the following examples, including all intermediate steps. 
```
 Linked list with cycle (d -> a)
 a --> b --> c --> d
 ^                 |
 |                 V
 <-----------------
 Linked list with no cycle 1 --> 4 --> 3 --> 2 --> None
```
A.
Linked list with cycle
1. slow and fast pointers start at 'a'
2. slow moves to 'b', fast moves to 'c'
3. slow moves to 'c', fast moves to 'a' because of the cycle
4. slow moves to 'd', fast moves to 'c'.
5. slow moves to 'a', fast moves to 'a'.
6. The two match. Within O(n)

Linked list with no cycle
1. slow and fast pointers start at 1.
2. slow moves to 4, fast moves to 3.
3. slow moves to 3, fast moves to None.
4. fast is at none, there is no cycle. Within O(n)


9. Explain how you would reverse a linked list. Explain using the following example. 
`a. 1 --> 4 --> 3 --> 2 --> None`
A. Reversing will look like this: (head) 2 -> 3 -> 4 -> 1 -> None
- Set a curr var to head.
- Set next and prev vars to None.
- Loop through the linked list until curr is None.
- For first iteration:
  - curr is 1.
  - Save curr's Node's next, 4, to the global next var.
  - Assign 1's next pointer to prev var.
  - Set prev to curr. Prev is 1 now.
  - Set curr to next (which was curr's next).
  - Now 4 is curr and can iterate through the loop again


10. How do you iterate through a linked list? Describe this process in detail if you want to print every element in a linked list. 
A. Iterate by traversing from the head to next elements. Assign the head to a curr var. Have a loop while curr is not None. print the current node, then assign curr var to the next node.

11. How can we use linked lists to implement a stack?
A. Stacks are LIFO. The top of the stack is implemented as the head of the list. Push a new node by adding it to the top. Pop the list by removing the top.
Queues is FIFO. Enqueue (add) an item by adding to the tail/back of the list. Dequeue by removing the top/head of the list.

12. Why do you need two pointers for a queue but not required to implement a stack?
A. A queue requires interacting with both sides of a doubly linked list. Enqueue/add to the tail of the list. Dequeue/remove from the head of the list.

13. When would you want to use a doubly linked list?
A. When you need to push, pop and/or enqueue/dequeue on both sides. When need to go both ways, down and up/left and right.

14. What are the differences between stack/queue/deque?
A. stack is LIFO. Queue is FIFO. Stack only pushes and pops on one end (head). Queue adds to the tail, removes from the head. Deque allows adding and removing on both ends.

15. What are their core functions and runtimes?
A.
Stack: 
push: adds element to the top. O(1)
pop: removes top element. O(1)
peek: returns top element. O(1)

Queue: 
enqueue: adds element to the tail/bottom. O(1).
dequeue: remove head/top. O(1).
peek: returns top element O(1)

Deque: 
push_front: add element to top. O(1)
push_back: add element to bottom. O(1)
pop_front: removes top element. O(1)
pop_back: removes bottom element. O(1)
front: return top element. O(1)
back:  return bottom element. O(1)

16. What are some challenges when iterating through a circular linked list?
A. Don't readily know the end of the list. Have to iterate through the list to detect if circular and the end. Same issue with ending in an infinite loop if circular isn't detected.

17. Why are queues better than stacks for ticket lines?
A. The first person who arrives wants to be able to buy a ticket first. That's how ticket lines work. So adding to the tail and taking out from the head (front of the line).

--

#new
### Linked List Code Analysis

Below is a LinkedList class. 
```
class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
        
        
class LinkedList:
    def __init__(self, node):
        # head references first node in chain of nodes
        self.head = node
      
    def function1(self, new_node):
        new_node.next = self.head
        self.head = new_node
  
    def function2(self, new_node):
        if self.head is None:
            self.head = new_node
        return
      
        cur = self.head
        while(cur.next):
            cur = cur.next
        cur.next = new_node
      
    def function3(self):
        if self.head:
            self.head = self.head.next
```

1. Describe function1​ and its runtime. 
A. A new node is assigned to the head. The old head is the next node after head. O(1) runtime.

2. Describe function2 and its runtime. 
A. If there is no linked list, start a new one with new node as the head and only node. Looping through the linked list to assign the new node to the end/tail of the linked list. O(n) runtime. Have to go through the whole linked list of n nodes.

3. Describe function3 and its runtime.
A. If there is a head of the linked list, overrwite that head as the next node/None. Original head is gone. O(1) runtime.


### Stacks 
```
stack = Stack()
stack.push(1) 
stack.push(2) 
print(stack.pop()) 
stack.push(3) 
stack.push(4) 
print(stack.pop()) 
print(stack.pop())
```

4. What is printed when the above code is run? 
A. 
2
4
3

5. What is the current state of the stack after the above code is run?
A. State of each line:
head -> []
head -> [1]
head -> [2,1]
head -> [1]
head -> [3,1]
head -> [4,3,1]
head -> [3,1]
head -> [1]

6. Give one real-life example of a Stack. 
A. I use browser history and undo/redo as my staple examples to remember Stacks. Normally you can't go forward in history or redo until a pop action is done first. Going back or undoing pops the stack. Going forward or redoing pushes the last popped element back into the stack.


### Queues
```
queue = Queue()
queue.enqueue(1)
queue.enqueue(2)
print(queue.dequeue())
queue.enqueue(3)
queue.enqueue(4)
print(queue.dequeue())
print(queue.dequeue())
```

7. What is printed when this code is run? 
A. 
1
2
3


8. What is the current state of the queue after this code is run?
A. 
State each line:
head -> []
head -> [1]
head -> [1,2]
head -> [2]
head -> [2,3]
head -> [2,3,4]
head -> [3,4]
head -> [4]

9. Give one real-life example of a Queue.
A. Queues are normal lists or lines where the first person who arrives is the first person served. New people go to the back.
