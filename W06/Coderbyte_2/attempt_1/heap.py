import heapq

# L
class StreamHandlerKLargest:
  def __init__(self, k: int) -> None:
    # Initialize the capacity k
    self.k = k
    # Create a min-heap to store the k largest elements
    self.min_heap = []

  def add_stream_element(self, e: int) -> None: 
    # If the heap is not full, add the element to the heap
    if len(self.min_heap) < self.k:
      heapq.heappush(self.min_heap, e)
    # If the heap is full and the new element is larger than the smallest element in the heap
    # Replace the smallest element with the new element
    elif e > self.min_heap[0]:
      heapq.heapreplace(self.min_heap, e)

  # # def k_largest(self) -> list[int]: 
  def k_largest(self) -> list: 
    # Return the k largest elements in descending order
    return sorted(self.min_heap, reverse=True)

# M
class StreamHandlerKSmallest:
  def __init__(self, k: int) -> None:
    # Initialize the capacity k
    self.k = k
    # Create a max-heap to store the k smallest elements
    # We negate the elements before adding them to the heap, so the largest element becomes the smallest
    self.max_heap = []

  def add_stream_element(self, e: int) -> None: 
    # If the heap is not full, add the negated element to the heap
    if len(self.max_heap) < self.k:
      heapq.heappush(self.max_heap, -e)
    # If the heap is full and the new element is smaller than the largest element in the heap
    # Replace the largest element with the new element
    # We negate the elements before comparing them, so the smallest element becomes the largest
    elif e < -self.max_heap[0]:
      heapq.heapreplace(self.max_heap, -e)


  # def k_smallest(self) -> list[int]: 
  def k_smallest(self) -> list: 
    # Return the k smallest elements in ascending order
    # We negate the elements before returning them, so they become positive again
    return sorted([-e for e in self.max_heap])

''' 
Write a function that creates a copy of the list, and sorts it in ascending order
using a heap.
'''
# R
# def heapsort(input_list: list[int]) -> list[int]: 
def heapsort(input_list: list) -> list: 
  # Create a copy of the input list
  input_list = input_list[:]
  # Transform the list into a heap
  heapq.heapify(input_list)
  # Pop the smallest element from the heap and add it to the sorted list, until the heap is empty
  return [heapq.heappop(input_list) for _ in range(len(input_list))]


# R
class Datapoint:
  def __init__(self, a: int, b: int, c: int) -> None:
    # Initialize the attributes a, b, and c
    self.a = a
    self.b = b
    self.c = c
    # Calculate the score of the datapoint
    self.score = 2*a + 5*b + 10*c

  # def to_tuple(self) -> tuple[int, int, int]:
  def to_tuple(self) -> tuple:
    # Return the attributes a, b, and c as a tuple
    return (self.a, self.b, self.c)

  def __lt__(self, other):
    # Compare two datapoints based on their scores
    return self.score < other.score

# def get_top_k_datapoints(data_collection: list[Datapoint], k: int) -> set[tuple[int, int, int]]:
def get_top_k_datapoints(data_collection: list, k: int) -> set:
  # Create a min-heap to store the top k datapoints
  min_heap = []
  for datapoint in data_collection:
    # If the heap is not full, add the datapoint to the heap
    if len(min_heap) < k:
      heapq.heappush(min_heap, datapoint)
    # If the heap is full and the new datapoint's score is larger than the smallest score in the heap
    # Replace the datapoint with the smallest score with the new datapoint
    elif datapoint.score > min_heap[0].score:
      heapq.heapreplace(min_heap, datapoint)
  # Return the top k datapoints as tuples
  return {datapoint.to_tuple() for datapoint in min_heap}

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

print('-k largest-')
shkl1.k_largest() == []
print(sorted(shkl2.k_largest()) == [3, 5])
print(sorted(shkl3.k_largest()) == [5, 7, 9])
print(sorted(shkl4.k_largest()) == [5, 7, 9])

print('-k smallest-')
shks1.k_smallest() == []
print(sorted(shks2.k_smallest()) == [3, 5])
print(sorted(shks3.k_smallest()) == [3, 5, 7])
print(sorted(shks4.k_smallest()) == [3, 5, 7])

print('-heapsort-')
print(heapsort([9, 6, 2, 11, 15]) == [2, 6, 9, 11, 15])

print(get_top_k_datapoints([Datapoint(1,2,3), Datapoint(2,3,1), Datapoint(3,2,1)], 2) == set([(1,2,3), (2,3,1)]))
