from graphHelpers import buildAdjList, prettyPrint


#is there a cycle in this graph?

#return true if a cycle exists
def detectCycle(adj_list):
    #visited: Helena, Titania, Oberon, Puck, Demetrius, Lysander
    visited = set()
    #O(N^2) runtime or O(E + V)
    #O(N) space

    #N
    for key in adj_list.keys():
        if key not in visited:
            if (DFS(key, set(), visited, adj_list)):
                return True
    return False

def DFS(cur_node, cur_path, visited, adj_list):

    #cur path: Puck, Demetrius, Lysander
    cur_path.add(cur_node)
    visited.add(cur_node)
    #N
    for neighbor in adj_list[cur_node]:
        if cur_node == neighbor:
            continue
        if neighbor in cur_path:
            return True
        #N
        if neighbor not in visited and DFS(neighbor, cur_path, visited, adj_list):
            return True
    cur_path.remove(cur_node)
    return False


if __name__ == '__main__':
    love_connections = [("Hermia", "Lysander"), ("Demetrius", "Lysander"), ("Oberon", "Titania"),
                        ("Puck", "Puck"), ("Lysander", "Puck"), ("Helena", "Titania"), ("Hermia", "Puck"), ("Puck", "Helena"),
                        ("Titania", "Titania"), ("Helena", "Hermia")]

    #start Hermia
    #cur path: Hermia, Lysander, Puck, Demetrius
    #directed adjacency list
    adj_list = buildAdjList(love_connections)

    #prettyPrint(love_connections)
    print(detectCycle(adj_list))
