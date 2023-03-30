from __future__ import annotations 
from math import sqrt

# (2D point data type to model points in the plane.)
class Point: 
    # create the point (x, y)
    def __init__(self, x: float, y: float) -> None:
      self.x = x
      self.y = y

    # Returns a string representation of the point.
    # Should be in coordinate pair output with no spaces.
    # i.e. (x,y)
    def __str__(self) -> str:
      return("(%s,%s)"%(str(self.x), str(self.y)))

    # return Euclidean distance between the two points
    def distance_to(self, that: Point) -> float:
      return sqrt(
        (self.x - that.x) ** 2 + (self.y - that.y) ** 2
      )
      