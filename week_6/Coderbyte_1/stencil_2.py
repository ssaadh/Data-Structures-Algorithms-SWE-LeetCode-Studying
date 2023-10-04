from __future__ import annotations
from stencil_1 import to_adjacency_list
from queue import Queue

'''
Given a DAG that is represented as a collection of edges, i.e. ["n1", "n2"] means that n1 precedes n2 (visually, n1 -> n2),
'''

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
# input = ("v1", "v4", [["v1", "v2"], ["v1", "v3"], ["v2", "v4"], ["v2", "v5"], ["v4", "v3"], ["v5", "v6"], ["v6", "v4"]])
# output = 2

# BFS
def find_shortest_path_distance(s: str, d: str, edges: list[list[str]]) -> int:
  adj_list = to_adjacency_list(edges)
  queue = Queue()
  queue.put(s)
  seen = set(s)
  progress = dict()
  progress[s] = None
  while queue:
    curr = queue.get()
    if curr == d:
      res = []
      while curr is not None:
        res.append(curr)
        curr = progress[curr]
      return len(res) - 1
    
    for neighbor in adj_list[curr]:
      if neighbor not in seen:
        seen.add(neighbor)
        queue.put(neighbor)
        progress[neighbor] = curr

'''
Modify the above algorithm to return the path itself. 
For the test inputs, the path will always exist.
'''
# input = ("v1", "v4", [["v1", "v2"], ["v1", "v3"], ["v2", "v4"], ["v2", "v5"], ["v4", "v3"], ["v5", "v6"], ["v6", "v4"]])
# output = ["v1", "v2", "v4"]

# BFS
def find_shortest_path(s: str, d: str, edges: list[list[str]]) -> list[str]:
  adj_list = to_adjacency_list(edges)
  queue = Queue()
  queue.put(s)
  seen = set(s)
  progress = dict()
  progress[s] = None
  while queue:
    curr = queue.get()
    if curr == d:
      res = []
      while curr is not None:
        res.append(curr)
        curr = progress[curr]
      res.reverse()
      return res
    
    for neighbor in adj_list[curr]:
      if neighbor not in seen:
        seen.add(neighbor)
        queue.put(neighbor)
        progress[neighbor] = curr

'''
Modify the above algorithm to work if each connection costs k where k > 0.
'''
# input = ("v1", "v6", [["v1", "v2"], ["v1", "v3"], ["v2", "v4"], ["v2", "v5"], ["v4", "v3"], ["v5", "v6"], ["v6", "v4"]], 5)
# output = ["v1", "v2", "v5", "v6"]

# wait why is this different?
# BFS still??
def find_shortest_path_wt(s: str, d: str, edges: list[list[str]], k: int) -> list[str]:
  return find_shortest_path(s, d, edges)
