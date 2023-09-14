Identifying Recursive Relationships

2. sum
a. 

b. base case: 
  if root is None: 
    return 0

c. recurrence relation: 
  recursive(L) + recursive(R) + root.data

d. Verified: 
  A. L: 1+4+7+6+3 = 21, R: 12+14+10 = 36, rt: 8. Total = 65
  B. L: 0, R: 5+4+3+2 = 14, rt: 1. Total = 15
  C. L: 8+9+4+10+11+5+2 = 49 , R: 6+7+3 = 16 , rt: 1. Total = 66
  D. L: 4+5+2 = 11, R: 5+4+2 = 11, rt: 1. Total = 23
  E. L: 10+4+5+2 = 21, R: 9+8+6+3 = 26, rt: 1. Total = 48

e. N-ary solution: 
 root + sum(root.child)
f. full code:
def sum(root):
  if root is None:
    return 0
  L = sum(root.left)
  R = sum(root.right)
  return L + R + root.data


3. max_val
a. 

b. base case:
  if root is None: 
    return 0

c. recurrence relation: 
  max(root.data, recursive(L, R))

d. Verified: 
  max(root, max(L, R))
  A. max(8, max(7, 14)) = 14
  B. max(1, max(None, 5) = 5
  C. max(1, max(11, 7) = 11
  D. max(1, max(5, 5) = 5
  E. max(1, max(10, 9) = 10

e. N-ary solution: 
  max(root.data, max(root.children))
  ```
  def max_val(root):
    if root is None:
        return 0

    maxval = 0
    for child in root.children:
      maxval = max(maxval, max_val(child))
    return maxval
  ```

f. full code:
def max_val(root):
  if root is None:
    return 0
  L = max_val(root.left)
  R = max_val(root.right)
  return max(root.data, max(L, R))


4 is_symmetric
a. 

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

d. Verified: 
  A. False
  B. False
  C. False
  D. True: L: 2,4,5, R: 2,5,4
  E. False

e. N-ary solution: 
# we start by adding all pairs of children of the root to the queue. Then, for each pair of nodes, we add their children to the queue in a symmetric manner: the first child of the left node with the last child of the right node, the second child of the left node with the second-to-last child of the right node, and so on.
def is_symmetric(root):
  if root is None:
      return True
  queue = [(child, root.children[-i-1]) for i, child in enumerate(root.children)]
  while queue:
      left, right = queue.pop(0)
      if left is None and right is None:
          continue
      if left is None or right is None:
          return False
      if left.data != right.data:
          return False
      queue.extend((left_child, right.children[-i-1]) for i, left_child in enumerate(left.children))
  return True

f. full code: 
def is_symmetric(root):
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
  
  if root is None:
    return True
  else:
    return is_mirror(root.left, root.right)


5. height
a. 

b. base case: 
  # For a tree with a single node (the root), there are no edges, so the height is 0. So for an empty tree, the height is -1.
  if root is None: 
    return -1

c. recurrence relation: 
  max(recursive(L), recursive(R)) + 1

d. Verified: 
  A. (L = 2, R = 2) + 1 = 3
  B. (L = 0, R = 3) + 1 = 4
  C. (L = 2, R = 1) + 1 = 3
  D. (L = 1, R = 1) + 1 = 2
  E. (L = 2, R = 3) + 1 = 4

e. N-ary solution: 
  max(height(root.children)) + 1
f. full code:
def height(root):
  if root is None:
    return -1
  L = height(root.left)
  R = height(root.right)
  return max(L, R) + 1


6 diameter
a. 

b. base case: 
  if root is None:
    return 0

c. recurrence relation: 
    max_diameter = max(self.max_diameter, _recursive_depth(L) + _recursive_depth(R))

d. Verified: 
  A. 6 (4 or 7 to 12)
  B. 4 (5 to 1)
  C. 5 (8, 9, 10, 11 to 6 or 7)
  D. 4 (4 or 5 to 5 or 4)
  E. 7 (10 to 9)

e. N-ary solution: 
  sum(root.child)
f. full code:
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


7 leafs
a. 

b. base case: 
   if root is None:
    return 0
  if L and R are None:
    return 1

c. recurrence relation: 
  recursive(L) + recursive(R)

d. Verified: 
  A. L: 3 (1, 4, 7), R: 1 (12) = 4
  B. L: 0, R: 1 (5) = 1
  C. L: 4 (8, 9, 10, 11), R: 2 (6, 7) = 6
  D. L: 2 (4, 5), R: 2 (5, 4) = 4
  E. L: 2 (10, 5), R: 1 (9) = 3

e. N-ary solution: 
  sum(leaf(root.children))


8. top_ordered
a. 

b, c. base case + recurrence relation
  if root is None:
    return False

  if L and R:
    True if root.data is < than L.data and R.data
  if L only:
    True if root.data < L.data
  if R only:
    True if root.data < R.data

  return recursive(L) and recursive(R)

d. Verified: 
(root < root.left and root < root.left)
  A. False (Root: 8 < 3,10. False)
  B. True (Root: 1 < 2. Right: 2 < 3 < 4 < 5)
  C. True (Root: 1 < 2,3. Left: 2 < 4,5. 4 < 8,9. 5 < 10,11. Right: 3 < 6,7)
  D. True (Root: 1 < 2,2. Left: 2 < 4,5. Right: 2 < 5,4)
  E. True (Root: 1 < 2,3. Left: 2 < 4,5, 4 < 10. Right: 3 < 6 < 8 < 9)

e. N-ary solution: 
  pass
f. full code:
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


9. find_height
a. 

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

d. Verified: 
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
  for child in root:
    queue.put([child, h+1])

f. full code:
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


10. sum_only_child_parents
a. 

b. base case: 
  if root is None:
    return 0

c. recurrence relation: 
  if only L or only R:
    return recursive(L) + recursive(R) + root.data
  else:
    return recursive(L) + recursive(R)

d. Verified: 
  A. L: 0, R: 10 + 14 = 24
  B. L: 0, R: 2 + 3 + 4, root: 1 = 10
  C. L: 0, R: 0 = 0
  D. L: 0, R: 0 = 0
  E. L: 4, R: 3 + 6 + 8 = 21

e. N-ary solution: 
  child_count = sum(1 for child in root.children if child is not None)
  if child_count == 1:
      return sum(sum_only_child_parents(child) for child in root.children) + root.data
  return sum(sum_only_child_parents(child) for child in root.children)

f. full code: 
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


11. sum_only_child
a. 

b. base case: 
  if root is None: 
    return 0

c. recurrence relation: 
  if ONLY L:
    return recursive(R) + R.data + root.data if root
  if ONLY R:
    return recursive() + L.data +  + root.data if root
  # if there are 2 children
  else:
    return recursive(L) + recursive(R) + root.data if root

d. Verified: 
  A. L: 0, R: 14 + 12, root: 8 = 34
  B. L: 0, R: 2 + 3 + 4 + 5, root: 1 = 15
  C. L: 0, R: 0, root: 1 = 1
  D. L: 0, R: 0, root: 1 = 1
  E. L: 10, R: 6 + 8 + 9, root: 1 = 34

e. N-ary solution: 
  pass

f. full code:
def sum_only_child(root, is_root = True):
  if root is None:
    return 0
  
  if_root = 0
  if is_root:
    if_root = root.data
  
  if root.left is None and root.right is not None:
    return sum_only_child(root.left, False) + sum_only_child(root.right, False) + root.right.data + if_root
  elif root.left is not None and root.right is None:
    return sum_only_child(root.left, False) + sum_only_child(root.right, False) + root.left.data + if_root
  else:
    return sum_only_child(root.left, False) + sum_only_child(root.right, False) + if_root


12. level_min
a. 

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


d. Verified: 
  A. level_min(root, 2): min(1, 6, 14) = 1
  B. level_min(root, 2): min(3) = 3
  C. level_min(root, 2): min(4, 5, 6, 7) = 4
  E. level_min(root, 2): min(4, 5, 5, 4) = 4
  D. level_min(root, 2): min(4, 5, 6) = 4

e. N-ary solution: 
  pass

f. full code:
def level_min(root, height):
  if root is None:
    return 0
  min_node = float('inf')
  queue = Queue()
  queue.put((root, 0))
  while queue.empty() is False:
    node, h = queue.get()
    if node is not None:
      if h == height and node.data < min_node:
        min_node = node.data
      queue.put((node.left, h + 1))
      queue.put((node.right, h + 1))
  return min_node


13. full
a. 

b. base case: 
  if root is None:
    return True

c. recurrence relation: 
  # check if there are 2 children or no children
  if (both L and R) or (both not L and not R):
    return recursive(L) and recursive(R)
  elif L or R aka one child:
    return False

d. Verified: 
  A. L: True. R: 10, 14, have one child only. False.
  B. root: 1 has one child. R: 2, 3, 4 have one child. False.
  C. L: All 0 or 2 children. R: All 0 or 2 children. True.
  D. L: All 0 or 2 children. R: All 0 or 2 children. True.
  E. L: 4 has one child. R: 3, 6, 8 have one child. False.

e. N-ary solution: 
  if root is None:
      return True
  if len(root.children) == 0 or len(root.children) == n:
      return all(full_n_ary(child, n) for child in root.children)
  return False

f. full code:
def full(root):
  if root is None:
    return True
  if (root.left is not None and root.right is not None) or (root.left is None and root.right is None):
    L = full(root.left)
    R = full(root.right)
    return L and R
  elif root.left or root.right:
    return False


14. same(root_a, root_b)
aka same(A, B)
a. 

b. base case: 
  if A is None and B is None:
    return True

c. recurrence relation: 
  if A and B
    return (A.data == B.data) and same(A.left, B.left) and same(A.right, B.right)

d. Verified: 
verified

e. N-ary solution: 
  if root_a is None and root_b is None:
    return True
  if root_a is not None and root_b is not None:
    if root_a.value != root_b.value or len(root_a.children) != len(root_b.children):
      return False
    for i in range(len(root_a.children)):
      if not same(root_a.children[i], root_b.children[i]):
        return False
    return True
  return False

f. full code:
def same(root_a, root_b):
  if root_a is None and root_b is None:
    return True
  if root_a is not None and root_b is not None:
    L = same(root_a.left, root_b.left)
    R = same(root_a.right, root_b.right)
    return (root_a.data == root_b.data) and L and R
  return False


15. almost_same(root_a, root_b)
aka almost_same(A, B)
a. 

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
    if k < 0:
      return False, k
  return recursive(A.left, B.left, k) and recursive(A.right, B.right, k), k

d. Verified: 
  changed 1, 2, and 3 integers for the binary tree examples

e. N-ary solution: 
  pass

f. full code:
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
