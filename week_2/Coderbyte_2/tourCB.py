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
      if self.head is None:
        return ''
      # do
      curr = self.get_head()
      full_string = curr.point.toString() + '\n '
      # while
      while curr.next is not self.head:
        curr = curr.next
        full_string += curr.point + '\n '
      return full_string

    # return the number of points on tour
    # Hint: You should not have to iterate through the entire Tour to get the size.

    def size(self):
        return self._count

    # Computers and returns the distance of entire tour
    def distance(self):
      if self.head is None:
        return 0

      # do
      curr = self.head
      total = curr.point.distance_to(curr.next.point)
      # while
      while curr.next is not self.head:
        curr = curr.next
        total += curr.point.distance_to(curr.next.point)
      return total

    # Helper function to insert a new point p into the Tour after a previous Node prev.
    # Example if the tour is a -> b -> c -> d
    # And you call _insert_at(p, c). Then the Tour should look like.
    # a -> b -> c -> p -> d
    # You can use this helper function in the insertNearest and insertSmallest
    # once you find the point you should insert p after.
    def _insert_at(self, p, prev: Node):
      new_node = Node(p)
      new_node.next = prev.next
      prev.next = new_node
      self._count += 1

    def _initial_insert(self, p):
      new_node = Node(p)
      self.head = new_node
      new_node.next = self.head
      self._count += 1

    # Insert a new Point p to the Tour using neearest neighbor heuristic
    def insert_nearest(self, p):
      if self.head is None:
        self._initial_insert(p)
      elif self.size() == 1:
        self._insert_at(p, self.head)
      else:
        # init
        curr = self.head
        new_node = Node(p)
        least_node = self.head
        least_distance = float('inf')

        # do
        diff = new_node.point.distance_to(curr.point)
        if least_distance > diff:
          least_distance = diff
          least_node = curr
        # while
        while curr.next is not self.head:
          curr = curr.next
          diff = new_node.point.distance_to(curr.point)
          if least_distance > diff:
            least_distance = diff
            least_node = curr
        # insert new node
        self._insert_at(p, least_node)

    def _smallest_diff(self, curr, new_node):
      # difference between the two inserts
      initial = curr.point.distance_to(curr.next.point)
      # subtract original distance, add 2 new distances
      new_distance = curr.point.distance_to(new_node.point)
      new_distance += new_node.point.distance_to(curr.next.point)
      return new_distance - initial

    # Insert a new Point p to the Tour using smallest increase heuristic
    def insert_smallest(self, p):
      if self.head is None:
        self._initial_insert(p)
      elif self.size() == 1:
        self._insert_at(p, self.head)
      else:
        # init
        curr = self.head
        new_node = Node(p)
        least_node = self.head
        least_distance = float('inf')

        # do
        diff = self._smallest_diff(curr, new_node)
        if least_distance > diff:
          least_distance = diff
          least_node = curr
        # while
        while curr.next is not self.head:
          curr = curr.next
          diff = self._smallest_diff(curr, new_node)
          if least_distance > diff:
            least_distance = diff
            least_node = curr
        # insert new node
        self._insert_at(p, least_node)
