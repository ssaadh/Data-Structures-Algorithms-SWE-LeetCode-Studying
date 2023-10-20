
from collections import deque, defaultdict
import heapq

from stencil import to_adjacency_list

# def find_shortest_path_distance(s: str, d: str, edges: list[list[str]]) -> int:
def fsp(s: str, d: str, edges: list) -> int:
  # Convert the edge list to an adjacency list
  adjacency_list = to_adjacency_list(edges)

  # Create a set to keep track of visited nodes
  visited = set()

  # Create a queue for the BFS, each element in the queue is a tuple (node, distance)
  queue = deque([(s, 0)])
  # queue = deque([(s, [])])

  while queue:
    # Dequeue a node and its distance from the source node
    node, distance = queue.popleft()
    # node, path = queue.popleft()

    # If this node is the destination, return its distance from the source
    if node == d:
      return distance
      # return path + [node]

    # If this node has not been visited before
    if node not in visited:
      # Mark it as visited
      visited.add(node)

      # Enqueue all its unvisited neighbors, their distances from the source are the current node's distance + 1
      if node in adjacency_list:
      # if node in adjacency_list:
        for neighbor in adjacency_list[node]:
          if neighbor not in visited:
            queue.append((neighbor, distance + 1))
            # queue.append((neighbor, path + [node]))

  # If we have exhausted all nodes and haven't found the destination, return -1
  return -1
  # return []

# def find_shortest_path_distance(s: str, d: str, edges: list[list[str]]) -> int:
def find_shortest_path_distance(s: str, d: str, edges: list) -> int:
  # Convert the edge list to an adjacency list
  adjacency_list = to_adjacency_list(edges)

  # Create a set to keep track of visited nodes
  visited = set()

  # Create a queue for the BFS, each element in the queue is a tuple (node, distance)
  queue = deque([(s, 0)])

  while queue:
    # Dequeue a node and its distance from the source node
    node, distance = queue.popleft()

    # If this node is the destination, return its distance from the source
    if node == d:
      return distance

    # If this node has not been visited before
    if node not in visited:
      # Mark it as visited
      visited.add(node)

      # Enqueue all its unvisited neighbors, their distances from the source are the current node's distance + 1
      if node in adjacency_list:
        for neighbor in adjacency_list[node]:
          if neighbor not in visited:
            queue.append((neighbor, distance + 1))

  # If we have exhausted all nodes and haven't found the destination, return -1
  return -1

# def find_shortest_path(s: str, d: str, edges: list[list[str]]) -> list[str]:
def find_shortest_path(s: str, d: str, edges: list) -> list:
  # Convert the edge list to an adjacency list
  adjacency_list = to_adjacency_list(edges)

  # Create a set to keep track of visited nodes
  visited = set()

  # Create a queue for the BFS, each element in the queue is a tuple (node, path)
  queue = deque([(s, [])])

  while queue:
    # Dequeue a node and the path from the source to this node
    node, path = queue.popleft()
    print("node: ", node)
    print("path: ", path)

    # If this node is the destination, return the path from the source to this node
    if node == d:
      return path + [node]

    # If this node has not been visited before
    if node not in visited:
      # Mark it as visited
      visited.add(node)
      
      print("visited: ", visited)

      # Enqueue all its unvisited neighbors, their paths from the source are the current node's path + the current node
      for neighbor in adjacency_list[node]:
        if neighbor not in visited:
          queue.append((neighbor, path + [node]))
          print("queue: ", queue)
  
  print('--')
  print(queue)
  # If we have exhausted all nodes and haven't found the destination, return an empty list
  return []

# def find_shortest_path_wt(s: str, d: str, edges: list[list[str]], k: int) -> list[str]:
def find_shortest_path_wt(s: str, d: str, edges: list, k: int) -> list:
  # Convert the edge list to an adjacency list
  adjacency_list = to_adjacency_list(edges)

  # Create a dictionary to store the shortest distance from the source to each node, initialized with infinity
  distances = defaultdict(lambda: float('inf'))

  # Create a dictionary to store the previous node on the shortest path from the source to each node
  previous_nodes = {}

  # Create a priority queue for Dijkstra's algorithm, each element in the queue is a tuple (distance, node)
  priority_queue = [(0, s)]

  while priority_queue:
    # Dequeue the node with the smallestdistance from the source
    current_distance, node = heapq.heappop(priority_queue)

    # If this is the shortest distance from the source to this node
    if current_distance < distances[node]:
      # Update the shortest distance
      distances[node] = current_distance

      # Update the previous node on the shortest path
      for neighbor in adjacency_list[node]:
        distance = current_distance + k
        if distance < distances[neighbor]:
          # If we have found a shorter path to the neighbor
          # Enqueue the neighbor and its distance from the source
          heapq.heappush(priority_queue, (distance, neighbor))

          # Update the shortest distance from the source to the neighbor
          previous_nodes[neighbor] = node

  # If we have found a path from the source to the destination
  path, current_node = [], d
  while previous_nodes.get(current_node) is not None:
    # Add the current node to the path
    path.append(current_node)

    # Move to the previous node on the path
    current_node = previous_nodes[current_node]

  # If we have found a path from the source to the destination
  if path:
    # Add the source to the path
    path.append(s)

  # Return the path from the source to the destination
  return path[::-1]

edges = [["v1", "v2"], ["v1", "v3"], ["v2", "v4"], ["v2", "v5"], ["v4", "v3"], ["v5", "v6"], ["v6", "v4"]]
courses = [[0, 1], [1, 2], [0, 2], [1, 3],[2, 3]]
courses_none = [[0, 1], [1, 2], [2, 0]]

print(find_shortest_path("v1", "v4", edges))
# print(find_shortest_path_distance("v4", "v5", edges))

# 2
# print(find_shortest_path_distance("v1", "v4", edges))
# -1
# WRONG
# ["v1", "v2", "v4"]
# print(find_shortest_path("v1", "v4", edges))
# ["v1", "v2", "v5", "v6"]
# print(find_shortest_path("v1", "v6", edges))
# ["v1", "v2", "v5", "v6"]
# print(find_shortest_path_wt("v1", "v6", edges, 5))
