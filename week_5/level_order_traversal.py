from queue import Queue

## Node
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

def level_order_traversal(root):
  queue = Queue()
  queue.put(root)
  while queue.empty() is False:
    node = queue.get()
    if node is not None:
      print(node.data)
      queue.put(node.left)
      queue.put(node.right)

print(level_order_traversal(bt_a()))
