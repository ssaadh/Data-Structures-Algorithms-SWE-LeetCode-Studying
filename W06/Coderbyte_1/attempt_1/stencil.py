from __future__ import annotations

'''
Given a DAG that is represented as a collection of edges, i.e. ["n1", "n2"] means that n1 precedes n2 (visually, n1 -> n2),
'''

'''
Create an adjacency list for it.
'''
# def to_adjacency_list(edges: list[list[str]]) -> dict[str, list[str]]:
def to_adjacency_list(edges: list) -> dict:
  edge_dict = dict()
  for edge_1,edge_2 in edges:
    if edge_1 not in edge_dict:
      edge_dict[edge_1] = [edge_2]
    elif edge_1 in edge_dict:
      edge_dict[edge_1].append(edge_2)
    if edge_2 not in edge_dict:
      edge_dict[edge_2] = []
  return edge_dict

'''
Create an adjacency matrix for it where each 
respective cell contains 0 for unconnected and 1 for connected.
Index 0 represents "v1" and so on. 
'''
# def to_adjacency_matrix(edges: list[list[str]]) -> list[list[int]]:
#   k = []
#   for e in edges:
#   for n in edge:
#     if n not in k:
#     k.append(n)
    
def to_adjacency_matrix(edges: list[list[str]]) -> list[list[int]]:
  # We need a list of unique nodes to determine the size of our matrix.
  # We're also sorting the nodes to ensure a consistent ordering.
  nodes = []
  for edge in edges:
    for node in edge:
      if node not in nodes:
        nodes.append(node)
  nodes.sort()

  # We create a dictionary mapping each node to its index in the sorted list.
  # This will allow us to quickly find the correct row and column in the matrix for each edge.
  node_indices = {}
  for index, node in enumerate(nodes):
    node_indices[node] = index

  # print('-node_indices-')
  # print(node_indices)

  # We initialize an empty matrix of the correct size.
  # The matrix is a 2D list, with the same number of rows and columns as there are nodes.
  # Initially, all values are 0, indicating no connections between nodes.
  matrix = []
  for _ in nodes:
    row = []
    for _ in nodes:
      row.append(0)
    matrix.append(row)

  # print('-matrix-')
  # print(matrix)

  # We iterate over the edges, and for each edge, we set the corresponding cell in the matrix to 1.
  # This indicates that there is a connection from the first node in the edge to the second.
  for k,j in edges:
    row = node_indices[k]
    col = node_indices[j]
    matrix[row][col] = 1

  # print('-matrix final-')
  
  return matrix

edges = [["v1", "v2"], ["v1", "v3"], ["v2", "v4"], ["v2", "v5"], ["v4", "v3"], ["v5", "v6"], ["v6", "v4"]]
print(to_adjacency_matrix(edges))

'''
Suppose you’re given a list of graph edges where 
each edge is of the form ["e1", "e2"], meaning that 
"e1" is connected to "e2". You’re also given a source 
node s and destination node d.
'''

'''
Write an algorithm to return the distance of one of the shortest paths, 
where each connection costs 1 to traverse. Return -1 if there is no path.
'''
def find_shortest_path_distance(s: str, d: str, edges: list[list[str]]) -> int:
  pass

'''
Modify the above algorithm to return the path itself. 
For the test inputs, the path will always exist.
'''
def find_shortest_path(s: str, d: str, edges: list[list[str]]) -> list[str]:
  pass

'''
Modify the above algorithm to work if each connection costs k where k > 0.
'''
def find_shortest_path_wt(s: str, d: str, edges: list[list[str]], k: int) -> list[str]:
  pass

'''
Given a list of course prerequisites each in the form [0, 1] 
where 0 is a prerequisite of 1 and n, the total number of courses, 
write a function to output a valid course ordering, 
or None if not possible. Courses are numbered from 0 to n-1.
'''
def find_valid_course_ordering_if_exists(prerequisites: list[list[int]], n: int) -> list[int] | None:
  pass

'''
Suppose you’re given a list of graph edges where each edge is of the form 
("e1", "e2", 3), meaning that "e1" is connected to "e2" and has an 
edge weight of 3. The graph is connected. Write an algorithm to print 
out the an MST of the graph.

You can assume the graph is undirected for this problem. 
If there is an edge (e1, e2, 3) in the input,
you should assume there is an equivalent edge (e2, e1, 3) as well.
'''
def output_mst(edges: list[tuple[str, str, int]]) -> list[tuple[str, str, int]]:
  pass