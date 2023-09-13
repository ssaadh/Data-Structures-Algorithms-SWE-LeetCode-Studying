from queue import Queue

## 1. size
def size(root):
  if root is None:
    return 0
  L = size(root.left)
  R = size(root.right)
  return L + R + 1


# 2. sum
def qsum(root):
  if root is None:
    return 0
  L = qsum(root.left)
  R = qsum(root.right)
  return L + R + root.data


# 3. max_val
def max_val(root):
  if root is None:
    return 0
  L = max_val(root.left)
  R = max_val(root.right)
  return max(root.data, max(L, R))


# 4. is_symmetric
# straight up
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

# queue
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


# 5. height
def height(root):
  # 0 or -1?
  if root is None:
    return -1
  L = height(root.left)
  R = height(root.right)
  return max(L, R) + 1


# 6. diameter
class Diameter:
  def __init__(self):
    # maximum diameter calculated thus far
    self.max_diameter = 0
    
  def depth(self, node) -> int:
    if node is None:
      return -1
    
    L = self.depth(node.left)
    R = self.depth(node.right)    
    # Calculating diameter
    self.max_diameter = max(self.max_diameter, 2 + L + R)
    # Returning the height.
    # Make sure the parent gets the correct depth from this node
    return max(L, R) + 1
  
  def calc(self, root) -> int:
    self.depth(root)
    return self.max_diameter

def diameter(root):
  clas = Diameter()
  return clas.calc(root)


# 7. leafs
def leafs(root):
  if root is None:
    return 0
  if root.left is None and root.right is None:
    return 1
  L = leafs(root.left)
  R = leafs(root.right)
  return L + R


# 8. top_ordered
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


# 9. find_height
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


# 10. sum_only_child_parents
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


# 11. sum_only_child
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


# 12. level_min
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


# 13. full
def full(root):
  if root is None:
    return True
  if (root.left is not None and root.right is not None) or (root.left is None and root.right is None):
    L = full(root.left)
    R = full(root.right)
    return L and R
  elif root.left or root.right:
    return False


# 14. same
def same(root_a, root_b):
  if root_a is None and root_b is None:
    return True
  if root_a is not None and root_b is not None:
    L = same(root_a.left, root_b.left)
    R = same(root_a.right, root_b.right)
    return (root_a.data == root_b.data) and L and R
  return False


# 15. almost_same
def almost_same(root_a, root_b, k):  
  def _recursive(a, b, count, k):
    if a is None or b is None:
      return True
    if a is None and b is None:
      return True
    if count > k:
      return False

    lefty = a.data
    righty = b.data
    if lefty == righty:
      return _recursive(a.left, b.left, count, k) and _recursive(a.right, b.right, count, k)

    left = _recursive(a.left, b.left, count + 1, k)
    right = _recursive(a.right, b.right, count + 1, k)
    return left + right
  return _recursive(root_a, root_b, 0, k)
