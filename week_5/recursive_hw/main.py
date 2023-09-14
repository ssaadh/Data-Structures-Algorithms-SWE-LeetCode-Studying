import pytest

from binary_trees import bt_a
from binary_trees import bt_b
from binary_trees import bt_c
from binary_trees import bt_d
from binary_trees import bt_e
from binary_trees import bt_long_legs
from binary_trees import bt_a_diff

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

# do not modify this function call
retcode = pytest.main(['-vv'])

## Driver code
if __name__ == "__main__":
  # print('')
  # print('size')
  # print('a: ', size(bt_a()))
  # print('b: ', size(bt_b()))
  # print('c: ', size(bt_c()))
  # print('d: ', size(bt_d()))
  # print('e: ', size(bt_e()))

  # print('')
  # print('sum qsum')
  # print('a: ', qsum(bt_a()))
  # print('b: ', qsum(bt_b()))
  # print('c: ', qsum(bt_c()))
  # print('d: ', qsum(bt_d()))
  # print('e: ', qsum(bt_e()))

  # print('')
  # print('max_val')
  # print('a: ', max_val(bt_a()))
  # print('b: ', max_val(bt_b()))
  # print('c: ', max_val(bt_c()))
  # print('d: ', max_val(bt_d()))
  # print('e: ', max_val(bt_e()))

  # print('')
  # print('height')
  # print('a: ', height(bt_a()))
  # print('b: ', height(bt_b()))
  # print('c: ', height(bt_c()))
  # print('d: ', height(bt_d()))
  # print('e: ', height(bt_e()))

  # print('')
  # print('diameter')
  # print('a: ', diameter(bt_a()))
  # print('b: ', diameter(bt_b()))
  # print('c: ', diameter(bt_c()))
  # print('d: ', diameter(bt_d()))
  # print('e: ', diameter(bt_e()))
  # print('k: ', diameter(bt_long_legs()))

  # print('')
  # print('sym')
  # print('a: ', is_symmetric(bt_a()))
  # print('b: ', is_symmetric(bt_b()))
  # print('c: ', is_symmetric(bt_c()))
  # print('d: ', is_symmetric(bt_d()))
  # print('e: ', is_symmetric(bt_e()))

  # print('')
  # print('leafs')
  # print('a: ', leafs(bt_a()))
  # print('b: ', leafs(bt_b()))
  # print('c: ', leafs(bt_c()))
  # print('d: ', leafs(bt_d()))
  # print('e: ', leafs(bt_e()))

  # print('')
  # print('top_ordered')
  # print('a: ', top_ordered(bt_a()))
  # print('b: ', top_ordered(bt_b()))
  # print('c: ', top_ordered(bt_c()))
  # print('d: ', top_ordered(bt_d()))
  # print('e: ', top_ordered(bt_e()))

  # print('')
  # print('find_height')
  # print('a: ', find_height(bt_a(), 2))
  # print('b: ', find_height(bt_b(), 2))
  # print('c: ', find_height(bt_c(), 2))
  # print('d: ', find_height(bt_d(), 2))
  # print('e: ', find_height(bt_e(), 2))

  # print('')
  # print('sum_only_child_parents')
  # print('a: ', sum_only_child_parents(bt_a()))
  # print('b: ', sum_only_child_parents(bt_b()))
  # print('c: ', sum_only_child_parents(bt_c()))
  # print('d: ', sum_only_child_parents(bt_d()))
  # print('e: ', sum_only_child_parents(bt_e()))

  print('')
  print('sum_only_child')
  print('a: ', sum_only_child(bt_a(), True))
  print('b: ', sum_only_child(bt_b(), True))
  print('c: ', sum_only_child(bt_c(), True))
  print('d: ', sum_only_child(bt_d(), True))
  print('e: ', sum_only_child(bt_e(), True))

  # print('')
  # print('level_min')
  # print('a: ', level_min(bt_a(), 2))
  # print('b: ', level_min(bt_b(), 2))
  # print('c: ', level_min(bt_c(), 2))
  # print('d: ', level_min(bt_d(), 2))
  # print('e: ', level_min(bt_e(), 2))

  print('')
  print('full_binary_tree')
  print('a: ', full(bt_a()))
  print('b: ', full(bt_b()))
  print('c: ', full(bt_c()))
  print('d: ', full(bt_d()))
  print('e: ', full(bt_e()))

  # print('')
  # print('same')
  # print('a: ', same(bt_a(), bt_a()))
  # print('b: ', same(bt_b(), bt_b()))
  # print('c: ', same(bt_c(), bt_b()))
  # print('d: ', same(bt_d()))
  # print('e: ', same(bt_e()))

  # print('')
  # print('almost_same')
  # print('0: ', almost_same(bt_a(), bt_a_diff(), 0))
  # print('1: ', almost_same(bt_a(), bt_a_diff(), 1))
  # print('2: ', almost_same(bt_a(), bt_a_diff(), 2))
  # print('3: ', almost_same(bt_a(), bt_a_diff(), 3))
  # print('4: ', almost_same(bt_a(), bt_a_diff(), 4))
