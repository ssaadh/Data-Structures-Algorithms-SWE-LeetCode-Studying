from binary_trees import bt_a
from binary_trees import bt_b
from binary_trees import bt_c
from binary_trees import bt_d
from binary_trees import bt_e
from binary_trees import bt_long_legs

"""
This function needs to do the following:
    1. Calculate the maximum depth of the left and right sides of the given node
    2. Determine the diameter at the given node and check if its the maximum
"""

def diameter(root):
  def _recursive(node):
    if node is None:
        return 0, 0
    L, LD = _recursive(node.left)
    R, RD = _recursive(node.right)
    return max(L, R) + 1, max(L + R, LD, RD)
  return _recursive(root)[1]

class Diameter:
  def __init__(self):
    # stores the maximum diameter calculated
    self.max_diameter = 0
    
  def depth(self, node) -> int:
    if node is None:
      return 0
    # Calculate maximum depth
    left = self.depth(node.left)
    right = self.depth(node.right)
    # Calculate diameter
    self.max_diameter = max(self.max_diameter, left + right)
    # Make sure the parent node(s) get the correct depth from this node
    return max(left, right) + 1
  
def depth(self, node):
    if node is None:
        return 0

    # Initialize maximum and second maximum depths
    max1 = max2 = 0

    # Iterate over all children of the node
    for child in node.children:
        # Calculate the depth of the child
        d = self.depth(child)

        # Update maximum and second maximum depths
        if d > max1:
            max1, max2 = d, max1
        elif d > max2:
            max2 = d

    # Update maximum diameter
    self.max_diameter = max(self.max_diameter, max1 + max2)

    # Return maximum depth
    return max1 + 1
  
  def calc(self, root) -> int:
    self.depth(root)
    return self.max_diameter

hi = Algo()
print(hi.diameter(bt_a()))
hi = Algo()
print(hi.diameter(bt_b()))
hi = Algo()
print(hi.diameter(bt_c()))
hi = Algo()
print(hi.diameter(bt_d()))
hi = Algo()
print(hi.diameter(bt_e()))
hi = Algo()
print(hi.diameter(bt_long_legs()))
print('')
