import matplotlib.pyplot as plt
import networkx as nx

from app.graph.graph_builder import build_graph

def visualize_graph():

    G = build_graph()

    plt.figure(figsize=(10, 8))

    pos = nx.spring_layout(G)

    nx.draw(
        G,
        pos,
        with_labels=True,
        node_color='lightblue',
        edge_color='gray',
        node_size=3000,
        font_size=10
    )

    plt.title("Phase 2 Hypergraph Visualization")

    plt.savefig("graph_output.png")

    return "graph_output.png"