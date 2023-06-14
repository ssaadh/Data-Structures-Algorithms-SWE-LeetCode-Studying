## Node
class Node:
  def __init__(self, v):
    self.data = v
    self.left = None
    self.right = None

## 15 
def size(root):
  if root is None:
    return 0
  # print(root.data)
  left = size(root.left)
  right = size(root.right)
  return left + right + 1

def sum(root):
  if root is None:
    return 0
  return sum(root.left) + root.data + sum(root.right)

def max_val(root):
  if root is None:
    return 0
  left = max_val(root.left)
  right = max_val(root.right)
  return max(root.data, max(left, right))

def preorder(root):
  def _recursive(node):
    if node is not None:
      output.append(node.data)
      _recursive(node.left)
      _recursive(node.right)

  output = []
  _recursive(root)
  return output

def rev_preorder(root):
  def _recursive(node):
    if node is not None:
      output.append(node.data)
      _recursive(node.right)
      _recursive(node.left)

  output = []
  _recursive(root)
  return output

def is_symmetric(root):
  arr = []
  if root is None:
    return False
  left = preorder(root)
  right = rev_preorder(root)
  return left == right

def height_preorder(root):
  def _recursive(node):
    if node is not None:
      return 0
    # height[0] += 1
    _recursive(node.right)
    _recursive(node.left)

  height = [0]
  _recursive(root)
  return height[0]

def heighty(root):
  if root is None:
    # 0 or -1?
    return -1
  left = heighty(root.left)
  right = heighty(root.right)
  return max(left, right) + 1

def diameter(root):
  max_diameter = 0
  return _recursive(root.left, max_diameter) + _recursive(root.right, max_diameter) + 1

  def _recursive(node):
    if node is None:
      return 0
    left = _recursive(node.left)
    right = _recursive(node.right)
    max_diameter = max(max_diameter, left + right)
    return max(left, right) + 1


# def diameter(root):
#   if root is None:
#     return 0
  
#   left = heighty(root.left)
#   right = heighty(root.right)

#   l = diameter(root.left)
#   r = diameter(root.root)

#   return 1 + max(diameter)

def leafs(root):
  def _recursive(node):
    if node is None:
      return 0
    if node.left is None and node.right is None:
      return 1
    left = _recursive(node.left)
    right = _recursive(node.right)
    return left + right
  return _recursive(root)

def top_ordered(root):
  if root is None:
    return False
  if root.left and root.right:
    if root.data < max(root.left.data, root.right.data):
      return True
  if root.left and root.right is None:
    if root.data < root.left.data:
      return True
  if root.right and root.left is None:
    if root.data < root.right.data:
      return True
  left = top_ordered(root.left)
  right = top_ordered(root.right)
  return left + right

def find_height(root, height):
  def _recursive(node, count):
    if node is None:
      return 0
    if count >= height:
      return 1
      
    left = find_height(node.left, count + 1)
    right = find_height(node.right, count + 1)
    return max(left, right) + 1
  return _recursive(root, 0)

def sum_only_child_parents(root):
  if root is None:
    return 0
  if (root.left is None and root.right is not None) or (root.left is not None and root.right is None):
    return sum_only_child_parents(root.left) + sum_only_child_parents(root.right) + root.data
  left = sum_only_child_parents(root.left)
  right = sum_only_child_parents(root.right)
  return left + right

def sum_only_child(root):
  if root is None:
    return 0
  if root.left is None and root.right is not None:
    return sum_only_child(root.left) + sum_only_child(root.right) + root.right.data
  elif root.left is not None and root.right is None:
    return sum_only_child(root.left) + sum_only_child(root.right) + root.left.data
  left = sum_only_child(root.left)
  right = sum_only_child(root.right)
  return left + right

def level_min(root, height):
  def _recursive(node, count):
    if root is None:
      return 0
    if count >= height:
      return node.data
    left = _recursive(node.left, height + 1)
    right = _recursive(node.left, height + 1)
    return min(left, right)
  return _recursive(root, 0)

def full_binary_tree(root):
  if root is None:
    return False
  
  left = full_binary_tree(root.left)
  right = full_binary_tree(root.right)

  if root.left is not None and root.right is not None:
    return True
  if root.left is None and root.right is None:
    return False
  if root.left or root.right:
    return False
  pass  

def same(root_a, root_b):
  if root_a is None or root_b is None:
    return False
  if root_a is None and root_b is None:
    return True

  left = same(root_a.left, root_b.left)
  right = same(root_a.right, root_b.right)
  lefty = root_a.data
  righty = root_b.data
  return lefty == righty and left == right

def almost_same(root_a, root_b, k):  
  def _recursive(a, b, count, k):
    if a is None or b is None:
      return False
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


## PRINT

