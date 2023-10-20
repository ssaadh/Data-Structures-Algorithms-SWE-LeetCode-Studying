from collections import deque, defaultdict

def to_adjacency_list(edges: list) -> dict:
    # Create an adjacency list representation of the graph
    adjacency_list = defaultdict(list)
    for edge in edges:
        adjacency_list[edge[0]].append(edge[1])
        adjacency_list[edge[1]].append(edge[0])
    return adjacency_list

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
            for neighbor in adjacency_list[node]:
                if neighbor not in visited:
                    queue.append((neighbor, distance + 1))

    # If we have exhausted all nodes and haven't found the destination, return -1
    return -1

edges = [["v1", "v2"], ["v1", "v3"], ["v2", "v4"], ["v2", "v5"], ["v4", "v3"], ["v5", "v6"], ["v6", "v4"]]
print(find_shortest_path_distance("v4", "v5", edges))
