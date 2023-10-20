import collections

# Gets the neighbors for cell i,j.
# 
def get_neighbors_ocean(matrix, i, j):
    m = len(matrix)
    n = len(matrix[0])
    
    directions = [(0,1), (1,0), (-1,0), (0,-1)]
    neighbors = []
    for x,y in directions:
        # Check if the new cell is in bounds.
        if 0 <= i+x < m and 0 <= j+y < n:
            # Check that water can actually flow downstream.
            if matrix[i][j] <= matrix[i+x][j+y]:
                neighbors.append((i+x, j+y))
    return neighbors


# Find all cells that can make it to a given ocean.
# If is_pacific == True, then we see if we can reach top row or left column.
# If is_pacific == False, then we see if we can reach the bottom row or right column.
def can_reach_ocean(matrix, is_pacific = False):
    cells_that_can_reach_ocean = set()
    queue = collections.deque([])
    
    # Initialize for Pacific.
    if is_pacific:
        # Initialize Queue to have all cells in the top row.
        for j in range(len(matrix[0])):
            queue.append((0,j))
        # Initialize Queue to have all cells in the left column.
        for i in range(len(matrix)):
            queue.append((i,0))

    # Initialize for Atlantic.
    else:
        # Initialize Queue to have all cells in the top row.
        for j in range(len(matrix[0])):
            queue.append((len(matrix)-1,j))
        # Initialize Queue to have all cells in the left column.
        for i in range(len(matrix)):
            queue.append((i,len(matrix)-1)) 

    
    # BFS from all nodes already touching the pacific, then any node reached can also reach the pacific.
    while queue:
        x,y = queue.popleft()
        if (x,y) in cells_that_can_reach_ocean:
            continue
        
        # Add x,y to visited.
        cells_that_can_reach_ocean.add((x,y))
        
        # Gets all adjacent neighbors.
        for neighbor in get_neighbors_ocean(matrix, x,y):
            queue.appendleft(neighbor)
            
    # Return the cells that can make it to pacific.
    return cells_that_can_reach_ocean
        
#   Pacific ~   ~   ~   ~   ~ 
#        ~  1   2   2   3  (5) *
#        ~  3   2   3  (4) (4) *
#        ~  2   4  (5)  3   1  *
#        ~ (6) (7)  1   4   5  *
#        ~ (5)  1   1   2   4  *
#           *   *   *   *   * Atlantic
ocean = [[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]

# Print the ocean and heights.
for row in ocean:
    print(row)
    
# Initialize a matrix of all False.
can_visit_matrix = []
for i in range(0,len(ocean)):
    can_visit_matrix.append([False] * len(ocean[0]))

# Perform BFS on both.
pacific_cells = can_reach_ocean(ocean, is_pacific=True)
atlantic_cells = can_reach_ocean(ocean, is_pacific=False)

# On;y elements in both sets above can reach both oceans.
pacific_atlantic_cells = set()
for cell in pacific_cells:
    if cell in atlantic_cells:
        pacific_atlantic_cells.add(cell)

# For Leetcode you would return pacific_atlantic_cells here.

for x,y in pacific_atlantic_cells:
    can_visit_matrix[x][y] = True

# Print the solution matrix.
print() 
for row in can_visit_matrix:
    print(row)