def printInorder(root):
  if root:
    printInorder(root.left)    
    print(root.data,end=" ")      
    printInorder(root.right)

def printPreOrder(node):
  if node is None:
    return
  print(node.data, end = " ")    
  printPreOrder(node.left)
  printPreOrder(node.right)

def printRevPreOrder(node):
  if node is None:
    return
  print(node.data, end = " ")
  printRevPreOrder(node.right)
  printRevPreOrder(node.left)

def printPostOrder(node):
  if node is None:
    return
  printPostOrder(node.left)
  printPostOrder(node.right)  
  print(node.data, end = " ")

def bt_first():
  root = Node(100)
  root.left = Node(50)
  root.left.left = Node(25)
  root.left.left.left = Node(20)
  root.left.left.right = Node(30)
  root.left.right = Node(75)
  root.left.right.left = Node(60)
  root.left.right.right = Node(80)
  root.right = Node(200)
  root.right.left = Node(190)
  root.right.left.left = Node(180)
  root.right.left.left.left = Node(170)
  root.right.left.left.right = Node(181)
  root.right.right = Node(500)
  root.right.right.right = Node(550)
  root.right.right.right.left = Node(525)
  root.right.right.right.right = Node(575)
  return root

def bt_second():
  root = Node(1)    
  root.left = Node(2)
  root.left.left = Node(4)
  root.left.left.left = Node('4L')
  root.left.left.right = Node('4R')
  root.left.right = Node('2R')
  root.left.right.left = Node('2RL')
  root.left.right.right = Node('2RR')

  root.right = Node(3)
  root.right.left = Node('3L')
  root.right.right = Node(5)
  root.right.right.left = Node(6)
  root.right.right.left.left = Node('6L')
  root.right.right.left.right = Node('6R')
  root.right.right.right = Node(7)
  root.right.right.right.left = Node('7L')
  root.right.right.right.right = Node(8)
  return root

def bt_a():
  root = Node(8)
  root.left = Node(3)
  root.left.left = Node(1)
  root.left.right = Node(6)
  root.left.right.left = Node(4)
  root.left.right.right = Node(7)

  root.right = Node(10)
  root.right.right = Node(14)
  root.right.right.left = Node(12)
  return root

def bt_b():
  root = Node(1)
  root.right = Node(2)
  root.right.right = Node(3)
  root.right.right.right = Node(4)
  root.right.right.right.right = Node(5)
  return root

def bt_c():
  root = Node(1)
  root.left = Node(2)
  root.left.left = Node(4)
  root.left.left.left = Node(8)
  root.left.left.right = Node(9)

  root.left.right = Node(5)
  root.left.right.left = Node(10)
  root.left.right.right = Node(11)

  root.right = Node(3)
  root.right.left = Node(6)
  root.right.right = Node(7)
  return root

def bt_d():
  root = Node(1)
  root.left = Node(2)
  root.left.left = Node(4)
  root.left.right = Node(5)

  root.right = Node(2)
  root.right.left = Node(5)
  root.right.right = Node(4)    
  return root

def bt_e():
  root = Node(1)
  root.left = Node(2)
  root.left.left = Node(4)
  root.left.right = Node(5)
  root.left.left.left = Node(10)

  root.right = Node(3)
  root.right.right = Node(6)
  root.right.right.right = Node(8)
  root.right.right.right.right = Node(9)
  return root
 
## Driver code
if __name__ == "__main__":
  # Function call
  # print("Inorder Traversal: ", end = "")
  
  # # print(bt_first())
  # printInorder(bt_first())
  # print('\n')

  # print("Preorder Traversal: ", end = "")
  # printPreOrder(bt_first())
  # print('\n')

  # print("RevPreOrder Traversal: ", end = "")
  # printRevPreOrder(bt_first())
  # print('\n')

  # print("Postorder Traversal: ", end = "")
  # printPostOrder(bt_first())
  # print('\n')


  print('size')
  print(size(bt_c()))

  print('sum')
  print(sum(bt_c()))

  print('max_val')
  print(max_val(bt_a()))

  print('diameter')
  # print(diameter(bt_c()))

  print('heighty')
  print(heighty(bt_c()))

  print('sym')
  print(is_symmetric(bt_d()))

  print('leafs')
  print(leafs(bt_e()))

  print('top_ordered')
  print(top_ordered(bt_b()))

  print('find_height')
  print(find_height(bt_b(), 2))

  print('sum_only_child_parents')
  print(sum_only_child_parents(bt_c()))

  print('sum_only_child')
  print(sum_only_child(bt_c()))

  print('level_min')
  print(level_min(bt_c(), 3))

  print('full_binary_tree')
  print(full_binary_tree(bt_b()))

  print('same')
  print(same(bt_c(), bt_b()))

  print('almost_same')
  print(almost_same(bt_c(), bt_c(), 2))
