


class AdjMatrixGraph:
    # Initializes an empty graph with V vertices and 0 edges.
    # Here V is an integer.
    def __init__(self, V):
        self._V = V
        self._E = 0
        # initalizes an adjacency list for each vertex
        self._adj = []
        for i in range(0,V):
            self._adj.append([False] * V)

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
        if not self._adj[u][v]:
            self._E += 1

        # Since this graph is undirected, we add both directions 
        # of the relation in our adjacency matrix.
        self._adj[u][v] = True
        self._adj[v][u] = True

    # returns all the neighbors of vertex v
    def adj(self, v):
        self._validate_vertex(v)
        neighbors = []
        for u in range(0, self._V):
            if self._adj[v][u]:
                neighbors.append(u)
        return neighbors

    def __str__(self):
        s = ""
        for row in self._adj:
            s += str(row) + "\n"
        return s

    # helper function to validate vertices
    def _validate_vertex(self, v):
        if v < 0 or v >= self._V:
            raise Exception("vertex " + str(v) + " is not between 0 and " + str((self._V-1)))

if __name__ == "__main__":
    # We can use this array to convert intgers stored in the graph back to 
    # the real-world names.
    vertices = ["Albert", "Bob", "Christa", "Danielle"]
    V = len(vertices)
    G = AdjMatrixGraph(V)

    # Add the relationships 
    G.add_edge(0,1)
    G.add_edge(0,2)
    G.add_edge(0,3)
    G.add_edge(2,3)
    

    print(G.adj(0)) # 1,2,3 
    print(str(G))
    """
    [False, True, True, True]
    [True, False, False, False]
    [True, False, False, True]
    [True, False, True, False]
    """


