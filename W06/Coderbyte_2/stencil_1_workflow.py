from __future__ import annotations
import heapq

'''
Complete the StreamHandlerKLargest class that has a capacity k by filling in the methods.
'''
class StreamHandlerKLargest:
  def __init__(self, k: int) -> None:
    self.k = k
    self.heap = []
  
  '''
  This method adds the stream element to the collection. 
  You only need to store the k largest elements seen so far at any given point in time.
  '''

# Binary heaps work by having the highest value at the beginning of the array. When it has to be popped, it does this in O(log n) by swapping the first and last values then sinking the swapped value that is smallest/largest down the binary heap until it can get to its new position. And the original smallest/largest number can be popped in O(1) because it's at the end of the array where that can happen. heapq specifically is a min-heap so it holds the smallest values.

# That's why add_stream_element for k_largest needs to check the smallest element by popping once which pulls out the smallest element. Whichever is larger, the new element or the popped smallest element, gets re-added to the min-heap. Which again is holding the smallest values.

# So for add_stream_element, once the k largest elements have been added, an if statement can instead heappop the smallest element out, see if that or the element to be added is larger, and add the larger element thru heappush.

# For k_largest, we know the heap can't be larger than k and since it doesn't need to be sorted, just return the array data structure. For me that's self.heap.

  def add_stream_element(self, e: int) -> None:
    if len(self.heap) < self.k:
      heapq.heappush(self.heap, e)
    elif len(self.heap) == self.k:
      # heapq.heappushpop(self.heap, e)
      val = heapq.heappop(self.heap)
      if e > val:
        heapq.heappush(self.heap, e)
      else:
        heapq.heappush(self.heap, val)
    return None

  ''' 
  This method returns the k largest elements seen so far.
  '''
  def k_largest(self) -> list[int]:
    return self.heap

# TODO explain the differences

class StreamHandlerKSmallest:
  def __init__(self, k: int) -> None:
    self.k = k
    self.heap = []
  
  '''
  This method adds the stream element to the collection. 
  You only need to store the k smallest elements seen so far at any given point in time.
  '''
  # For doing k smallest stuff, every number is negated because that way the "smallest" number goes to the top of the binary heap or the most to the left in the array data structure. This number is actually the largest when it is not negative. Then when the heap has to pop out the "smallest" number, it will pop out the most negative number which when negated is actually the biggest number.

  # 2nd comment section
  # For which element to keep between the popped and the next value
  # Whichever value is larger is actually smaller since they are both negative
  # So if the incoming value to add, e, is 9. Then it's -e so -9 and the popped element is already negative from being in the heap thru add_stream_element
  # So if the popped element is -7, then -7 is technically larger than -9 and so put the "larger" value back into the heap which is for the smallest elements.

  # k_smallest needs to undo the negation so can do a for loop and negate the output again so the double negative makes them all positive. Order doesn't matter.

  def add_stream_element(self, e: int) -> None: 
    if len(self.heap) < self.k:
      heapq.heappush(self.heap, -e)
    elif len(self.heap) == self.k:
      # heapq.heappushpop(self.heap, -e)
      val = heapq.heappop(self.heap)
      # 2nd comment section
      if -e < val:
        heapq.heappush(self.heap, val)
      else:
        heapq.heappush(self.heap, -e)
    return None

  ''' 
  This method returns the k smallest elements seen so far.
  '''
  def k_smallest(self) -> list[int]: 
    return [-m for m in self.heap]

''' 
Write a function that creates a copy of the list, and sorts it in ascending order
using a heap.
'''
# To make a copy, add everything to a heap (can use heapify to do it one go with the incoming array). Go thru the input list, keep popping values. The smallest values will be coming out first so they can be added first to a new array. That way the smallest values are first and largest are last aka ascending.

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

# The heap has to have the score value stored for the heap to compare them
# A score method can be added to do the basic math
# The comparisons can be done either with a comparison being added to the object for less than since we need to measure what is smaller for a min-heap.
# Or can add the score and the tuples to a min-heap. This would require negating the scores at first so that the min-heap can properly have the largest scores be at the top (by being negated and seeming to be the smallest since we want to order by the greater the datapoint)
# The comparison less than is inverted so the max goes to the "top" (lowest index in array) of heap

# Then with the comparison, get_top_k_datapoints just requires adding everything to the tuple and then looping k times, adding each popped (aka largest first) scores added to the set, but add the Datapoint that is popped to the set via to_tuple().

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
  for _ in range(k):
    final.add(heapq.heappop(data_collection).to_tuple())
  return final
