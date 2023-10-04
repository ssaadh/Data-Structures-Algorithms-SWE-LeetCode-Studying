from __future__ import annotations

'''
Given a DAG that is represented as a collection of edges, i.e. ["n1", "n2"] means that n1 precedes n2 (visually, n1 -> n2),
'''

'''
Create an adjacency list for it.
'''
# input: [["v1", "v2"], ["v1", "v3"], ["v2", "v4"], ["v2", "v5"], ["v4", "v3"], ["v5", "v6"], ["v6", "v4"]]
# output: {'v1': ['v2', 'v3'], 'v2': ['v4', 'v5'], 'v3': [], 'v4': ['v3'], 'v5': ['v6'], 'v6': ['v4']}
def to_adjacency_list(edges: list[list[str]]) -> dict[str, list[str]]:
  data = dict()
  for first,second in edges:
    if first in data:
      data[first].append(second)
    elif first not in data:
      data[first] = [second]
    if second not in data:
      data[second] = []
  return data

'''
Create an adjacency matrix for it where each 
respective cell contains 0 for unconnected and 1 for connected.
Index 0 represents "v1" and so on. 
'''

# input: [["v1", "v2"], ["v1", "v3"], ["v2", "v4"], ["v2", "v5"], ["v4", "v3"], ["v5", "v6"], ["v6", "v4"]]
# output = [
#   [0, 1, 1, 0, 0, 0],
#   [0, 0, 0, 1, 1, 0],
#   [0, 0, 0, 0, 0, 0],
#   [0, 0, 1, 0, 0, 0],
#   [0, 0, 0, 0, 0, 1],
#   [0, 0, 0, 1, 0, 0]
# ]
def to_adjacency_matrix(edges: list[list[str]]) -> list[list[int]]:
  result = []
  largestVertex = 0
  for first,second in edges:
    first = int(first[1:]) - 1
    second = int(second[1:]) - 1
    largestVertex = max(largestVertex, first, second)

    plusOne = largestVertex + 1
    # make the height of the 2D array as long as the biggest vertex and each newer row as long as the longest
    # i didnt look into the extend enough or check loop by loop why this first while append cant be an if and extend too
    while len(result) < plusOne:
      result.append([0] * plusOne)

    # if the length of the 2D array row that is getting a 1 for the edge connection is not long enough, add enough 0s.
    if len(result[first]) < plusOne:
      result[first].extend([0] * (plusOne - len(result[first])))
      
    # assign the 1 for connected
    result[first][second] = 1
    
  for k in result:
    if len(k) < plusOne:
      k.extend([0] * (plusOne - len(k)))

  return result
