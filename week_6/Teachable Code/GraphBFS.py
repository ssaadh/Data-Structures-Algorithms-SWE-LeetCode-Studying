from buildAdjList import buildAdjList, prettyPrint
from queue import Queue

#is there a path from this node to that node

#return true if the target can be reached from the source

#start hermia
#end Oberon
def BFS(adj_list, source, target):
    #O(N) space
    #O(N^2) runtime
    Q = Queue()
    Q.put(source)
    seen = set(source)

    #N
    while(not Q.empty()):
        cur = Q.get()
        if cur == target:
            return True
        #N
        for neighbor in adj_list[cur]:
            if neighbor not in seen:
                seen.add(neighbor)
                Q.put(neighbor)

    return False

# BFS for storing the shortest path
# From Coachable-AI
def BFSU(adj_list, source, target):
    Q = Queue()
    Q.put(source)
    seen = set([source])
    predecessor = {source: None}  # Add a dictionary to keep track of predecessors
    # print(predecessor)
    while(not Q.empty()):
        cur = Q.get()
        if cur == target:
            path = []
            while cur is not None:  # Construct the path by backtracking through predecessors
                path.append(cur)
                cur = predecessor[cur]
            return path[::-1]  # Reverse the path to get it from source to target
        for neighbor in adj_list[cur]:
            if neighbor not in seen:
                seen.add(neighbor)
                Q.put(neighbor)
                predecessor[neighbor] = cur  # Update the predecessor of the neighbor
                print(predecessor)

    return None  # Return None if there is no path from source to target


if __name__ == '__main__':
    love_connections = [("Hermia", "Lysander"), ("Demetrius", "Lysander"),
                        ("Helena", "Demetrius"), ("Titania", "Oberon"), ("Oberon", "Titania"),
                        ("Puck", "Puck"), ("Lysander", "Puck"), ("Helena", "Titania"), ("Hermia", "Puck"), ("Puck", "Helena")]

    #directed adjacency list
    adj_list = buildAdjList(love_connections)

    #Lysander: [Helena, Puck]
    #Hermia: [Lysander]
    #Demetrius: [Lysander]
    #Helena: [Demetrius, Titania]
    #Titania: [Oberon]
    #Oberon: [Titania]
    #Puck: [Puck]

    #visited: Hermia, Puck, Lysander, Helena, Titania, Demetrius

    #0 Hermia
    #1 Puck, Lysander
    #2 Helena
    #3 Titania, Demetrius
    #4 Oberon

    print(BFS(adj_list, "Hermia", "Oberon"))
    print(BFSU(adj_list, "Hermia", "Oberon"))

    #prettyPrint(love_connections)
