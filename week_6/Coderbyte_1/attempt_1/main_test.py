from stencil import *

adj_list = {}
adj_list["v1"] = ["v2", "v3"]
adj_list["v2"] = ["v4", "v5"]
adj_list["v3"] = []
adj_list["v4"] = ["v3"]
adj_list["v5"] = ["v6"]
adj_list["v6"] = ["v4"]

adj_matrix = [
  [0, 1, 1, 0, 0, 0],
  [0, 0, 0, 1, 1, 0],
  [0, 0, 0, 0, 0, 0],
  [0, 0, 1, 0, 0, 0],
  [0, 0, 0, 0, 0, 1],
  [0, 0, 0, 1, 0, 0]
]

edges = [["v1", "v2"], ["v1", "v3"], ["v2", "v4"], ["v2", "v5"], ["v4", "v3"], ["v5", "v6"], ["v6", "v4"]]
courses = [[0, 1], [1, 2], [0, 2], [1, 3],[2, 3]]
courses_none = [[0, 1], [1, 2], [2, 0]]

graph = []
graph.append(("e1", "e2" , 6))
graph.append(("e2", "e3", 2))
graph.append(("e1", "e3" , 4))
graph.append(("e4", "e5" , 3))
graph.append(("e1", "e4" , 5))

mst = [("e2", "e3", 2), ("e4", "e5" , 3), ("e1", "e3" , 4), ("e1", "e4" , 5)]

def test_to_adjacency_list_1():
  assert to_adjacency_list(edges) == adj_list

def test_to_adjacency_matrix_1():
  assert to_adjacency_matrix(edges) == adj_matrix

def test_find_shortest_path_distance_1():
  assert find_shortest_path_distance("v1", "v4", edges) == 2

def test_find_shortest_path_distance_2():
  assert find_shortest_path_distance("v4", "v5", edges) == -1

def test_find_shortest_path_1():
  assert find_shortest_path("v1", "v4", edges) == ["v1", "v2", "v4"]

def test_find_shortest_path_2():
  assert find_shortest_path("v1", "v6", edges) == ["v1", "v2", "v5", "v6"]

def test_find_shortest_path_wt_1():
  assert find_shortest_path_wt("v1", "v6", edges, 5) == ["v1", "v2", "v5", "v6"]

def test_find_valid_course_ordering_if_exists_1():
  assert find_valid_course_ordering_if_exists(courses, 4) == [0, 1, 2, 3]

def test_find_valid_course_ordering_if_exists_2():
  assert find_valid_course_ordering_if_exists(courses_none, 4) == None

def test_output_mst_1():
  assert set(output_mst(graph)) == set(mst)