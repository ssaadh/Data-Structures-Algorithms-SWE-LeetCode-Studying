from queue import Queue

class Node:
  def __init__(self, v):
    self.data = v
    self.left = None
    self.right = None

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

print(find_height(bt_a(), 2))
  
def level_order_traversal(root):
  queue = Queue()
  queue.put(root)
  while queue.empty() is False:
    node = queue.get()
    if node is not None:
      print(node.data)
      queue.put(node.left)
      queue.put(node.right)

def sum_only_child_parents(root):
  if root is None:
    return 0
  if (root.left is None and root.right is not None) or (root.left is not None and root.right is None):
    return root.data
  L = sum_only_child_parents(root.left)
  R = sum_only_child_parents(root.right)
  return L + R

def level_min(root, height):
  if root is None:
    return 0
  min_node = 999
  queue = Queue()
  queue.put([root, 0])
  while queue.empty() is False:
    arr = queue.get()
    node = arr[0]
    h = arr[1]
    if node is not None:
      if h == height:
        if node.data < min_node:
          min_node = node.data
      queue.put([node.left,h+1])
      queue.put([node.right,h+1])
  return min_node
