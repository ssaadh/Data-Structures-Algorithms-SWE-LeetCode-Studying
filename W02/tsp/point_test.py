import unittest
from point import Point

class TestPoint(unittest.TestCase):
    
    def test_distance_example(self):
        a = Point(0,0)
        b = Point(0,2)
        self.assertEqual(a.distanceTo(b), 2.0)

        c = Point(4,5)
        d = Point(1,1)
        self.assertEqual(a.distanceTo(b), 5.0)

    # Please add tests to verify your Point class below.

if __name__ == '__main__':
    unittest.main()