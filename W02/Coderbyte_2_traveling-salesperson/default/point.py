from __future__ import annotations 

# (2D point data type to model points in the plane.)
class Point: 
    # create the point (x, y)
    def __init__(self, x: float, y: float) -> None:
        pass

    # Returns a string representation of the point.
    # Should be in coordinate pair output with no spaces.
    # i.e. (x,y)
    def __str__(self) -> str:
        pass

    # return Euclidean distance between the two points
    def distance_to(self, that: Point) -> float:
        pass
