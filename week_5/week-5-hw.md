Identifying Recursive Relationships

2. sum
a. 

b. base case: 
  if root is None: return 0

c. recurrence relation: 
  sum(root) = sum(L) + sum(R) + root.data

d. Verified: 
  A. L: 1+4+7+6+3 = 21, R: 12+14+10 = 36, rt: 8. Total = 65
  B. L: 0, R: 5+4+3+2 = 14, rt: 1. Total = 15
  C. L: 8+9+4+10+11+5+2 = 49 , R: 6+7+3 = 16 , rt: 1. Total = 66
  D. L: 4+5+2 = 11, R: 5+4+2 = 11, rt: 1. Total = 23
  E. L: 10+4+5+2 = 21, R: 9+8+6+3 = 26, rt: 1. Total = 48

e. N-ary solution: 
 root + sum(root.child)


3. max_val
a. 

b. base case:
  if root is None: return 0

c. recurrence relation: 
  max_val(root) = max(root.data, max(L, R))

d. Verified: 
  A. max(8, max(7,14)) = 14
  B. max(1, max(None,5) = 5
  C. max(1, max(11, 7) = 11
  D. max(1, max(5, 5) = 5
  E. max(1, max(10, 9) = 10

e. N-ary solution: 
  max(root.data, max(root.children))


4 is_symmetric
a. 

b. base case: 
  if root is None: return False

c. recurrence relation: 
  is_symmetric(root) = preorder_traversal(L) == reverse_preorder_traversal(R)

d. Verified: 
  A. 
  B. 
  C. 
  D. 
  E. 

e. N-ary solution: 
  pass


5. height
a. 

b. base case: 
  # if root is None: return 0
  if root is None: return -1

c. recurrence relation: 
  height(root) = max(height(L), height(R)) + 1

d. Verified: 
  A. (L = 2, R = 2) + 1 = 3
  B. (L = 0, R = 3) + 1 = 4
  C. (L = 2, R = 1) + 1 = 3
  D. (L = 1, R = 1) + 1 = 2
  E. (L = 2, R = 3) + 1 = 4

e. N-ary solution: 
  max(height(root.children)) + 1


6 diameter
a. 

b. base case: 
  if root is None: return 0

c. recurrence relation: 
    diameter(root) = max(diameter(L), diameter(R)) + 1
    return diameter(L) + diameter(R)

d. Verified: 
  A. 6
  B. 4
  C. 5
  D. 4
  E. 7

e. N-ary solution: 
  sum(root.child)


7 leafs
a. 

b. base case: 
   if root is None:
    return 0
  if root.left is None and root.right is None:
    return 1

c. recurrence relation: 
  leaf(L) + leaf(R)

d. Verified: 
  A. L: 3, R: 1 = 4
  B. L: 0, R: 1 = 1
  C. L: 4, R: 2 = 6
  D. L: 2, R: 2 = 4
  E. L: 2, R: 1 = 3

e. N-ary solution: 
  sum(leaf(root.children))


8. top_ordered
a. 

b. base case: 
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

c. recurrence relation: 
  top_ordered(L) and top_ordered(R)

d. Verified: 
  A. False
  B. True
  C. True
  D. True
  E. True

e. N-ary solution: 
  pass


9. find_height
a. 

b. base case: 
  if root is None:
    return 0

c. recurrence relation: 
def find_height(root, height):
  if root is None:
    return 0
  num_nodes = 0
  queue = Queue()
  queue.put([root, 0])
  while queue.empty() is False:
    arr = queue.get()
    node = arr[0]
    h = arr[1]
    if node is not None:
      if h == height:
        num_nodes += 1
      queue.put([node.left,h+1])
      queue.put([node.right,h+1])
  return num_nodes

d. Verified: 
  A. find_height(root, 2) = 3 (1, 6, 14)
  B. find_height(root, 2) = 1 (3)
  C. find_height(root, 2) = 4 (4,5,6,7)
  D. find_height(root, 2) = 4 (4,5,5,4)
  E. find_height(root, 2) = 3 (4,5,6)

e. N-ary solution: 
  for child in root:
    queue.put([child, h+1])



10. sum _only_child_parents
a. 

b. base case: 
  if root is None:
    return 0
  if (root.left is None and root.right is not None) or (root.left is not None and root.right is None):
    return sum_only_child_parents(root.left) + sum_only_child_parents(root.right) + root.data

c. recurrence relation: 
  L = sum_only_child_parents(root.left)
  R = sum_only_child_parents(root.right)
  return L + R

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


11. sum_only_child
a. 

b. base case: 
  if root is None: return False

c. recurrence relation: 
  pass

d. Verified: 
  A. L: 0, R: 14 + 12, root: 8 = 34
  B. L: 0, R: 2 + 3 + 4 + 5, root: 1 = 15
  C. L: 0, R: 0, root: 1 = 1
  D. L: 0, R: 0, root: 1 = 1
  E. L: 10, R: 6 + 8 + 9, root: 1 = 34

e. N-ary solution: 
  pass


12. level_min
a. 

b. base case: 
  if root is None: return False

c. recurrence relation: 
  pass

d. Verified: 
  A. level_min(root, 2): min(1, 6, 14) = 1
  B. level_min(root, 2): min(3) = 3
  C. level_min(root, 2): min(4, 5, 6, 7) = 4
  E. level_min(root, 2): min(4, 5, 5, 4) = 4
  D. level_min(root, 2): min(4, 5, 6) = 4

e. N-ary solution: 
  pass


13. full
a. 

b. base case: 
  if root is None: return False

c. recurrence relation: 
  pass

d. Verified: 
  A. 
  B. 
  C. 
  D. 
  E. 

e. N-ary solution: 
  if root is None:
      return True
  if len(root.children) == 0 or len(root.children) == n:
      return all(full_n_ary(child, n) for child in root.children)
  return False


14. same(root_a, root_b)
a. 

b. base case: 
  if root_a is None and root_b is None:
    return True

c. recurrence relation: 
  if root_a is not None and root_b is not None:
    L = same(root_a.left, root_b.left)
    R = same(root_a.right, root_b.right)
    return (root_a.data == root_b.data) and L and R

d. Verified: 
  A. 
  B. 
  C. 
  D. 
  E. 

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


15. almost_same(root_a, root_b)
a. 

b. base case: 
  if root is None: return False

c. recurrence relation: 
  pass

d. Verified: 
  A. 
  B. 
  C. 
  D. 
  E. 

e. N-ary solution: 
  pass
