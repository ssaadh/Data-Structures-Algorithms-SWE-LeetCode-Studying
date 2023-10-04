from stencil_1 import to_adjacency_list
from queue import Queue

# i0

# seen  = [v1]
# queue = [v1]

# i1
# 'v1': ['v2', 'v3']

# loop thru neighbors, add v2 and v3 to the queue.

# v1 now
# gone_to = [v1: None]

# seen = [v1, v2, v3]
# queue = [v2, v3]

# i2
# 'v2': ['v4', 'v5']

# v2 now
# gone_to = [v1: None, v2: v1]

# seen = [v1, v2, v3, v4, v5]
# queue = [v3, v4, v5]

# i3
# 'v3': []

# v3 now
# gone_to = [v1: None, v2: v1, v3: v1]

# seen = [v1, v2, v3, v4, v5]
# queue = [v4, v5]
# nothing happens

# 'v4': ['v3']

# v4 now
# gone_to = [v1: None, v2: v1, v3: v1, v4: v2]

# seen = [v1, v2, v3, v4, v5]
# queue = [v5]
# it matches

# 'v5': ['v6']
# 'v6': ['v4']

# with cur matching destination, reverse thru gone_to:

# v4 -> v2 -> v1
# 3 - 1 = 2
# Add the reverse path to an array and do an array count, or just do a counter and return that

# --

# Overall doing BFS for graphs. Put the edges through adj list function. Set up a queue and add/put the source vertex. Set up a seen set initialized with the source vertex as an array. Also set up a progress dictionary with the source vertex as the key and set the value to something like None. What you set the value to will matter later on*. Look into what the best data type for this is.
# Loop while the queue is not empty. Pop out the next queue item as the current vertex. For the first run through this will obviously be the source vertex.
# Now the equivalent of base cases. Check if the current vertex matches the destination vertex. If so, instantiate an array. Do a loop while the current vertex does not equal None*. Add the current vertex to the new array and to iterate, overwrite the current vertex to be its value in the progress dictionary. This is because later on we make the value of each key in the progress dictionary equal to the vertex it came from. Eventually this will get us back to the source index key with a value of None. Return the length of the new array minus 1.
# Loop through the neighbors of the current vertex in the adj list. Only add things in the loop if the current neighbor isn't in the seen set. If it has not been seen, add it to the seen set, the queue, and assign the neighbor key in the progress dictionary to the current vertex. This is to track that the neighbor is coming from the current vertex.

# --

# basic BFS with adj_list:
#   use a queue for the adj_list
#   make a seen set
#   loop thru the queue
#   cur = pop from queue
#   check if the cur is the destination
#     if so, we are done...
  
#     go thru the neighbors of the cur in adj list
#       if not in seen set
#         add to seen set
#         add to queue



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
  return -1



# This is the same as find_shortest_path_distance except return the reverse of the final array getting the vertices through the progress dictionary.

# # input = ("v1", "v4", [["v1", "v2"], ["v1", "v3"], ["v2", "v4"], ["v2", "v5"], ["v4", "v3"], ["v5", "v6"], ["v6", "v4"]])
# # output = ["v1", "v2", "v4"]
# # BFS
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
  return -1




# 'v1': ['v2', 'v3']
# 'v2': ['v4', 'v5']
# 'v3': []
# 'v4': ['v3']
# 'v5': ['v6']
# 'v6': ['v4']

# I don't think this is different. Uniform edge weights don't make a difference.

# # input = ("v1", "v6", [["v1", "v2"], ["v1", "v3"], ["v2", "v4"], ["v2", "v5"], ["v4", "v3"], ["v5", "v6"], ["v6", "v4"]], 5)
# # output = ["v1", "v2", "v5", "v6"]
def find_shortest_path_wt(s: str, d: str, edges: list[list[str]], k: int) -> list[str]:
  return find_shortest_path(s, d, edges)
