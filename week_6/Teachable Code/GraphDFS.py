from buildAdjList import buildAdjList, prettyPrint

#is there a path from this node to that node

#return true if the target can be reached from the source
def DFS(adj_list, source, target):
    #O(N^2) runtime
    #O(N)
    visited = set()
    return _DFS(adj_list, source, target, visited)


def _DFS(adj_list, cur_node, target, visited):
    if cur_node == target:
        return True

    if cur_node in visited:
        return False

    visited.add(cur_node)
    #O(N)
    for neighbor in adj_list[cur_node]:

        #O(N)
        if (_DFS(adj_list, neighbor, target, visited)):
            return True
    return False



if __name__ == '__main__':
    #start Hermia
    #end Oberon
    #-> True

    #cur - Lysander
    #start Lysander
    #end Oberomn
    #-> True

    #start Helena
    #end Oberon
    #->True

    #Titania
    #-> True

    #Oberon
    # -> True

    #start Demetrius
    #-> False

    #cur - Puck
    #start Puck
    #end Oberon -> False
    love_connections = [("Lysander", "Helena"), ("Hermia", "Lysander"), ("Demetrius", "Lysander"),
                        ("Helena", "Demetrius"), ("Titania", "Oberon"), ("Oberon", "Titania"),
                        ("Puck", "Puck"), ("Lysander", "Puck"), ("Helena", "Titania")]

    #directed adjacency list
    adj_list = buildAdjList(love_connections)

    #source 0
    #N+1
    edges = []
    N = 5
    for i in range(N):
        for j in range(N):
            edges.append((i,j))
    edges.append((N+1,N+1))
    prettyPrint(edges)

    #Lysander: [Helena, Puck]
    #Hermia: [Lysander]
    #Demetrius: [Lysander]
    #Helena: [Demetrius]
    #Titania: [Oberon]
    #Oberon: [Titania]
    #Puck: [Puck]

    #graph_repr = prettyPrint(love_connections)
    print(DFS(adj_list, "Hermia", "Oberon"))
