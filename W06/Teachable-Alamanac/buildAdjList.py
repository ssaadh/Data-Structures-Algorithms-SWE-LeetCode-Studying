#pip install networkx
#or
#pip install networkx --user
import networkx as nx
import matplotlib.pyplot as plt

def buildAdjList(edges):
    adj_list = {}
    for source,target in edges:
        if source in adj_list:
            adj_list[source].append(target)
        else:
            if target:
                adj_list[source] = [target]
            else:
                adj_list[source] = []
    return adj_list


def prettyPrint(edges):
    G = nx.DiGraph(directed=True)
    G.add_edges_from(edges)
    G.selfloop_edges(data=True)
    pos=nx.spring_layout(G,k=1,iterations=20)
    # k controls the distance between the nodes and varies between 0 and 1
    # iterations is the number of times simulated annealing is run
    # default k =0.1 and iterations=50

    node_labels = {node:node for node in G.nodes()}
    nx.draw_networkx_labels(G, pos, labels=node_labels)
    nx.draw(G,pos, node_color = 'red', node_size=2750, node_labels=node_labels, arrowsize=25)
    plt.show()
