class Node:
    def __init__(self):
        self.children = {}
        self.isWord = False

class Trie:
  def _init__(self):
        """
        Initialize your data structure here.
        """
        self.root = Node()


  def insert(self, word: str) -> None:
      """
      Inserts a word into the trie.
      """
      curNode = self.root
      for c in word:
          if c not in curNode.children:
              curNode.children[c] = Node()
          curNode = curNode.children[c]
      curNode.isWord = True


  def search(self, word: str) -> bool:
      """
      Returns if the word is in the trie.
      """
      curNode = self.root
      for c in word:
          if c in curNode.children:
              curNode = curNode.children[c]
          else:
              return False
      return curNode.isWord

  def startsWith(self, prefix: str) -> bool:
      """
      Returns if there is any word in the trie that starts with the given prefix.
      """
      curNode = self.root
      for c in prefix:
          if c in curNode.children:
              curNode = curNode.children[c]
          else:
              return False
      return True
