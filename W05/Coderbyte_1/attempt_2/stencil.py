from __future__ import annotations
from treenode import TreeNode
from queue import Queue

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

# Follow the TreeNode structure to add the nodes
# I think of BTs in their recursive nature with their children
# So splitting up into the left and right child
# Since it's very few nodes, that's enough compartmentalization without being unwieldly
def create_BST() -> TreeNode:
  L = TreeNode(2, TreeNode(1), None)
  R = TreeNode(6, TreeNode(5), TreeNode(7))
  root = TreeNode(3, L, R)
  return root


## English workflow summary for preorder, inorder, postorder traversals

# Preorder is visiting root first, then the left then right children
# Base case of checking if root is None and return nothing to stop the recursion
# Pass in an empty array to a helper function.
# After base case, first append the node value to the array then do recursion of left child (and pass the array too) then right child
# Return the final array at the end

# Inorder will be same except visit left child first, then root, then right child
# Post order is the same except visit left child, then right child, then root

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
def inorder_traversal(root: TreeNode) -> list[int]:
  if root is None:
    return []
  L = inorder_traversal(root.left)
  R = inorder_traversal(root.right)
  return L + [root.value] + R

# def inorder_traversal(root: TreeNode) -> list[int]:
#   def helper(root: TreeNode, lst: list[int]) -> list[int]:
#     if root is None:
#        return
#     helper(root.left, lst)
#     lst.append(root.value)
#     helper(root.right, lst)
#   lst = []
#   helper(root, lst)
#   return lst


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
# This is normal BFS mostly
# Each level is in its own subarray
# start off with init a final array and a queue.
# pass in a tuple of the height of the tree along with the node to the queue
# while the queue is not empty, do the usual BFS mostly of taking a tuple out of the queue, adding it to the array, and adding the left and right children to the queue
# Node has to be checked if it is not none before doing everything after getting the next queue item as there are None nodes in the input data
# To get the subarrays, we can check if the height received from the queue is at least the size of the final array.
# If so, that means the final array is not large enough for the current height as arrays are 0 indexed.
# All of the nodes in a single level will go into the same subarray and won't increase the overall length of the final array. Since again all nodes are in a single subarray so that is just one element when counting the overall final array length
# So append a new array to the array
# For adding the current node value to the final array, now it can be added in the current heights subarray

# In other words, each time a child with the same height is added to the subarray, the length of the final array doesnt go up because the same level/height nodes are being added to the same subarray, not effecting the length of the overall final array which only gets a new empty array added the first time a new height is seen.

# Trace
# height of 0 passed in first. The first root is 3
# final: []
# queue: (3, 0)

# inside the loop:

# get next queued item is (3, 0)
# height of 0 >= len of final which is 0. init new subarray. the final array length will now be 1.
# final[0] = []
# append the node value to the subarray with the current height
# final[0] = [3]
# add left and right children to queue. the height gets iterated by 1
# queue: (2, 0 + 1), (6, 0 + 1)

# get next queued item is (2, 1)
# height of 1 >= len of final which is 1. init new subarray. the final array length will now be 2.
# final[1] = []
# append the node value to the subarray with the current height
# final[1] = [2]
# add children, iterate height
# 2 only has a single left child, 1
# queue: (6, 1), (1, 1 + 1)

# get next queued item is (6, 1)
# height of 1 is not equal or greater than len of final arr of 2
# append the node value to the subarray with the current height
# final[1] = [2, 6]
# add children, iterate height
# queue: (1, 2), (5, 1 + 1), (7, 1 + 1)

# get next queued item is (1, 2)
# Drilling it in again: The length of the final array didnt go up before because the 6 that was added was only added to the index/height of 1 subarray. So the length of the overall final array is still 2.
# height of 2 is equal or greater than len of final arr of 2. init new subarray. the final array length will now be 3.
# final[2] = []
# append the node value to the subarray with the current height
# final[2] = [1]
# no children to add
# queue: (5, 2), (7, 2)

# get next queued item is (5, 2)
# height of 2 is not equal or greater than len of final arr of 3.
# append the node value to the subarray with the current height
# final[2] = [1, 5]
# no children to add
# queue: (7, 2)

# get next queued item is (7, 2)
# height of 2 is not equal or greater than len of final arr of 3.
# append the node value to the subarray with the current height
# final[2] = [1, 5, 7]
# no children to add
# queue: empty

# final array: [[3], [2, 6], [1, 5, 7]]

# input: root = TreeNode(3, TreeNode(2, TreeNode(1)), TreeNode(6, TreeNode(5), TreeNode(7)))
# output: level_order = [[3], [2, 6], [1, 5, 7]]
def level_order_traversal(root: TreeNode) -> list[list[int]]:
  arr = []
  queue = Queue()
  queue.put((root, 0))
  while queue.qsize() > 0:
    node, height = queue.get()
    if node is not None:
      if height >= len(arr):
         arr.append([])
      arr[height].append(node.value)
      queue.put((node.left, height + 1))
      queue.put((node.right, height + 1))
  return arr


## English workflow summary for get k smallest/largest elements
# PS: not sure if the check of length of passed array into helper is an acceptable way of doing these

# Inorder can be done for this to get the smallest elements first. This works because BSTs have the left children smaller than the parent always and right children larger than the parent always. So the smallest values will be to the left.
  #        3         
  #      /   \        
  #     2     6     
  #   /     /   \    
  #  1     5     7 

