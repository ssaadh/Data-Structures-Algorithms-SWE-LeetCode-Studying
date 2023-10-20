from stencil import *
from treenode import TreeNode

root = TreeNode(3, TreeNode(2, TreeNode(1)), TreeNode(6, TreeNode(5), TreeNode(7)))


inorder = [1, 2, 3, 5, 6, 7]
preorder = [3, 2, 1, 6, 5, 7]
postorder = [1, 2, 5, 7, 6, 3]
level_order = [[3], [2, 6], [1, 5, 7]]

def test_create_bst():
  new_bst = create_BST()
  assert new_bst.value == 3
  assert new_bst.left.value == 2
  assert new_bst.left.left.value == 1
  assert new_bst.left.left.left is None
  assert new_bst.right.value == 6
  assert new_bst.right.right.value == 7
  assert new_bst.right.left.value == 5

def test_preorder_traversal_1():
  assert preorder_traversal(root) == preorder

def test_inorder_traversal_1():
  assert inorder_traversal(root) == inorder

def test_postorder_traversal_1():
  assert postorder_traversal(root) == postorder

def test_level_order_traversal_1():
  assert level_order_traversal(root) == level_order

def test_level_order_traversal_2():
  assert level_order_traversal(None) == []

def test_get_k_smallest_elements_1():
  assert get_k_smallest_elements(root, 4) == [1, 2, 3, 5]

def test_get_k_largest_elements_1():
  assert get_k_largest_elements(root, 4) == [7, 6, 5, 3]

trie = Trie()
trie.insert("doghouse")

def test_trie_word_exists_1():
  assert trie.word_exists("doghouse") == True

def test_trie_word_exists_2():
  assert trie.word_exists("dog") == False

def test_trie_word_exists_3():
  assert trie.word_exists("dogs") == False

def test_trie_prefix_exists_1():
  assert trie.prefix_exists("dog") == True

def test_trie_prefix_exists_2():
  assert trie.prefix_exists("dogs") == False