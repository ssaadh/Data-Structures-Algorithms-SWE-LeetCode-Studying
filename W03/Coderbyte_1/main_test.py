from stencil import *

def test_recurse_1():
  assert recurse([1, 2, 3]) == "1 2 3 "

def test_fact_iter_1():
  assert fact_iter(5) == 120

def test_fact_iter_2():
  assert fact_iter(10) == 3628800

def test_fact_recursive_1():
  assert fact_recursive(5) == 120

def test_fact_recursive_2():
  assert fact_recursive(10) == 3628800

def test_find_index_1():
  assert find_index([1, 5, 10, 20, 100], 5) == 1

def test_find_index_2():
  assert find_index([1, 5, 10, 20, 100], 15) == -1

def test_find_closest_1():
  assert find_closest([1, 5, 10, 20, 100], 9) == 1

def test_find_closest_2():
  assert find_closest([1, 5, 10, 20, 100], 21) == 3

def test_find_closest_3():
  assert find_closest([1, 5, 10, 20, 100], 0) == -1