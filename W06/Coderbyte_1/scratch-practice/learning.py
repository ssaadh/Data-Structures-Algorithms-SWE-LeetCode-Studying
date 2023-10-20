from stencil_1 import to_adjacency_list
from collections import deque

def find_shortest_path_distance(s: str, d: str, edges: list[list[str]]) -> int:
  # on positive, uniform weight, graphs first BFS solution is optimal
  adjacency_list = to_adjacency_list(edges)
  agenda: deque[list[str]] = deque()  # can reduce space complexity via deque[tuple[str, int]] (last node, length)
  # visited: set[str] = set()  # detects/avoids loops when not recording paths
  agenda.append([s])
  while agenda:
    current_path = agenda.popleft()
    for neighbor in adjacency_list[current_path[-1]]:
      # if neighbor not in current_path:  # can be used to exclude loops
      extended_path = current_path + [neighbor]
      agenda.append(extended_path)
      if neighbor is d:
        return len(extended_path) - 1
  return -1

edges = [["v1", "v2"], ["v1", "v3"], ["v2", "v4"], ["v2", "v5"], ["v4", "v3"], ["v5", "v6"], ["v6", "v4"]]
print(find_shortest_path_distance("v1", "v4", edges))
