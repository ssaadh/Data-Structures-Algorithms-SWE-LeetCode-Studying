<!-----
Conversion notes:
* Docs to Markdown version 1.0β34
* Thu Oct 19 2023 15:38:39 GMT-0700 (PDT)
* Source doc: W5 Coachable Practice HW 2.0
----->


# W5 Coachable Practice HW

## Free Response Questions

### Trees

Extra Info

**Full BT (or proper)**

every parent node/internal node has either two or no children.

**Perfect BT**

every internal node has exactly two child nodes and all the leaf nodes are at the same level

**Balanced BT**

difference between the height of the left and the right subtree for each node is either 0 or 1.

**Complete BT**

just like a Full BT, but with two major differences

- Every level must be completely filled

- All the leaf elements must lean towards the left.

- The last leaf element might not have a right sibling i.e. a complete binary tree doesn't have to be a full binary tree.

--

A binary tree of height ‘h’ having the maximum number of nodes is a perfect binary tree. 

For a given height h, the maximum number of nodes is 2h+1-1.



1. _Explain what a binary tree is using a recursive definition._

    Each [root] node can have at most a left and right child node. The binary tree itself is defined recursively as a structure that consists of a root node and two subtrees, each of which is also a binary tree. Every node is a binary tree.

2. _What are the different traversals that we can do on a binary tree?_

    Breadth First Traversal (iterative while loop with a queue)


        Level-Order Traversal: Visit each node in level order. We start with the root and iterate horizontally across each level.


    Depth First Traversal (recursive function with a stack)

1. Pre-Order: Visits nodes in the following order: current node, left child, right child
    1. In-Order: Visits nodes in the following order: left child, current node, right child
    2. Post-Order: Visits nodes in the following order: left child, right child, parent node \
 \
Always go from the root in a counter clockwise direction around the tree. \
 - Preorder: print the nodes on 1st visit \
 - Inorder: print the nodes on 2nd visit \
 - Postorder: print the nodes on 3rd/last visit \
This means always going to the left and right children of every node including nodes with no children. Count the None child[ren] \
Intuitively, this means a node with no children will have all 3 visits happen at once (the node itself, and both children which dont exist)
3. _Your friend claims that “the time complexity of traversing a tree recursively is O(n), where n is the number of nodes in the tree.” Are they correct? Why/why not?_

    Yes, if there are n nodes, then recursively going through each one would be across n nodes. Each node is visited once.

4. _Your friend claims that “the worst-case space complexity of traversing a tree recursively is O(1), because we are not using extra space to hold a queue like a BFS would.” Are they correct? Why/why not? What if the tree is balanced?_

    Each recursive call to the traversal function adds a new level to the call stack. The maximum depth of the call stack is equal to the height of the tree.


    In the worst case, where the tree is a straight line of nodes (a "skewed" tree), the height of the tree is n and the space complexity is O(n). In the best case, where the tree is perfectly balanced, the height of the tree is log(n) and the space complexity is O(log(n)).

5. _What is the difference between a binary tree and a binary search tree (BST)?_

    A BST is a binary tree with the following properties:


    - All keys in the left subtree are less than the key in the parent node.


    - All keys in the right subtree are greater than the key in the parent node.


    - There are no duplicate keys


    - Both the left and right subtrees must also be binary search trees. 

6. _What is the runtime of searching for an element in a balanced and unbalanced BST? What about the space complexity?_

    For a balanced BST the runtime is O(log n) because at each step you discard half of the remaining tree. The space complexity is also O(log n) due to the maximum height of the tree defining the maximum number of recursive calls on the stack.


    For an unbalanced BST, the worst-case scenario is that the tree degenerates into something like a linked list, with each node only having a right child or a left child. In this worst case, the time complexity for searching an element would be O(n). The space complexity would also be O(n) due to the maximum depth of the recursive call stack being n.

7. _What’s the “worst” BST structure given the numbers <code>[1,2,3,4,5]</code>, in terms of number of nodes visited to search for the existence of 6?</em>

    If the BST starts with 1 and all the nodes go to the right.


    1 \
  \ \
   2 \
     \ \
      3 \
        \ \
         4 \
           \ \
            5

