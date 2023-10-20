from stencil import *

shkl1 = StreamHandlerKLargest(3)

shkl2 = StreamHandlerKLargest(3)
shkl2.add_stream_element(5)
shkl2.add_stream_element(3)

shkl3 = StreamHandlerKLargest(3)
shkl3.add_stream_element(5)
shkl3.add_stream_element(3)
shkl3.add_stream_element(7)
shkl3.add_stream_element(9)

shkl4 = StreamHandlerKLargest(3)
shkl4.add_stream_element(5)
shkl4.add_stream_element(7)
shkl4.add_stream_element(9)
shkl4.add_stream_element(3)

shks1 = StreamHandlerKSmallest(3)

shks2 = StreamHandlerKSmallest(3)
shks2.add_stream_element(5)
shks2.add_stream_element(3)

shks3 = StreamHandlerKSmallest(3)
shks3.add_stream_element(5)
shks3.add_stream_element(9)
shks3.add_stream_element(7)
shks3.add_stream_element(3)

shks4 = StreamHandlerKSmallest(3)
shks4.add_stream_element(3)
shks4.add_stream_element(5)
shks4.add_stream_element(7)
shks4.add_stream_element(9)

def test_k_largest_1():
  assert shkl1.k_largest() == []

def test_k_largest_2():
  assert sorted(shkl2.k_largest()) == [3, 5]

def test_k_largest_3():
  assert sorted(shkl3.k_largest()) == [5, 7, 9]

def test_k_largest_4():
  assert sorted(shkl4.k_largest()) == [5, 7, 9]

def test_k_smallest_1():
  assert shks1.k_smallest() == []

def test_k_smallest_2():
  assert sorted(shks2.k_smallest()) == [3, 5]

def test_k_smallest_3():
  assert sorted(shks3.k_smallest()) == [3, 5, 7]

def test_k_smallest_4():
  assert sorted(shks4.k_smallest()) == [3, 5, 7]

def test_heapsort_1():
  assert heapsort([9, 6, 2, 11, 15]) == [2, 6, 9, 11, 15]

def test_get_top_k_datapoints_1():
  assert get_top_k_datapoints([Datapoint(1,2,3), Datapoint(2,3,1), Datapoint(3,2,1)], 2) == set([(1,2,3), (2,3,1)])