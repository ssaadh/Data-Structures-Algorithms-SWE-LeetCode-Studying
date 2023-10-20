from __future__ import annotations
import heapq

'''
Complete the StreamHandlerKLargest class that has a capacity k by filling in the methods.
'''

class StreamHandlerKLargest:
  def __init__(self, k: int) -> None:
    self.k = k
  
  '''
  This method adds the stream element to the collection. 
  You only need to store the k largest elements seen so far at any given point in time.
  '''
  def add_stream_element(self, e: int) -> None: 
    pass

  ''' 
  This method returns the k largest elements seen so far.
  '''
  def k_largest(self) -> list[int]: 
    return []

'''
Complete the StreamHandlerKSmallest class that has a capacity k by filling in the methods.
'''

class StreamHandlerKSmallest:
  def __init__(self, k: int) -> None:
    self.k = k
  
  '''
  This method adds the stream element to the collection. 
  You only need to store the k smallest elements seen so far at any given point in time.
  '''
  def add_stream_element(self, e: int) -> None: 
    pass

  ''' 
  This method returns the k smallest elements seen so far.
  '''
  def k_smallest(self) -> list[int]: 
    return []

''' 
Write a function that creates a copy of the list, and sorts it in ascending order
using a heap.
'''
def heapsort(input_list: list[int]) -> list[int]: 
  return []

'''
Suppose we have some data that can be expressed as a tuple (a, b, c). 
We want to get the top k tuples out of a collection of n total tuples, 
where k <= n. Each datapoint has a score, defined as 2*a + 5*b + 10*c, 
and the higher the score, the greater the datapoint. 
Complete the class for this datapoint object, and complete the below function, using a heap to do so.
'''
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
  final = set()
  for m in range(k):
    final.add(heapq.heappop(data_collection).to_tuple())
  return final