8. _What’s the “worst” BST structure given the numbers <code>[1,2,3,4,5]</code>, in terms of number of nodes visited, to search for the existence of 0?</em>

    If the BST starts with 5 and all the numbers go to the left


            5 \
       / \
      4 \
     / \
    3 \
   / \
  2 \
 / \
1

9. _What’s the “best” BST structure, given the numbers <code>[1,2,3,4,5,6,7]</code>, in terms of the expected number of nodes visited to search for the existence of an arbitrary positive or negative number?</em>

          4 \
   /     \ \
  2        6 \
 / \        / \ \
1  3     5   7


    —--—--—--—--—--—--—--—--—--—--



##### Binary Tree A

    8

   /  \

  3   10

 / \        \

1   6    14

    / \     /

  4   7 12



10. _If I want to compute the size of each subtree in a tree, which traversal(s) could I use? If some do not work, explain why not. Show how your approach works in **Binary Tree A** from the below section._

    All 3 of the DFS traversals can be used.


    Count the root for each traversal to get the total size.


    Left subtree: 5


    Right subtree: 3


    **Inorder:**


    Left subtree: 1,3,4,6,7


    Right subtree: 10,12,14


    **Preorder:**


    Left subtree: 3,1,6,4,7


    Right subtree: 10,14,12


    **Postorder:**


    Left subtree: 1,4,7,6,3


    Right subtree: 12,14,10

11. _If I wanted to print out the tree node values level by level, which traversal(s) could I use? If some do not work, explain why not. Show how your approach works in **Binary Tree A** from the below section._

    Can use BFS traversal. You visit all the nodes at the current level before moving on to the next level.


    While DFS traversals visit all the nodes in a subtree before moving on to the next subtree so they won’t work.


    Level ordering:


    8


    3, 10


    1, 6, 14


    4, 7, 12

12. _If I wanted to sum all the node values in the tree, which traversal(s) could I use? If some do not work, explain why not. Show how your approach works in **Binary Tree A** from the below section._

    All the traversals can be used


DFS:

Root: 8

Left subtree: 21

Right subtree: 36

Total: 65

**Inorder:**

Root: 8 = 8

Left subtree: 1,3,4,6,7 = 21

Right subtree: 10,12,14 = 36

**Preorder:**

Root: 8 = 8

Left subtree: 3,1,6,4,7 = 21

Right subtree: 10,14,12 = 36

**Postorder:**

Root: 8 = 8

Left subtree: 1,4,7,6,3 = 21

Right subtree: 12,14,10 = 36

**BFS level ordering:**

8 = 8

3, 10 = 13

1, 6, 14 = 21

4, 7, 12 = 23

Total: 65



13. _If I wanted to sum all the node values in each subtree in a tree, which traversal(s) could I use? If some do not work, explain why not. Show how your approach works in **Binary Tree A** from the below section._

    This works the same as question 11. DFS will work. The work is already done in question 12.



### Tree Traversals Orderings

_Give the preorder, postorder, inorder, and level order traversals for each of the following trees. Assume that children are processed left to right._



1. Binary Tree

    1

   /  \

  2   3

 /       \

4        5

          / \

         6   7

               \

                8

**Level order:**

1,

2,3,

4,5,

6,7,

8

**Inorder:**

4,2,

1,

3,6,5,7,8

**Preorder:**

1,

2,4,

3,5,6,7,8

**Postorder:**

4,2,

6,8,7,5,3,

1



2. _N-Ary Tree (Nodes can have more than 2 children)_

              1

          /    |    \

        2     3    4

        /     / |      \

      5    6  7      8

            |          /  \

            9      10   11

                     | \      \

                   12  13  14

**Level order:**

1,

2,3,4,

5,6,7,8,

9,10,11,

12,13,14

**Inorder:**

5,2,

9,6,7,3,

1,

12,10,13,4,8,11,14

**Preorder:**

1,

2,5,

3,6,9,7,

4,8,10,12,13,11,14

**Postorder:**

5,2,

9,6,7,3,

12,13,10,14,11,8,4,

1


### Identifying Recursive Relationships

**Notice:** These exercises are new and quite challenging.

Please ask us on Slack immediately if you have questions about these problems.

Please identify the base case and recurrence relationship for the following relationships in binary trees. For each question, please answer the following.

Treat these more like math problems. Do not worry about having to implement your solutions in Python - we want to focus just on the approach.

