# input: list[list[str]] -> [["v1", "v2"], ["v1", "v3"], ["v2", "v4"], ["v2", "v5"], ["v4", "v3"], ["v5", "v6"], ["v6", "v4"]]
# output: dict[str, list[str]] -> {'v1': ['v2', 'v3'], 'v2': ['v4', 'v5'], 'v3': [], 'v4': ['v3'], 'v5': ['v6'], 'v6': ['v4']}

# There's a dictionary
# - Loop through the input list
# - The first/left element of each input inner list becomes a dictionary key
#   - Check if the element is a dictionary key yet. Create it if so and can assign the second element to its value within an array. If there's already the key, append the second value
# The second element of the input inner list is an element of the array of each dictionary value.
# Every element has to be come a key in the dictionary. Not every element is the first element like v3.
#   - Check if the second element is a dictionary key yet as well. if not, make it one with an empty array as the default value.

# iteration 1
# loop: ["v1", "v2"]
# result: {'v1': ['v2']}

# i2
# loop: ['v1', 'v3']
# result: {'v1': ['v2', 'v3']}

# i3
# ['v2', 'v4']
# {'v1': ['v2', 'v3'], 'v2': ['v4']}

# i4
# ['v2', 'v5']
# {'v1': ['v2', 'v3'], 'v2': ['v4', 'v5']}

# i5
# ['v4', 'v3']
# {'v1': ['v2', 'v3'], 'v2': ['v4', 'v5'], 'v4': ['v3']}

# i6
# ['v5', 'v6']
# {'v1': ['v2', 'v3'], 'v2': ['v4', 'v5'], 'v4': ['v3'], 'v5': ['v6']}

# i7
# ['v6', 'v4']
# {'v1': ['v2', 'v3'], 'v2': ['v4', 'v5'], 'v4': ['v3'], 'v5': ['v6'], 'v6': ['v4']}

# During i2 or i5, v3 as second element can be added to the dictionary too with a blank array value

# iteration 1
# loop: ["v1", "v2"]
# result: {'v1': ['v2'], 'v2': []}

# i2
# loop: ['v1', 'v3']
# result: {'v1': ['v2', 'v3'], 'v2': [], 'v3': []}

# i3
# ['v2', 'v4']
# {'v1': ['v2', 'v3'], 'v2': ['v4'], 'v3': [], 'v4': []}

# i4
# ['v2', 'v5']
# {'v1': ['v2', 'v3'], 'v2': ['v4', 'v5'], 'v3': [], 'v4': [], 'v5': []}

# i5
# ['v4', 'v3']
# {'v1': ['v2', 'v3'], 'v2': ['v4', 'v5'], 'v3': [], 'v4': ['v3'], 'v5': []}

# i6
# ['v5', 'v6']
# {'v1': ['v2', 'v3'], 'v2': ['v4', 'v5'], 'v3': [], 'v4': ['v3'], 'v5': ['v6'], 'v6': []}

# i7
# ['v6', 'v4']
# {'v1': ['v2', 'v3'], 'v2': ['v4', 'v5'], 'v3': [], 'v4': ['v3'], 'v5': ['v6'], 'v6': ['v4']}


def adj_list(edges):
  data = dict()
  for first,second in edges:
    if first in data:
      data[first].append(second)
    elif first not in data:
      data[first] = [second]
    if second not in data:
      data[second] = []
  return data

print(adj_list([["v1", "v2"], ["v1", "v3"], ["v2", "v4"], ["v2", "v5"], ["v4", "v3"], ["v5", "v6"], ["v6", "v4"]]))

# input: [["v1", "v2"], ["v1", "v3"], ["v2", "v4"], ["v2", "v5"], ["v4", "v3"], ["v5", "v6"], ["v6", "v4"]]
# output = [
#   [0, 1, 1, 0, 0, 0],
#   [0, 0, 0, 1, 1, 0],
#   [0, 0, 0, 0, 0, 0],
#   [0, 0, 1, 0, 0, 0],
#   [0, 0, 0, 0, 0, 1],
#   [0, 0, 0, 1, 0, 0]
# ]

# 0 is unconnected edges. The 2D array can initially be pre-filled out as all 0s. How is the size of the array known?
# The length of the input is not relevant to the number of vertices.
# The unique number of vertices within the list of lists would signal the height and width of the 2D array.
# Each inner array needs to be initialized. When a vertex comes up, either in the first or second spot, initialize that row of the result array. Won't be able to 0 fill it out tho because the amt of vertices won't be known until the end of the looping.



# result = []
# for input:
#   get the larger/largest vertex into a var:

#   LargestVertexNumber = 0
#   LargestVertexNumber = max(maxV, int(firstV[1:], int(secondV[1:])

# # make the height of the 2D array as long as the biggest vertex and each newer row as long as the longest
#   while len(res) < LargestVertexNumber:
#     res.append([0] * LargestVertexNumber)

#   # if the length of the 2D array row that is getting a 1 for the edge connection is not long enough, add enough 0s.
#   # can prob use extend vs append
#   while len(res[firstV]) < LargestVertexNumber:
#     res[firstVertice].append(0)

#   # assign the 1 for connected
#   res[firstV][secondV] = 1
  

# Would all previous array rows have their lengths be the largerVertice? Is that needed? At the end, could do a check of the length of each row and if it's not the length of the longest Vertice, do a while loop to keep appending 0s.

# At the end:

# for k in res:
#   # can prob use extend
#   while len(k) < LargestVertexNumber:
#     k.append(0)


# i1
# ["v1", "v2"]

