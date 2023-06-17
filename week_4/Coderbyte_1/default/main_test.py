from stencil import *

def test_reverse_str_1():
  assert reverse_str("abcd") == "dcba"

def test_reverse_str_2():
  assert reverse_str("abbd") == "dbba"

def test_most_freq_substring_1():
  assert most_freq_substring("abaa", 2) == "aa"

def test_most_freq_substring_2():
  assert most_freq_substring("eabcdeab", 3) == "eab"

def test_smallest_subsequence_1():
  assert smallest_subsequence("agbf", 2) == "ab"

def test_smallest_subsequence_2():
  assert smallest_subsequence("batman", 3) == "aan"

def test_merge_n_lists_1():
  assert merge_n_lists([[1, 5, 8], [0, 2, 10], [4, 8, 9]]) == [0, 1, 2, 4, 5, 8, 8, 9, 10]

def test_merge_n_lists_2():
  assert merge_n_lists([[1, 3], [2, 4]]) == [1, 2, 3, 4]

def test_merge_n_lists_3():
  assert merge_n_lists([[1, 3], [4, 6]]) == [1, 3, 4, 6]

def test_merge_n_lists_4():
  assert merge_n_lists([[4, 6], [1, 3]]) == [1, 3, 4, 6]

def test_merge_n_lists_5():
  assert merge_n_lists([[1, 3, 5]]) == [1, 3, 5]

def test_sort_tuples_1():
  assert sort_tuples([(1,1), (2,2), (2,1), (1,2)]) == [(1,2), (1,1), (2,2), (2,1)]

def test_sort_tuples_2():
  assert sort_tuples([(2,10),(1,10),(3,10)]) == [(1,10),(2,10),(3,10)]

def test_sort_tuples_3():
  assert sort_tuples([(10,2),(10,1),(10,3)]) == [(10,3),(10,2),(10,1)]