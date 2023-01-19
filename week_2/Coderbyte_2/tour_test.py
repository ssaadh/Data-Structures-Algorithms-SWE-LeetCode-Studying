import unittest
from point import Point
from tour import Tour

class TestTour(unittest.TestCase):
    
    def test_tour_simple_example(self):
        coordinates = [
            (0,0),
            (3,0),
            (0,4)
        ]

        tour = Tour()
        
        for x,y in coordinates:
            p = Point(x,y)
            tour.insert_smallest(p)
        
        self.assertEqual(tour.size(), 3)
        self.assertEqual(tour.distance(), 12.0)

    def test_empty_tour(*self):
        tour = Tour()
        self.assertEqual(tour.size(), 0)
        self.assertEqual(tour.distance(), 0)

    # Please add additional tests to verify your Tour class below.

if __name__ == '__main__':
    unittest.main()