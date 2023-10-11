from __future__ import annotations
import heapq

# import pytest
# do not modify this function call
# retcode = pytest.main(['-v'])

'''
Complete the StreamHandlerKLargest class that has a capacity k by filling in the methods.
'''

class StreamHandlerKLargest:
  def __init__(self, k: int) -> None:
    self.k = k
    self.heap = []

  # TODO go thru and trace the heappush and heappushpop
  # TODO this will give deeper understanding you dont have right now!
  # TODO understand ascending and decending and the defaults!
  
  '''
  This method adds the stream element to the collection. 
  You only need to store the k largest elements seen so far at any given point in time.
  '''
  def add_stream_element(self, e: int) -> None:
    if len(self.heap) < self.k:
      heapq.heappush(self.heap, e)
    elif len(self.heap) == self.k:
      heapq.heappushpop(self.heap, e)
    return None

  ''' 
  This method returns the k largest elements seen so far.
  '''
  def k_largest(self) -> list[int]:
    if len(self.heap) < self.k:
      return self.heap
    return self.heap[:self.k]
  
# TODO explain the differences

class StreamHandlerKSmallest:
  def __init__(self, k: int) -> None:
    self.k = k
    self.heap = []
  
  '''
  This method adds the stream element to the collection. 
  You only need to store the k smallest elements seen so far at any given point in time.
  '''
  def add_stream_element(self, e: int) -> None: 
    if len(self.heap) < self.k:
      heapq.heappush(self.heap, -e)
    elif len(self.heap) == self.k:
      heapq.heappushpop(self.heap, -e)
    return None

  ''' 
  This method returns the k smallest elements seen so far.
  '''
  def k_smallest(self) -> list[int]: 
    if len(self.heap) < self.k:
      return [-m for m in self.heap]
    return [-m for m in self.heap[:self.k]]
  
''' 
Write a function that creates a copy of the list, and sorts it in ascending order
using a heap.
'''

# TODO Trace thru
# Talk to Coachable-AI
# Go through the input list and add each to a heap
# Or heapify can do the whole list in one go?
# Heapify will order it from smallest to largest which is ascending (ascend up)

def heapsort(input_list: list[int]) -> list[int]: 
  final = []
  heapq.heapify(input_list)
  while input_list:
    next_up = heapq.heappop(input_list)
    final.append(next_up)
  return final


'''
Suppose we have some data that can be expressed as a tuple (a, b, c). 
We want to get the top k tuples out of a collection of n total tuples, 
where k <= n. Each datapoint has a score, defined as 2*a + 5*b + 10*c, 
and the higher the score, the greater the datapoint. 
Complete the class for this datapoint object, and complete the below function, using a heap to do so.
'''

# The heap has to have the score value stored for the heap to automatically compare them

class Datapoint:
  def __init__(self, a: int, b: int, c: int) -> None:
    self.a = a
    self.b = b
    self.c = c

  def to_tuple(self) -> tuple[int, int, int]:
    return (self.a, self.b, self.c)
  
  # TODO: you may need to add additional methods here. 
  def score(self):
    return 2 * self.a + 5 * self.b + 10 * self.c
  
  # This is inverted so the max goes to the "top" (lowest index in array) of heap
  def __lt__(self, other):
    if self.score() > other.score():
      return True

# Return them as tuples, using the to_tuple method in the Datapoint class.
def get_top_k_datapoints(data_collection: list[Datapoint], k: int) -> set[tuple[int, int, int]]:
  heapq.heapify(data_collection)
  for m in data_collection:
    print(m.to_tuple(), m.score())
  final = set()
  for m in range(k):
    final.add(heapq.heappop(data_collection).to_tuple())
  return final
