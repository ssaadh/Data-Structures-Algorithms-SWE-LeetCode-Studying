from stencil import to_adjacency_list

'''
Create an adjacency matrix for it where each 
respective cell contains 0 for unconnected and 1 for connected.
Index 0 represents "v1" and so on. 
'''
# def to_adjacency_matrix(edges: list[list[str]]) -> list[list[int]]:    
def to_adjacency_matrix(edges: list) -> list:
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
  node_indices = dict()
  for index, node in enumerate(nodes):
    node_indices[node] = index

  # 2D matrix of list of integers in a list defaulting to 0 (no directed edge)
  matrix = []
  for _ in nodes:
    row = []
    for _ in nodes:
      row.append(0)
    matrix.append(row)

  # We iterate over the edges, and for each edge, we set the corresponding cell in the matrix to 1.
  # This indicates that there is a connection from the first node in the edge to the second.
  for k,j in edges:
    row = node_indices[k]
    col = node_indices[j]
    matrix[row][col] = 1

  return[nodes,node_indices,matrix]
  return matrix

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

print('-list-')
print(to_adjacency_list(edges))
print('--')
print(to_adjacency_list(edges) == adj_list)
print('--')
print(to_adjacency_matrix(edges)[2] == adj_matrix)