Do not use or assume global variables of any kind. If you need to pass information through recursion, please use a helper function with additional arguments to pass this information.



1. **Verify Understanding **- Compute the expected output for all the example trees. Do this manually to verify understanding of the question.
2. **Base Case** - When does the recursion stop?
3. **Recurrence Relation** - How can you solve for the parent using the solution for the children? You can describe this with an equation or in English - whichever is more effective at communicating your approach.
4. **Check Unit Tests.** Double-check your proposed relation works for the examples trees provided. Think of these as test cases - we will be pretty critical if your proposed solution does not work on the provided examples.
5. **N-Ary Extension.** How would this change if you were dealing with an n-ary tree instead of a binary tree? Does the same solution work? If not, what additional changes need to be made?

**Example Binary Trees**


##### Binary Tree A

    8

   /  \

  3   10

 / \        \

1   6    14

    / \     /

  4   7 12

  


##### Binary Tree B

    1

     \

      2

       \

        3

         \

          4

           \

            5


##### Binary Tree C

            1

        /         \

      2           3

     /    \       / \

   4     5     6  7

  / \     / \

8  9  10 11


##### Binary Tree D

       1

     /    \

    2     2

   / \     / \

  4  5  5  4

  


##### Binary Tree E

      1

     /   \

    2     3

   / \       \

  4  5      6

 /              \

10             8

                   \

                    9

**Note:** The height of a binary tree is equal to the maximum number of edges from the root to the most distant leaf node. The height of an empty tree or tree with one node is 0. The height of an individual node is the number of edges from it to the root node.

You may use previous solutions or introduce additional recursive functions to help you solve the problems.

Here is an example of `size(root)` computing the size of a binary tree. Please complete the rest following this format.



1. **Example (i.e. SAMPLE SOLUTION).** ​`size(root)`​ finds the number of nodes in a binary tree. For case A, `size(A) = 9`​ since there are 9 nodes in the tree.
1. `size(B) = 5, size(C) = 11, size(D) = 7, size(E) = 9`
2. Base Case: `if root is None: return 0` in other words `size(None) = 0`​
3. Recurrence Relation: `size(root) = size(left) + size(right) + 1`​
4. Yes: Verified. `size(left/3) = 5, size(right/10) = 3, size(root) = 5+3+1 = 9`​ You should verify all 5 of them. Here `left/3` just identifies the left child is the one with value of `3` and `right/10` identifies the right node has the value ​`10`
5. A similar solution works but instead. `size(root) = 1 + sum(root.child) for each child node`​.
2. ​`sum(root)` finds the sum of all the nodes in the binary tree. `sum(A) = 1+3+8+6+4+&+10+14+12= 65`

    b. base case: 


      if root is None: 


        return 0


    c. recurrence relation: 


      recursive(L) + recursive(R) + root.data


    a, d. Verified: 


      A. L: 1+4+7+6+3 = 21, R: 12+14+10 = 36, rt: 8. Total = 65


      B. L: 0, R: 5+4+3+2 = 14, rt: 1. Total = 15


      C. L: 8+9+4+10+11+5+2 = 49 , R: 6+7+3 = 16 , rt: 1. Total = 66


      D. L: 4+5+2 = 11, R: 5+4+2 = 11, rt: 1. Total = 23


      E. L: 10+4+5+2 = 21, R: 9+8+6+3 = 26, rt: 1. Total = 48


    e. N-ary solution: 


     sum += root.data + sum(root.children)


    f. full code:


    ```
    def sum(root):
      if root is None:
        return 0
      L = sum(root.left)
      R = sum(root.right)
      return L + R + root.data
    ```


