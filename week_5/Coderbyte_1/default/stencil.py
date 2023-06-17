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

def create_BST() -> TreeNode:
  pass

'''
Write a function to perform a preorder traversal on the BT and return the preorder as a list.
'''
def preorder_traversal(root: TreeNode) -> list[int]:
  pass

'''
Write a function to perform an inorder traversal on the BT and return the inorder as a list. 
'''
def inorder_traversal(root: TreeNode) -> list[int]:
  pass

'''
Write a function to perform a postorder traversal on the BT and return the postorder as a list.
'''
def postorder_traversal(root: TreeNode) -> list[int]:
  pass

'''
Write a function to perform a level by level order traversal on the BT.
'''

def level_order_traversal(root: TreeNode) -> list[list[int]]:
  pass

'''
Write a function to perform a traversal where we return the k smallest elements in ascending order in this BST.
'''

def get_k_smallest_elements(root: TreeNode, k: int) -> list[int]:
  pass

'''
Write a function to perform a traversal where we return the k largest elements in descending order in this BST.
'''

def get_k_largest_elements(root: TreeNode, k: int) -> list[int]:
  pass

'''
Complete the following Trie class.  
insert(word: str) -> None
word_exists(word: str) -> bool i.e. if our dictionary contains “doghouse”, the word “doghouse” exists but the word “dog” does not.
prefix_exists(prefix: str) -> bool i.e. if our dictionary contains “doghouse”, “dog” and “doghouse” would both be prefixes of some word(s) in our dictionary (and thus return True).
'''        
class Trie:
    def __init__(self) -> None:
        """
        Initialize your data structure here.
        """
        pass

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
