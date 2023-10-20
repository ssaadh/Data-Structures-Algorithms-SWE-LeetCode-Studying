from __future__ import annotations

import pytest
# do not modify this function call
retcode = pytest.main(['-vv'])

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
