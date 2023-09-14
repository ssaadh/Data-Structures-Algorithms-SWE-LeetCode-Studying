from __future__ import annotations
from treenode import TreeNode

import pytest

# do not modify this function call
retcode = pytest.main(['-vv'])

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
  L = TreeNode(2, TreeNode(1), None)
  R = TreeNode(6, TreeNode(5), TreeNode(7))
  root = TreeNode(3, L, R)
  return root

'''
Write a function to perform a preorder traversal on the BT and return the preorder as a list.
'''
def preorder_traversal(root: TreeNode) -> list[int]:
  def helper(root: TreeNode, lst: list[int]) -> list[int]:
    if root is None:
       return
    lst.append(root.value)
    helper(root.left, lst)
    helper(root.right, lst)
  lst = []
  helper(root, lst)
  return lst

preorder_traversal(create_BST())

'''
Write a function to perform an inorder traversal on the BT and return the inorder as a list. 
'''
# def inorder_traversal(root: TreeNode) -> list[int]:
#   if root is None:
#     return []
#   L = inorder_traversal(root.left)
#   R = inorder_traversal(root.right)
#   return L + [root.value] + R

def inorder_traversal(root: TreeNode) -> list[int]:
  def helper(root: TreeNode, lst: list[int]) -> list[int]:
    if root is None:
       return
    helper(root.left, lst)
    lst.append(root.value)
    helper(root.right, lst)
  lst = []
  helper(root, lst)
  return lst


'''
Write a function to perform a postorder traversal on the BT and return the postorder as a list.
'''
def postorder_traversal(root: TreeNode) -> list[int]:
  def helper(root: TreeNode, lst: list[int]) -> list[int]:
    if root is None:
       return
    helper(root.left, lst)
    helper(root.right, lst)
    lst.append(root.value)
  lst = []
  helper(root, lst)
  return lst


'''
Write a function to perform a level by level order traversal on the BT.
'''

def level_order_traversal(root: TreeNode) -> list[list[int]]:
  arr = []
  queue = []
  queue.append([root, 0])
  while len(queue) > 0:
    res = queue.pop(0)
    node = res[0]
    height = res[1]
    if node is not None:
      if height >= len(arr):
         arr.append([])
      arr[height].append(node.value)
      queue.append([node.left, height + 1])
      queue.append([node.right, height + 1])
  return arr


'''
Write a function to perform a traversal where we return the k smallest elements in ascending order in this BST.
'''
# this cant be a good solution??
def get_k_smallest_elements(root: TreeNode, k: int) -> list[int]:
  def helper(root: TreeNode, lst: list[int], k) -> list[int]:
    if root is None:
      return
    helper(root.left, lst, k)
    # this is such a bad way of checking?
    if len(lst) < k:
      lst.append(root.value)
    helper(root.right, lst, k)

  lst = []
  helper(root, lst, k)
  return lst
  

'''
Write a function to perform a traversal where we return the k largest elements in descending order in this BST.
'''

def get_k_largest_elements(root: TreeNode, k: int) -> list[int]:
  def helper(root: TreeNode, lst: list[int], k) -> list[int]:
    if root is None:
      return
    helper(root.right, lst, k)
    # this is such a bad way of checking right?
    if len(lst) < k:
      lst.append(root.value)
    helper(root.left, lst, k)

  lst = []
  helper(root, lst, k)
  return lst


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
        pass

            
    def word_exists(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        pass
        

    def prefix_exists(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        pass
    
    # def printS(self):
    #   cur = self.head
    #   print(cur.children)