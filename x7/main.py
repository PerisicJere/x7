import networkx as nx
import matplotlib.pyplot as plt
import random
import sys

def create_random_graph(n, p):
    random_graph = nx.erdos_renyi_graph(n, p)
    for (u, v) in random_graph.edges():
        random_graph.edges[u, v]['weight'] = round(random.random(), 1) * 10
    return random_graph

def save_graph_with_mst(n, p, filename):
    random_graph = create_random_graph(n, p)
    
    plt.figure(figsize=(8, 6))
    pos = nx.spring_layout(random_graph)
    nx.draw(random_graph, pos, with_labels=True, node_size=500, node_color="lightblue", font_size=10, font_weight="bold")
    edge_labels = nx.get_edge_attributes(random_graph, 'weight')
    nx.draw_networkx_edge_labels(random_graph, pos, edge_labels=edge_labels)

    mst_edges = nx.minimum_spanning_edges(random_graph, algorithm='kruskal', data=False)
    mst = nx.Graph()
    mst.add_edges_from(mst_edges)
    nx.draw_networkx_edges(mst, pos, edge_color='red', width=2)

    plt.savefig(filename)

if __name__ == "__main__":
    if len(sys.argv) != 4:
        sys.exit(1)
    
    n = int(sys.argv[1])
    p = float(sys.argv[2])
    filename = sys.argv[3]
    save_graph_with_mst(n, p, filename)
