from __future__ import annotations
from treenode import TreeNode

'''
Create a BT that looks like this and return the root.
         3         
       /   \        
      2     6     
    /     /   \    
   1     5     7 

For example, you your code should do the following.

root = create_BST() 
print(x.value) # Prints 3.
print(x.left.value) # Prints 2

You only need to construct the above tree and return the root of that tree.
'''

class TreeNode:
  def __init__(self, value: int, left: TreeNode= None, right: TreeNode= None) -> None:
    self.value = value
    self.left = left
    self.right = right

def create_BST() -> TreeNode:
  root = TreeNode(3)
  root.left = TreeNode(2)
  root.left.left = TreeNode(1)  
  root.right = TreeNode(6)
  root.right.left = TreeNode(5)
  root.right.right = TreeNode(7)
  return root

'''
Write a function to perform a preorder traversal on the BT and return the preorder as a list.
'''
def preorder_traversal(root: TreeNode) -> list[int]:
  def __helper(root: TreeNode, lst: list[int]) -> list[int]:
    if root is None:
      return []
    lst.append(root.value)
    left = __helper(root.left, lst)
    right = __helper(root.right, lst)
    return lst
  
  lst = []
  return __helper(root, lst)

'''
Write a function to perform an inorder traversal on the BT and return the inorder as a list. 
'''
def inorder_traversal(root: TreeNode) -> list[int]:
  if root is None:
    return []
  lst = []
  lst.extend(inorder_traversal(root.left))
  lst.append(root.value)
  lst.extend(inorder_traversal(root.right))
  return lst

'''
Write a function to perform a postorder traversal on the BT and return the postorder as a list.
'''
def postorder_traversal(root: TreeNode) -> list[int]:
  def __helper(root: TreeNode, lst: list[int]) -> list[int]:
    if root is None:
      return []
    left = __helper(root.left, lst)
    right = __helper(root.right, lst)
    lst.append(root.value)
    return lst
  
  lst = []
  return __helper(root, lst)

'''
Write a function to perform a level by level order traversal on the BT.
'''

def level_order_traversal(root: TreeNode) -> list[list[int]]:
  result = []
  queue = []
  queue.append(root)
  while queue:
    nxt = queue.pop(0)
    if nxt is None:
      continue
    result.append(nxt.value)
    queue.append(nxt.left)
    queue.append(nxt.right)
  return result

'''
Write a function to perform a traversal where we return the k smallest elements in ascending order in this BST.
'''

def get_k_smallest_elements(root: TreeNode, k: int) -> list[int]:
  return inorder_traversal(root)[:k]
  

'''
Write a function to perform a traversal where we return the k largest elements in descending order in this BST.
'''

def get_k_largest_elements(root: TreeNode, k: int) -> list[int]:
  return inorder_traversal(root)[::-1][:k]


'''
Complete the following Trie class.  
insert(word: str) -> None
word_exists(word: str) -> bool i.e. if our dictionary contains “doghouse”, the word “doghouse” exists but the word “dog” does not.
prefix_exists(prefix: str) -> bool i.e. if our dictionary contains “doghouse”, “dog” and “doghouse” would both be prefixes of some word(s) in our dictionary (and thus return True).
'''

class Node:
  def __init__(self) -> None:
    self.childen = {}
    self.word_exists = False

class Trie:
    def __init__(self) -> None:
        """
        Initialize your data structure here.
        """
        self.head = Node()

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        cur = self.head
        for c in word:
          if c not in cur.children:
            cur.children[c] = Node()
          cur = cur.children[c]
        cur.word_exists = True

            
    def word_exists(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        cur = self.head
        for c in word:
          if c in self.children:
            cur = cur.children[c]
          else:
            return False
        return cur.word_exists
        

    def prefix_exists(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        cur = self.head
        for c in prefix:
          if c in self.children:
            cur = cur.children[c]
          else:
            return False
        return True
    
    # def printS(self):
    #   cur = self.head
    #   print(cur.children)