3. `max_val(root)`​ finds the maximum value among all nodes in a binary tree. `max_val(A) = 14` since it is the largest element in the tree.

    b. base case:


      if root is None: 


        return 0


    c. recurrence relation: 


      max(root.data, recursive(L, R))


    a, d. Verified: 


      max(root, max(L, R))


      A. max(8, max(7, 14)) = 14


      B. max(1, max(None, 5) = 5


      C. max(1, max(11, 7) = 11


      D. max(1, max(5, 5) = 5


      E. max(1, max(10, 9) = 10


    e. N-ary solution: 


      max(root.data, max(root.children))


      


      for child in root.children:


        maxval = max(maxval, max_val(child))


    f. full code:


    ```
    def max_val(root):
      if root is None:
        return 0
      L = max_val(root.left)
      R = max_val(root.right)
      return max(root.data, max(L, R))
    ```


4. `is_symmetric(root)` returns True if the tree is symmetric and False if it is not. `is_symmetric(A) = False` and `is_symmetric(D) = True`​. A tree is symmetric if the left and right subtrees are mirror images of each other.

    b. base case: 


      if root is None:


        return True


      if ONLY L or ONLY R:


        return False


      if NOT L or R:


        return True


    c. recurrence relation: 


      if L.data == R.data:


        return recursive(L.left, R.right) and recursive(L.right, R.left)


    a, d. Verified: 


      A. False


      B. False


      C. False


      D. True: L: 2,4,5, R: 2,5,4


      E. False


    e. N-ary solution: 


    Like the queue BT solution except the initial queue and queue adding on logic is different. Add all pairs of children of the root to the queue. The children pairs should be the first child and last child. Then next child and 2nd to last child.


    After the base case checking of the popped nodes, do the same thing when adding on to the queue except it's the first child of the left child and the last child of the right node and so on.


    f. full code:


    ```
    def is_symmetric(root):
      # helper
      def is_mirror(left, right):
        if left is None and right is not None:
          return False
        if left is not None and right is None:
          return False
        if left is None and right is None:
          return True
        if left.data == right.data:
          return is_mirror(left.left, right.right) and is_mirror(left.right, right.left)
        return False

      # is_symmetric base code
      if root is None:
        return True
      else:
        return is_mirror(root.left, root.right)

    # queue
    # Standard level order traversal
    # Base cases checked after popping the tuple of left and right subtrees from queue
    def is_symmetric_queue(root):
      if root is None:
        return True
      queue = [(root.left, root.right)]
      while queue:
        left, right = queue.pop(0)
        if left is None and right is None:
          continue
        if left is None or right is None:
          return False
        if left.data != right.data:
          return False
        queue.append((left.left, right.right))
        queue.append((left.right, right.left))
      return True
    ```


5. `height(root)`​ finds the height of the tree. The distance from the root to the lowest child. `height(A) = 3`​ because `12` is 3 levels down from the 8.

    b. base case: 


      # For a tree with a single node (the root), there are no edges, so the height is 0. So for an empty tree, the height is -1.


      if root is None: 


        return -1


    c. recurrence relation: 


      max(recursive(L), recursive(R)) + 1


    a, d. Verified: 


      A. (L = 2, R = 2) + 1 = 3


      B. (L = 0, R = 3) + 1 = 4


      C. (L = 2, R = 1) + 1 = 3


      D. (L = 1, R = 1) + 1 = 2


      E. (L = 2, R = 3) + 1 = 4


    e. N-ary solution: 


      # height is one more than the max height of any subtree


      max_height = max(max_height, height(root.children)) + 1


    f. full code:


    ```
    def height(root):
      if root is None:
        return -1
      L = height(root.left)
      R = height(root.right)
      return max(L, R) + 1
    ```


6. The diameter of a binary tree is the length of the longest path between any two nodes in the tree. **This path may or may not pass through the root of the tree.** `diameter(root)` finds the diameter of this tree. `diameter(A) = 6` because the path from `4` or `7` to `12` has length 6.

    b. base case: 


      if root is None:


        return 0


    c. recurrence relation: 


        max_diameter = max(self.max_diameter, _recursive_depth(L) + _recursive_depth(R))


    a, d. Verified: 


      A. 6 (4 or 7 to 12)


      B. 4 (5 to 1)


      C. 5 (8, 9, 10, 11 to 6 or 7)


      D. 4 (4 or 5 to 5 or 4)


      E. 7 (10 to 9)


    e. N-ary solution:


    Have 2 max variables for the top highest value height/depth


    Go through each child, get the recursive height/depth.


    If the recursive height is larger than either of the maxes, overwrite them


    When getting the max diameter, do a max of that variable or the sum of the two max heights


    Since we already know what is the current max height is in the larger max variable, can return that [+ 1]


    f. full code:


    ```
    class Diameter:
      def __init__(self):
        # stores the maximum diameter calculated
        self.max_diameter = 0

      def depth(self, node) -> int:
        if node is None:
          return 0
        L = self.depth(node.left)
        R = self.depth(node.right)
        # Calculate diameter
        self.max_diameter = max(self.max_diameter, L + R)
        # Make sure the parent node(s) get the correct depth from this node
        return max(L, R) + 1

      def calc(self, root) -> int:
        self.depth(root)
        return self.max_diameter
    ```


7. `leafs(root)`​ calculates the number of leaves in a binary tree. `leafs(A)=4`​ because `1,4,7,12`​ are all leaf nodes. Recall leaf nodes are nodes with no children.

    b. base case: 


       if root is None:


        return 0


      if L and R are None:


        return 1


    c. recurrence relation: 


      recursive(L) + recursive(R)


    a, d. Verified: 


      A. L: 3 (1, 4, 7), R: 1 (12) = 4


      B. L: 0, R: 1 (5) = 1


      C. L: 4 (8, 9, 10, 11), R: 2 (6, 7) = 6


      D. L: 2 (4, 5), R: 2 (5, 4) = 4


      E. L: 2 (10, 5), R: 1 (9) = 3


    e. N-ary solution:


      if len(root.children) == 0:


        return 1


      return sum(leafs(child) for child in root.children)


    f. full code:


    ```
    def leafs(root):
      if root is None:
        return 0
      if root.left is None and root.right is None:
        return 1
      L = leafs(root.left)
      R = leafs(root.right)
      return L + R
    ```


8. `top_ordered(root)`​ returns True if the root of every subtree is the smallest element in its subtree. `top_ordered(E) = True` because every Node, it is smaller than the elements in its subtree. `top_ordered(A) = False` because `3` is larger than its left child of `1`​.

    b, c. base case + recurrence relation


      if root is None:


        return False


      if L and R:


        True if root.data is &lt; than L.data and R.data


      if L only:


        True if root.data &lt; L.data


      if R only:


        True if root.data &lt; R.data


      return recursive(L) and recursive(R)


    a, d. Verified: 


    (root &lt; root.left and root &lt; root.left)


      A. False (Root: 8 &lt; 3,10. False)


      B. True (Root: 1 &lt; 2. Right: 2 &lt; 3 &lt; 4 &lt; 5)


      C. True (Root: 1 &lt; 2,3. Left: 2 &lt; 4,5. 4 &lt; 8,9. 5 &lt; 10,11. Right: 3 &lt; 6,7)


      D. True (Root: 1 &lt; 2,2. Left: 2 &lt; 4,5. Right: 2 &lt; 5,4)


      E. True (Root: 1 &lt; 2,3. Left: 2 &lt; 4,5, 4 &lt; 10. Right: 3 &lt; 6 &lt; 8 &lt; 9)


    e. N-ary solution: 


    partial pseudocode:


      for child in root.children:


        if child.val &lt; root.val or not is_top_ordered(child):


          return False


    f. full code:


    ```
    def top_ordered(root):
      if root is None:
        return False
      if root.left and root.right:
        if root.data < root.left.data and root.data < root.right.data:
          return True
        else:
          return False
      if root.left and root.right is None:
        if root.data < root.left.data:
          return True
        else:
          return False
      if root.right and root.left is None:
        if root.data < root.right.data:
          return True
        else:
          return False
      L = top_ordered(root.left)
      R = top_ordered(root.right)
      return L and R
    ```


9. `find_height(root, height)` determines the number of nodes that have height `height`​. `find_height(A, 2) = 3` because of `1,6,14` are the nodes with height `2`​. `find_height(any non empty tree, 0) = 1` because it will be just the root (assuming the tree is not empty)

    b. base case: 


      if root is None:


        return 0


    c. recurrence relation: 


    Do a level order traversal. Pass along a height to the queue.


      queue: add root and 0 (height)


      while there is something in the queue:


        do FIFO for queue to get root and height


        check if the node is valid


          if the queue's height matches the height to find, iterate counter


          append the left and right nodes and add 1 to the heights (because these children are on the next level) to the queue


    a, d. Verified: 


      A. find_height(root, 1) = 2 (3, 10)


      B. find_height(root, 1) = 1 (2)


      C. find_height(root, 1) = 2 (2, 3)


      D. find_height(root, 1) = 2 (2, 2)


      E. find_height(root, 1) = 2 (2, 3)


      A. find_height(root, 2) = 3 (1, 6, 14)


      B. find_height(root, 2) = 1 (3)


      C. find_height(root, 2) = 4 (4, 5, 6, 7)


      D. find_height(root, 2) = 4 (4, 5, 5, 4)


      E. find_height(root, 2) = 3 (4, 5, 6)


      A. find_height(root, 3) = 3 (4, 7, 12)


      B. find_height(root, 3) = 1 (4)


      C. find_height(root, 3) = 4 (8, 9, 10, 11)


      D. find_height(root, 3) = 0


      E. find_height(root, 3) = 2 (10, 8)


    e. N-ary solution: 


    Same as the binary tree except when adding to the queue in the loop there isnt just left and right child like:


    for child in root.children:


      queue.put((child, h + 1))


    f. full code:


    ```
    def find_height(root, height):
      if root is None:
        return 0
      num_nodes = 0
      queue = Queue()
      queue.put((root, 0))
      while queue.empty() is False:
        node, h = queue.get()
        if node is not None:
          if h == height:
            num_nodes += 1
          queue.put((node.left, h + 1))
          queue.put((node.right, h + 1))
      return num_nodes
    ```


10. `sum_only_child_parents(root)` determines the sum of nodes with exactly one child. `sum_only_child_parents(A) = 24` because `10,14` are the nodes with one child, and their sum if `24`.

    b. base case: 


      if root is None:


        return 0


    c. recurrence relation: 


      if only L or only R:


        return recursive(L) + recursive(R) + root.data


      else:


        return recursive(L) + recursive(R)


    a, d. Verified: 


      A. L: 0, R: 10 + 14 = 24


      B. L: 0, R: 2 + 3 + 4, root: 1 = 10


      C. L: 0, R: 0 = 0


      D. L: 0, R: 0 = 0


      E. L: 4, R: 3 + 6 + 8 = 21


    e. N-ary solution:


    # If the root children is 1, add on the root data to the ongoing sum.


    # Iterate through each child and recursively run


    # This is basically same as sum_only_child except getting the root/parent value


      psuedocode:


      child_count = sum(1 for child in root.children if child is not None)


      if child_count == 1:


        sum += root.data


      for child in root.children:


        sum += sum_only_child_parents(child)


    f. full code:


    ```
    def sum_only_child_parents(root):
      if root is None:
        return 0
      if (root.left is None and root.right is not None) or (root.left is not None and root.right is None):
        L = sum_only_child_parents(root.left)
        R = sum_only_child_parents(root.right)
        return L + R + root.data
      else:
        L = sum_only_child_parents(root.left)
        R = sum_only_child_parents(root.right)
        return L + R
    ```


11. `sum_only_child(root)` determines the sum of all nodes that do not have a sibling node. ​`sum_only_child(A) = 34 `because `8,14,12` are the nodes without siblings, and their sum if `35`. The root does not have a sibling node and is an "only child" node.

    b. base case: 


      if root is None: 


        return 0


    c. recurrence relation: 


      if ONLY L:


        return recursive(L) + L.data + root.data if root


      if ONLY R:


        return recursive(R) + R.data +  + root.data if root


      # if there are 2 children


      else:


        return recursive(L) + recursive(R) + root.data if root


    a, d. Verified: 


      A. L: 0, R: 14 + 12, root: 8 = 34


      B. L: 0, R: 2 + 3 + 4 + 5, root: 1 = 15


      C. L: 0, R: 0, root: 1 = 1


      D. L: 0, R: 0, root: 1 = 1


      E. L: 10, R: 6 + 8 + 9, root: 1 = 34


    e. N-ary solution: 


      # If root children is 1, add on the root data to the ongoing sum.


      # Otherwise continue the recursion without


      # code would need to do a sum += most likely not just return


      # This is basically same as sum_only_child_parent except getting the child value


      psuedocode:


      child_count = sum(1 for child in root.children if child is not None)


        if child_count == 1:


            sum(sum_only_child_parents(child) for child in root.children) + root.child.data


        else:


            sum(sum_only_child_parents(child) for child in root.children)


    f. full code:


    ```
    def sum_only_child(root, is_root = True):
      def helper(root, is_root = False):
        if root is None:
          return 0
        if_root = root.data if is_root else 0
        if root.left is None and root.right is not None:
          return helper(root.right) + root.right.data + if_root
        elif root.left is not None and root.right is None:
          return helper(root.left) + root.left.data + if_root
        else:
          return helper(root.left) + helper(root.right) + if_root
      return helper(root, is_root)

    ```


12. `level_min(root, height)`​ determines the node of minimum value ​`height` equal to the given height. `level_min(A, 0) = 8,level_min(A,1) = 3, level_min(A,2) = 1`

    b. base case: 


      if root is None:


        return 0


    c. recurrence relation: 


      queue: add root and 0 (level)


      while there is something in the queue:


        do FIFO for queue to get root and level


        check if the node is valid


          if the height matches the level and the current node value is the smallest so far, update a minimum node value


          append the left and right nodes and add 1 to the heights (because these children are on the next level) to the queue


    a, d. Verified: 


      A. level_min(root, 2): min(1, 6, 14) = 1


      B. level_min(root, 2): min(3) = 3


      C. level_min(root, 2): min(4, 5, 6, 7) = 4


      E. level_min(root, 2): min(4, 5, 5, 4) = 4


      D. level_min(root, 2): min(4, 5, 6) = 4


    e. N-ary solution:


      # when the height_counter is less than the height, recursively get the minimal value. pseudocode:


      min_val = min([level_min(child, height, height_counter + 1, min_val) for child in root.children])


    f. full code:


    ```
    def level_min(root, height):
      if root is None:
        return 0
      min_node = float('inf')
      queue = Queue()
      queue.put((root, 0))
      while queue.qsize() > 0:
        node, h = queue.get()
        if node is not None:
          if h == height and node.data < min_node:
            min_node = node.data
          queue.put((node.left, h + 1))
          queue.put((node.right, h + 1))
      return min_node

    ```


13. `full(root)` determines if a binary tree is `full`​. A binary tree is said to be `full` if every node has `0 or 2` children. `full(D) = True, full(A) = False`

    b. base case: 


      if root is None:


        return True


    c. recurrence relation: 


      # check if there are 2 children or no children


      if (both L and R) or (both not L and not R):


        return recursive(L) and recursive(R)


      elif L or R aka one child:


        return False


    a, d. Verified: 


      A. L: True. R: 10, 14, have one child only. False.


      B. root: 1 has one child. R: 2, 3, 4 have one child. False.


      C. L: All 0 or 2 children. R: All 0 or 2 children. True.


      D. L: All 0 or 2 children. R: All 0 or 2 children. True.


      E. L: 4 has one child. R: 3, 6, 8 have one child. False.


    e. N-ary solution:


      - Check if length of tree children are 0 or the amt we are looking for.


        - For example, this could be whichever subtree has the most children which would have to be calculated


        - If the length is 0 or it's whatever amt of children we determine to make it "full" then:


          - iterate through all children of root and recursively run the function


      psuedocode:


      if len(root.children) == 0 or len(root.children) == num_of_children_making_it_full:


        return all(recursive(child, num_of_children_making_it_full) for child in root.children)


    f. full code:


    ```
    def full(root):
      if root is None:
        return True
      both = root.left is not None and root.right is not None
      neither = root.left is None and root.right is None
      if both or neither:
        L = full(root.left)
        R = full(root.right)
        return L and R
      elif root.left or root.right:
        return False
    ```


14. ​`same(root_a, root_b)`​ returns True if `root_a` and `root_b` represent the same binary tree and False otherwise. Your recurrence will require you to use both `root_a, root_b` as inputs. `same(A, A) = True, same(A,B) = False`​

    aka same(A, B)


    b. base case: 


      if A is None and B is None:


        return True


    c. recurrence relation: 


      if A and B


        return (A.data == B.data) and same(A.left, B.left) and same(A.right, B.right)


    a, d. Verified: 


    verified


    e. N-ary solution:


      # go through all the children of the two N-arys and check if all the children are the same value (base case) and verify the amt of children are the same. Zip changes each item in each iterator into a tuple.


      if A.value != B.value or len(A.children) != len(B.children):


        return False


      for a_child, b_child in zip(A.children, B.children)


        if not same(A.a_child, b_child):


          return False


      return True


    f. full code:


    ```
    def same(root_a, root_b):
      if root_a is None and root_b is None:
        return True
      if root_a is not None and root_b is not None:
        L = same(root_a.left, root_b.left)
        R = same(root_a.right, root_b.right)
        return (root_a.data == root_b.data) and L and R
      return False
    ```


15. **Challenge Question. `almost_same(root_a, root_b, k)`**​ returns True if `root_a` and `root_b` represent the same binary tree except the `k` of the values can be different. Suppose we're using example A. If `k=1`​ then you can replace the value of the root in ​`A`​ to `20` instead of `8`. We have a modified version of `A` call this ​`Z`​ , then you would have `almost_same(A, Z, 1) = True`​ but `almost_same(A, Z, 0) = False` . The latter is False because A differs from Z in the root value. If the tree structure is any different, i.e. you find None in one tree at the same position as a Node in the other tree, then return False. If `k = 0` , then the output should be equivalent to `same`​ function in the previous problem. Namely, `almost_same(root_a, root_b,0) == same(root_a, root_b)` .

    aka almost_same(A, B)


    b. base case: 


      if not A and not B:


        return True, k


      if not A or not B:


        return False, k


    c. recurrence relation:


      # if the values for each BT dont match, decrement k by 1 and check if k has fallen below 0. If so, then too many differences and return false


      # return both left recursively and both right recursively


      if A.data != B.data:


        k -= 1


        if k &lt; 0:


          return False, k


      return recursive(A.left, B.left, k) and recursive(A.right, B.right, k), k


    a, d. Verified: 


      changed 1, 2, and 3 integers for the binary tree examples


    e. N-ary solution: 


    # go through all the children of the two N-arys recursively via zip iterating


    # same check of if the data isnt the same, decrement and check the difference counter


    # verify the amt of children are the same


      if A.data != B.data:


        k -= 1


        if k &lt; 0:


          return False, k


      if len(A.children) != len(B.children):


        return False, k


      for child_a, child_b in zip(A.children, B.children):


        result, k = almost_same(child_a, child_b, k)


        if not result:


          return False, k


      return True, k


    f. full code:


    ```
    def almost_same(root_a, root_b, k):
      if root_a is None and root_b is None:
        return True, k
      if root_a is None or root_b is None:
        return False, k
      if root_a.data != root_b.data:
        k -= 1
        if k < 0:
          return False, k
      L, k = almost_same(root_a.left, root_b.left, k)
      R, k = almost_same(root_a.right, root_b.right, k)
      return L and R, k

    # wrong without passing k around
    def almost_same(root_a, root_b, k):
      if root_a is None and root_b is None:
        return True
      if root_a is None or root_b is None:
        return False
      if root_a.data != root_b.data:
        k -= 1
        if k < 0:
          return False
      L = almost_same(root_a.left, root_b.left, k)
      R = almost_same(root_a.right, root_b.right, k)
      return L and R

    ```



### **Tries**


#### General



1. _What is a trie?_

    A trie is an n-ary tree data structure used for storing and searching strings over an alphabet.

2. _When do we use a trie?_

    autocomplete


    spell checkers


    IP routing (Longest prefix matching routing)

3. _How do we know that “dog” is an actual word in our trie and is not just a prefix of the word “doghouse”?_

    If the “g” points to some sort of existing word boolean that is True

4. _Suppose our dictionary has n words and the longest of them is m characters long. What is the time and space complexity of building our trie?_

    O(n * m). Worst case, we have to iterate through each character of each word to insert it into the Trie.



#### Building a Trie



1. _Start with an empty trie and insert the words <code>"hello", "help", "held", "helden", "helderman", "helping"</code>​ into this trie. Draw the resulting trie in tree structure.</em>

                                                       h


                                                       e


                                                       l


                                                d^    l      p^ 


                                                e    o^     i


                                              n^    r       n


                                                     m      g^


                                                     a


                                                     n^


    ^ = existing word

2. _Trace through how you would search for <code>"helping"</code> in this trie.</em>

    Go through each character and follow each path: h -> e -> l -> p -> i -> n -> g. Now check if there’s a boolean for the word existing flag which there is.

3. _Trace how you would find all words starting with the prefix ​<code>"he"</code> in this Trie.</em>

Traversing through every word:

h -> e -> l -> l -> o^

h -> e -> l -> p^

h -> e -> l -> d^

h -> e -> l -> d -> e -> n^

h -> e -> l -> d -> e -> r -> m -> a -> n

h -> e -> l -> p -> i -> n -> g
