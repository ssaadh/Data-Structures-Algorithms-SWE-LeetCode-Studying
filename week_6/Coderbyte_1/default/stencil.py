from __future__ import annotations

'''
Given a DAG that is represented as a collection of edges, i.e. ["n1", "n2"] means that n1 precedes n2 (visually, n1 -> n2),
'''

'''
Create an adjacency list for it.
'''
def to_adjacency_list(edges: list[list[str]]) -> dict[str, list[str]]:
  pass

'''
Create an adjacency matrix for it where each 
respective cell contains 0 for unconnected and 1 for connected.
Index 0 represents "v1" and so on. 
'''
def to_adjacency_matrix(edges: list[list[str]]) -> list[list[int]]:
  pass

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
