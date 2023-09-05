from node import Node

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
