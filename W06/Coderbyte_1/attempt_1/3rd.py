from collections import deque, defaultdict
import heapq

# def find_valid_course_ordering_if_exists(prerequisites: list[list[int]], n: int) -> list[int] | None:
def find_valid_course_ordering_if_exists(prerequisites: list, n: int):
  # Create an adjacency list representation of the graph
  adjacency_list = defaultdict(list)
  # Create an array to keep track of the in-degree of each node
  in_degree = [0] * n
  for course, prerequisite in prerequisites:
  # Add the edge to the adjacency list
    adjacency_list[prerequisite].append(course)
    # Increase the in-degree of the course
    in_degree[course] += 1

  # Create a queue and add all nodes with in-degree 0 to it
  queue = deque([course for course in range(n) if in_degree[course] == 0])
  # Create a list to keep track of the course order
  course_order = []

  while queue:
    # Dequeue a course
    course = queue.popleft()
    # Add the course to the course order
    course_order.append(course)

    # Decrease the in-degree of all courses that have this course as a prerequisite
    for next_course in adjacency_list[course]:
      in_degree[next_course] -= 1
      # If the in-degree of a course becomes 0, add it to the queue
      if in_degree[next_course] == 0:
        queue.append(next_course)

  # If we have added all courses to the course order, return it
  # Otherwise, return None because a valid course order does not exist
  return course_order if len(course_order) == n else None

# def output_mst(edges: list[tuple[str, str, int]]) -> list[tuple[str, str, int]]:
def output_mst(edges: list) -> list:
  # Create an adjacency list representation of the graph
  adjacency_list = defaultdict(list)
  for edge in edges:
    # Add the edge to the adjacency list in both directions
    adjacency_list[edge[0]].append((edge[1], edge[2]))
    adjacency_list[edge[1]].append((edge[0], edge[2]))

  # Create a list to keep track of the edges in the minimum spanning tree (MST)
  mst = []
  # Create a set to keep track of visited nodes
  visited = set()
  # Create a priority queue and add an arbitrary node to it
  priority_queue = [(0, edges[0][0], None)]

  while priority_queue:
    # Dequeue the node with the smallest weight
    weight, node, previous_node = heapq.heappop(priority_queue)

    # If this node has not been visited before
    if node not in visited:
      # Mark it as visited
      visited.add(node)
      # If this node is not the initial node, add the edge from the previous node to this node to the MST
      if previous_node is not None:
        mst.append((previous_node, node, weight))

      # Enqueue all unvisited neighbors of this node
      for neighbor, weight in adjacency_list[node]:
        if neighbor not in visited:
          heapq.heappush(priority_queue, (weight, neighbor, node))

  # Return the edges in the MST
  return mst

courses = [[0, 1], [1, 2], [0, 2], [1, 3],[2, 3]]
courses_none = [[0, 1], [1, 2], [2, 0]]

graph = []
graph.append(("e1", "e2" , 6))
graph.append(("e2", "e3", 2))
graph.append(("e1", "e3" , 4))
graph.append(("e4", "e5" , 3))
graph.append(("e1", "e4" , 5))

mst = [("e2", "e3", 2), ("e4", "e5" , 3), ("e1", "e3" , 4), ("e1", "e4" , 5)]

# [0, 1, 2, 3]
print(find_valid_course_ordering_if_exists(courses, 4))
# None
print(find_valid_course_ordering_if_exists(courses_none, 4))
# set(mst)
print(set(output_mst(graph)) == set(mst))