# As this shows from left to right it goes smallest to largest

# Do the same as usual inorder traversal with helper having an array passed in
# We want to grab the root values up to k nodes.
# We will append the values to the array so the array length will eventually be k.
# Each time we can check if the length of the array is less than k
# If so, append the root value to the array
'''
Write a function to perform a traversal where we return the k smallest elements in ascending order in this BST.
'''
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
  
# For k largest, go from right to left. So flip the recursive calls to have the right child called first
# Then check to see if array length is less than k and append root if so
# Then do recursive call to the left child
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
    self.children = {}
    self.word_exists = False

class Trie:
  ## English workflow summary for Trie insert, work_exists, prefix_exists
  # These are similar but each is a bit diff

  # The Trie is structured to have a head which is a Node. We are only looking at alphanumerical or just alphabet so the head will have at most 26 children -- each character of the alphabet.
  # The input for each is a string. We want to go character by character for the string. At first we can make the current Node we are looking at be the head. This will be the current node whose children we will look at.
  # Check if each character is in the children of the current node we are looking at.
  # If so, make the current node, the checked character. This is consistent across all functions as all 3 are trying to either check for the exitence of the whole word or to insert it.

  # So the overall structure again is to have some current node we can check thru. This is the head each time.
  # We iterate thru each character in the input string
  # We check if the character is in the current node's children
  # Now the details for each function will be diff
  def __init__(self) -> None:
    """
    Initialize your data structure here.
    """
    self.head = Node()

  # For insert:
  # If the character is not in the current node, make a new node for that character in the current node's children.
  # If the character is in the current node's children, iterate the current node to that character.
  # We will do the iteration of the current to that of the character being checked in both cases.
  # The current character is set as the key of the current node's children if the character exists in the current node's children
  # This is because if the character exists already, we have to move on to the next character to see if that exists and if not, to insert that character. If it doesn't exist, we have to create that character in the current nodes children to eventually get the full word inserted.
  # At the end after iterating thru the input string, since we are inserting a word, the final node we end up at which is the last character of the input string, has to have its word_exists flag be set to True. Since it is a word.
  def insert(self, word: str) -> None:
    """
    Inserts a word into the trie.
    """
    cur = self.head
    for char in word:
      if char not in cur.children:
        cur.children[char] = Node()
      cur = cur.children[char]
    cur.word_exists = True


  # For word_exists:
  # Similar to insert, we iterate thru each character. If the character exists in the current node's children, iterate the current node to the character we are checking in the current node's children.
  # The current character is set as the key of the current node's children if the character exists in the current node's children
  # If the character is not in the current node's children, return false because without that character in the Trie, the word is not in the Trie.
  # Once done iterating thru all of the input strings characters, we dont yet know if the word actually exists in the Trie, just that those set of characters are in the Trie. Returning the current/final character/node's word_exists flag will return True if the word exists or otherwise false.
  def word_exists(self, word: str) -> bool:
    """
    Returns if the word is in the trie.
    """
    cur = self.head
    for char in word:
      if char not in cur.children:
        return False
      cur = cur.children[char]
    return cur.word_exists
      

  # For prefix_exists:
  # This is the same as word existing except we dont have to care if the input prefix connects to a word. just that the entire prefix aka each of the characters of the prefix are in the Trie. So if we can iterate thru all of the characters and always have the characters inside the current node's children, once done with the loop, we know that the prefix exists.
  # The current character is set as the key of the current node's children if the character exists in the current node's children
  # Otherwise like for word_exists function, in the loop if the current iterating character is not in the current node's children, return false
  def prefix_exists(self, prefix: str) -> bool:
    """
    Returns if there is any word in the trie that starts with the given prefix.
    """
    cur = self.head
    for char in prefix:
      if char not in cur.children:
        return False
      cur = cur.children[char]
    return True
    
  # def printS(self):
  #   cur = self.head
  #   print(cur.children)

## PSUEDOCODE
# To be read after reading the specific English workflow summary comments in the Trie class itself and for each of the main methods

# Psuedocode way of having the check always check if the current character isnt in the Trie initially in the loop.
# This is preferred for my mental model because normally iterating always has to happen so the curr character not being in the Trie breaks that and afterward if we do get out of this if statement check, the iterating will happen

# cur = self.head
# for c in input_str:
#   if c not in cur.children:    
#     # can return False if we are looking for the existence of stuff
#     # example:
#     return False
#     # if inserting or something, then we would create the new node with the current c character being the key of the cur node's children and creating a new Node.
#     # example:
#     cur.children[c] = Node()
#   # now we iterate
#   cur = cur.children[c]
# # outside the loop meaning the full input string was processed
# # so cur is now at the final character of the input string
# # Can use `word_exists` if we are looking for the input string being an existing word.
# # example:
# return cur.word_exists
# # Return `True`` if just looking for the input string existing in the Trie at all
# # example:
# return True

# Psuedocode basic when checking if the current character of the input string is in the current node's children:
# cur = self.head
# for c in input_str:
#   if c in cur.children:
#     # do something like iterate to the next character
#     cur = cur.children[c]
#   OR
#   if c not in cur.children:
#     # this can end the loop if checking if something exists since it doesnt.
#     # Or if inserting, we would create the Node:
#     cur.children[c] = Node()
# once done with loop