from __future__ import annotations

'''
Tour class which is a collection of ordered points.
The functions allow you to insert points in a way that will 
keep the distance of the tour as small as possible.
Each Tour object should be able to print out the points in order, 
count its number of points, compute its total distance, 
and insert a new point using either of the two heuristics. 
The constructor creates an empty tour.
'''

from point import Point

# Hint: You will want to use a classic LinkedList Node to implement the tour.
class Node:
  def __init__(self, point):
    # This node's point 
    self.point = point

    # The next node
    self.next = None 

class Tour:
  # Creates an empty tour
  # Initialize any instance variables you think are needed.
  def __init__(self):
    self.head = None
    self._count = 0

  # Returns string representation of the Tour.
  # Should output a list of all points on the Tour.
  def __str__(self):
    if self.head == None:
      return ''
    curr = self.head
    arr = []
    arr.append('(')
    arr.append(curr.point)
    while curr is not None:
      curr = curr.next
      arr.append(',')
      arr.append(curr.point)
    arr.append(')')
    return ''.join(arr)

  # return the number of points on tour
  # Hint: You should not have to iterate through the entire Tour to get the size.
  def size(self):
    return self._count

  # Computers and returns the distance of entire tour
  def distance(self):
    if self.head == None:
      return 0
    curr = self.head
    total = curr.point.distance_to(curr.next.point)
    curr = curr.next
    while curr is not self.head:
      total += curr.point.distance_to(curr.next.point)
      curr = curr.next
    return total


  # Helper function to insert a new point p into the Tour after a previous Node prev.
  # Example if the tour is a -> b -> c -> d
  # And you call _insert_at(p, c). Then the Tour should look like.
  # a -> b -> c -> p -> d
  # You can use this helper function in the insertNearest and insertSmallest
  # once you find the point you should insert p after.
  def _insert_at(self, p, prev: Node):
    # new node
    new_node = Node(p)
    # prev next becomes new node next
    new_node.next = prev.next
    # new node becomes prev next
    prev.next = new_node
    # increment size
    self._count += 1

  # Insert a new Point p to the Tour using neearest neighbor heuristic
  def insert_nearest(self, p):
    if self.head == None:
      self.head = Node(p)
      self.head.next = self.head
      self._count += 1
    elif self.size() == 1:
      self._insert_at(p, self.head)
    else:
      curr = self.head
      new = Node(p)
      least = self.head
      dist = float('inf')
      # do
      diff = new.point.distance_to(curr.point)
      if dist > diff:
        dist = diff
        least = curr
      while curr.next is not self.head:
        curr = curr.next
        # find the smallest distance between new point and any current point    
        diff = new.point.distance_to(curr.point)
        if dist > diff:
          dist = diff
          least = curr
      self._insert_at(p, least)


  def _smallest(self, curr, new):
    # diff two original points/nodes as they are right now
    og = curr.point.distance_to(curr.next.point)
    # diff between two new points. the original node/point and the new distance to new node/point
    new_dist = new.point.distance_to(curr.point)
    # add new distance from new point and new next point (which is the original next point)
    new_dist += new.point.distance_to(curr.next.point)
    # subtract original diff from new distance
    return new_dist - og

  # Insert a new Point p to the Tour using smallest increase heuristic
  def insert_smallest(self, p):                
    if self.head == None:
      self.head = Node(p)
      self.head.next = self.head
      self._count += 1
    elif self.size() == 1:
      self._insert_at(p, self.head)
    else:
      curr = self.head
      new = Node(p)
      least = self.head
      dist = float('inf')
      # do
      diff = self._smallest(curr, new)
      if dist > diff:
        dist = diff
        least = curr
      while curr.next is not self.head:
        curr = curr.next
        diff = self._smallest(curr, new)
        # updating if smallest distance
        if dist > diff:
          dist = diff
          least = curr
      self._insert_at(p, least)
  