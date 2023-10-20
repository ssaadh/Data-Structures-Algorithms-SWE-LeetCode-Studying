# 11. sum_only_child
def sum_only_child_deux(root, is_root = True):
  if root is None:
    return 0
  
  if is_root:
    return sum_only_child_deux(root.left, False) + sum_only_child_deux(root.right, False) + root.data
  
  if root.left is None and root.right is not None:
    return sum_only_child_deux(root.left, False) + sum_only_child_deux(root.right, False) + root.right.data
  elif root.left is not None and root.right is None:
    return sum_only_child_deux(root.left, False) + sum_only_child_deux(root.right, False) + root.left.data
  else:
    return sum_only_child_deux(root.left, False) + sum_only_child_deux(root.right, False)