# [
#   [0, 0],
#   [0, 0]
# ]

# [
#   [0, 1],
#   [0, 0]
# ]

# i2
# ["v1", "v3"]

# [
#   [0, 1, 0],
#   [0, 0],
#   [0, 0, 0]
# ]

# [
#   [0, 1, 1],
#   [0, 0],
#   [0, 0, 0]
# ]


# i3
# ["v2", "v4"]

# [
#   [0, 1, 1],
#   [0, 0, 0, 0],
#   [0, 0, 0],
#   [0, 0, 0, 0]
# ]

# [
#   [0, 1, 1],
#   [0, 0, 0, 1],
#   [0, 0, 0],
#   [0, 0, 0, 0]
# ]


# i4
# ["v2", "v5"]

# [
#   [0, 1, 1],
#   [0, 0, 0, 1, 0],
#   [0, 0, 0],
#   [0, 0, 0, 0],
#   [0, 0, 0, 0, 0]
# ]

# [
#   [0, 1, 1],
#   [0, 0, 0, 1, 1],
#   [0, 0, 0],
#   [0, 0, 0, 0],
#   [0, 0, 0, 0, 0]
# ]

# i5
# ["v4", "v3"]

# [
#   [0, 1, 1],
#   [0, 0, 0, 1, 1],
#   [0, 0, 0],
#   [0, 0, 1, 0],
#   [0, 0, 0, 0, 0]
# ]

# i6
# ["v5", "v6"]

# [
#   [0, 1, 1],
#   [0, 0, 0, 1, 1],
#   [0, 0, 0],
#   [0, 0, 1, 0],
#   [0, 0, 0, 0, 0, 0]
# ]

# [
#   [0, 1, 1],
#   [0, 0, 0, 1, 1],
#   [0, 0, 0],
#   [0, 0, 1, 0],
#   [0, 0, 0, 0, 0, 1]
# ]


# i7
# ["v6", "v4"]

# [
#   [0, 1, 1],
#   [0, 0, 0, 1, 1],
#   [0, 0, 0],
#   [0, 0, 1, 0],
#   [0, 0, 0, 0, 0, 1],
#   [0, 0, 0, 0, 0, 0]
# ]

# [
#   [0, 1, 1],
#   [0, 0, 0, 1, 1],
#   [0, 0, 0],
#   [0, 0, 1, 0],
#   [0, 0, 0, 0, 0, 1],
#   [0, 0, 0, 1, 0, 0]
# ]

# post main loop:

# each row will add 0s until the length gets to the largest vertex length (under 0 based indexing)

# [
#   [0, 1, 1, 0, 0, 0],
#   [0, 0, 0, 1, 1, 0],
#   [0, 0, 0, 0, 0, 0],
#   [0, 0, 1, 0, 0, 0],
#   [0, 0, 0, 0, 0, 1],
#   [0, 0, 0, 1, 0, 0]
# ]


# How to translate vertex to the output list index? Like v1 being 0, v6 being 5. Obviously the index is 1 less than the vertex value without the v.
# Slice the first character of each vertex string. Convert to an int. Subtract by 1.
# So something like:
# int(vertex[1:])


# --

# Can keep track of the max vertex and at the end, 0 out the remaining left over things to save on runtime.
# _Could also not 0 anything out initially, and do the 0ing out at the end. Check everything, if it's not 1, make it 0._


# Let's say what happens if the zeroing out of the array is only happening when v6 is seen.
# So i6 would go from:
# [
#   [0, 1],
#   [0, 0, 0, 1, 1],
#   [],
#   [0, 0, 1],
#   [0, 0, 0, 0, 0, 1],
#   []
# ]

# to:
# [
#   [0, 1, 0, 0, 0, 0],
#   [0, 0, 0, 1, 1, 0],
#   [0, 0, 0, 0, 0, 0],
#   [0, 0, 1, 0, 0, 0],
#   [0, 0, 0, 0, 0, 1],
#   [0, 0, 0, 0, 0, 0]
# ]

# _I THINK ALL EXPLANATION BELOW CAN ALL BE DELETED:_
# Whatever the current length of each array row, extend it to v6 length. The new ones being 0s.

# the actual looping will be looping the input:

# i6 is ["v5", "v6"]

# outer loop of input:
# first = v5 - 1 = 4
# second = v6 - 1 = 5
#   result[v5 - 1][v6 - 1] = 1

#   if len(result[0]) < second (5):
#     for 


# for k in lst:
#   if len(k) < 


def adj_matrix(edges):
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

adjmatrix = [
  [0, 1, 1, 0, 0, 0],
  [0, 0, 0, 1, 1, 0],
  [0, 0, 0, 0, 0, 0],
  [0, 0, 1, 0, 0, 0],
  [0, 0, 0, 0, 0, 1],
  [0, 0, 0, 1, 0, 0]
]

print(adj_matrix([["v1", "v2"], ["v1", "v3"], ["v2", "v4"], ["v2", "v5"], ["v4", "v3"], ["v5", "v6"], ["v6", "v4"]]))
print(adj_matrix([["v1", "v2"], ["v1", "v3"], ["v2", "v4"], ["v2", "v5"], ["v4", "v3"], ["v5", "v6"], ["v6", "v4"]]) == adjmatrix)
# [[0, 1, 1, 0, 0, 0], [0, 0, 0, 1, 1, 0], [0, 0, 0, 0, 0, 0], [0, 0, 1, 0, 0, 0], [0, 0, 0, 0, 0, 1], [0, 0, 0, 1, 0, 0]]
