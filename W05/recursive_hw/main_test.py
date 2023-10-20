from binary_trees import bt_a
from binary_trees import bt_b
from binary_trees import bt_c
from binary_trees import bt_d
from binary_trees import bt_e
from binary_trees import bt_long_legs

from recursive_relations import size
from recursive_relations import qsum
from recursive_relations import max_val
from recursive_relations import is_symmetric
from recursive_relations import height
from recursive_relations import diameter
from recursive_relations import leafs
from recursive_relations import top_ordered
from recursive_relations import find_height
from recursive_relations import sum_only_child_parents
from recursive_relations import sum_only_child
from recursive_relations import level_min
from recursive_relations import is_symmetric
from recursive_relations import full
from recursive_relations import same
from recursive_relations import almost_same

# def test_qsum_1():
#   assert qsum(bt_a()) == 65
#   assert qsum(bt_b()) == 15
#   assert qsum(bt_c()) == 66
#   assert qsum(bt_d()) == 23
#   assert qsum(bt_e()) == 48

# def test_max_val_1():
#   assert max_val(bt_a()) == 14
#   assert max_val(bt_b()) == 5
#   assert max_val(bt_c()) == 11
#   assert max_val(bt_d()) == 5
#   assert max_val(bt_e()) == 10

# def test_height_1():
#   assert height(bt_a()) == 3

# def test_height_2():
#   assert height(bt_b()) == 4

# def test_height_3():
#   assert height(bt_c()) == 3

# def test_height_4():
#   assert height(bt_d()) == 2

# def test_height_5():
#   assert height(bt_e()) == 4

# def test_diameter_1():
#   assert diameter(bt_a()) == 6

# def test_diameter_2():
#   assert diameter(bt_b()) == 4

# def test_diameter_3():
#   assert diameter(bt_c()) == 5

# def test_diameter_4():
#   assert diameter(bt_d()) == 4

# def test_diameter_5():
#   assert diameter(bt_e()) == 7

# def test_diameter_6():
#   assert diameter(bt_long_legs()) == 8

def test_sum_only_child_1():
  assert sum_only_child(bt_a(), True) == 34

def test_sum_only_child_2():
  assert sum_only_child(bt_b(), True) == 15

def test_sum_only_child_3():
  assert sum_only_child(bt_c(), True) == 1

def test_sum_only_child_4():
  assert sum_only_child(bt_d(), True) == 1

def test_sum_only_child_5():
  assert sum_only_child(bt_e(), True) == 34
