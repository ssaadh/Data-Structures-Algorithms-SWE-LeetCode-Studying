from queue import Queue

from treenode import TreeNode

root = TreeNode(3, TreeNode(2, TreeNode(1)), TreeNode(6, TreeNode(5), TreeNode(7)))

# 2023-10-11 15:53 | fixed this to a tuple but height isn't being used
def level_order_traversal(root: TreeNode) -> list[list[int]]:
  arr = []
  queue = []
  queue.append((root, 0))
  while len(queue) > 0:  
    node, height = queue.pop(0)
    if node is not None:
      arr.append(node.value)
      queue.append(node.left)
      queue.append(node.right)
  return arr

def lot(root):
  # queue = Queue()
  queue = []
  # queue.put(root)
  queue.append(root)
  while len(queue) > 0:
    # node = queue.get()
    node = queue.pop(0)
    if node is not None:
      print(node.value)
      queue.append(node.left)
      queue.append(node.right)

print(level_order_traversal(root))
print(level_order_traversal(None))
