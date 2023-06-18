from __future__ import annotations 
import unittest
from point import Point
from tour import Tour

class TestPoint(unittest.TestCase):

    def test_string(self):
        a = Point(1,2)
        self.assertEqual(str(a), '(1,2)')
    
    def test_distance(self):
        a = Point(0,0)
        b = Point(0,2)
        self.assertEqual(a.distance_to(b), 2.0)

        c = Point(4,5)
        d = Point(1,1)
        self.assertEqual(c.distance_to(d), 5.0)


        e = Point(1,7)
        f = Point(13,2)
        self.assertEqual(e.distance_to(f), 13.0)

def read_point_file(filename: str):
    point_list = []
    with open(filename) as f:
        lines = f.readlines()
        for line in lines:
            row = line.split()
            x = float(row[0])
            y = float(row[1])
            p = Point(x,y)
            point_list.append(p)
    return point_list

class TestTour(unittest.TestCase):
    tsp_2 = read_point_file('coderbyte-tests/test_data/tsp2.txt')
    tsp_3 = read_point_file('coderbyte-tests/test_data/tsp3.txt')
    tsp_10 = read_point_file('coderbyte-tests/test_data/tsp10.txt')
    tsp_100 = read_point_file('coderbyte-tests/test_data/tsp100.txt')
    tsp_1000 = read_point_file('coderbyte-tests/test_data/tsp1000.txt')


    def test_tour_simple_example(self):
        coordinates = [
            (0,0),
            (3,0),
            (0,4)
        ]

        tour = Tour()
        
        for x,y in coordinates:
            p = Point(x,y)
            tour.insert_nearest(p)
        
        self.assertEqual(tour.size(), 3)
        self.assertEqual(tour.distance(), 12.0)

    def test_duplicates(self):
        coordinates = [
            (0,0),
            (3,0),
            (0,4),
            (0,0),
            (0,0),
            (0,4)
        ]

        tour = Tour()
        
        for x,y in coordinates:
            p = Point(x,y)
            tour.insert_smallest(p)
        
        self.assertEqual(tour.size(), 6)
        self.assertEqual(tour.distance(), 12.0)


    def test_empty_tour(self):
        tour = Tour()
        self.assertEqual(tour.size(), 0)
        self.assertEqual(tour.distance(), 0)


    def test_tsp_2_insert_smallest(self):
        smallest_tour = Tour()
        for p in self.tsp_2:
            smallest_tour.insert_smallest(p)
        self.assertAlmostEqual(smallest_tour.distance(), 565.68542, places = 2)   
        self.assertEqual(smallest_tour.size(), 2)

    def test_tsp_3_insert_smallest(self):
        smallest_tour = Tour()
        for p in self.tsp_3:
            smallest_tour.insert_smallest(p)
        self.assertAlmostEqual(smallest_tour.distance(), 832.4555320336758, places = 2)   
        self.assertEqual(smallest_tour.size(), 3)

    def test_tsp_10_insert_smallest(self):
        smallest_tour = Tour()
        for p in self.tsp_10:
            smallest_tour.insert_smallest(p)
        self.assertAlmostEqual(smallest_tour.distance(), 1655.7461857661865, places = 2)   
        self.assertEqual(smallest_tour.size(), 10)

    def test_tsp_100_insert_smallest(self):
        smallest_tour = Tour()
        for p in self.tsp_100:
            smallest_tour.insert_smallest(p)
        self.assertAlmostEqual(smallest_tour.distance(), 4887.219040311983, places = 2)   
        self.assertEqual(smallest_tour.size(), 100)


    def test_tsp_1000_insert_smallest(self):
        smallest_tour = Tour()
        for p in self.tsp_1000:
            smallest_tour.insert_smallest(p)
        self.assertAlmostEqual(smallest_tour.distance(), 17265.6282, places = 2)
        self.assertEqual(smallest_tour.size(), 1000)


    def test_tsp_2_insert_nearest(self):
        nearest_tour = Tour()
        for p in self.tsp_2:
            nearest_tour.insert_nearest(p)
        self.assertAlmostEqual(nearest_tour.distance(), 565.68542, places = 4)   
        self.assertEqual(nearest_tour.size(), 2)

    def test_tsp_3_insert_nearest(self):
        nearest_tour = Tour()
        for p in self.tsp_3:
            nearest_tour.insert_nearest(p)
        self.assertAlmostEqual(nearest_tour.distance(),  832.4555320336758, places = 4)   
        self.assertEqual(nearest_tour.size(), 3)

    def test_tsp_10_insert_nearest(self):
        nearest_tour = Tour()
        for p in self.tsp_10:
            nearest_tour.insert_nearest(p)
        self.assertAlmostEqual(nearest_tour.distance(), 1566.1363051360363, places = 4)   
        self.assertEqual(nearest_tour.size(), 10)

    def test_tsp_100_insert_nearest(self):
        nearest_tour = Tour()
        for p in self.tsp_100:
            nearest_tour.insert_nearest(p)
        self.assertAlmostEqual(nearest_tour.distance(),  7389.929676351667, places = 4)   
        self.assertEqual(nearest_tour.size(), 100)

    def test_tsp_1000_insert_nearest(self):
        nearest_tour = Tour()
        for p in self.tsp_1000:
            nearest_tour.insert_nearest(p)
        self.assertAlmostEqual(nearest_tour.distance(), 27868.7106, places = 4)   
        self.assertEqual(nearest_tour.size(), 1000)