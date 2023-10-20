


class Graph:
	# Initializes an empty graph with V vertices and 0 edges.
	def __init__(self, V):
		self._V = V
		self._E = 0
		# initalizes an adjacency list for each vertex
		self._adj = [[] for i in range(0, V)]

	# returns the number of vertices in this graph
	def V(self):
		return self._V

	# returns the number of edges in this graph
	def E(self):
		return self._E

	# add edge between u-v in this graph, u,v are vertices
	def add_edge(self, u, v):
		self._validate_vertex(u)
		self._validate_vertex(v)
		self._E += 1
		self._adj[v].append(u)
		self._adj[u].append(v)

	# returns all the neighbors of vertex v
	def adj(self, v):
		self._validate_vertex(v)
		return self._adj[v]

	def __str__(self):
		return str(self._adj)

	# helper function to validate vertices
	def _validate_vertex(self, v):
		if v < 0 or v >= self._V:
			raise Exception("vertex " + str(v) + " is not between 0 and " + str((self._V-1)))


if __name__ == "__main__":
    # We can use this array to convert intgers stored in the graph back to 
    # the real-world names.
    vertices = ["Albert", "Bob", "Christa", "Danielle"]
    V = len(vertices)
    G = Graph(V)

    # Add the relationships 
    G.add_edge(0,1)
    G.add_edge(0,2)
    G.add_edge(0,3)
    G.add_edge(2,3)
    

    print(G.adj(0)) # 1,2,3 
    print(str(G))
    """
    [
		[0,1],
		[0,2]
		[0,3],
		[2,3]
    ]
    """
