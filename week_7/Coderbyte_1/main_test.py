from stencil import *

def test_unique_paths_top_down_1():
  assert unique_paths_top_down(3, 7) == 28

def test_unique_paths_top_down_2():
  assert unique_paths_top_down(7, 3) == 28

def test_unique_paths_top_down_3():
  assert unique_paths_top_down(3, 2) == 3

def test_unique_paths_top_down_4():
  assert unique_paths_top_down(2, 3) == 3

def test_unique_paths_bottom_up_1():
  assert unique_paths_bottom_up(3, 7) == 28

def test_unique_paths_bottom_up_2():
  assert unique_paths_bottom_up(7, 3) == 28

def test_unique_paths_bottom_up_3():
  assert unique_paths_bottom_up(3, 2) == 3

def test_unique_paths_bottom_up_4():
  assert unique_paths_bottom_up(2, 3) == 3