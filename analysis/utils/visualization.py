import graphviz
import pickle
import snap
import networkx as nx
import matplotlib.pyplot as plt


def load_graph_networkx(edges_path, create_using=None):
    """Same but with NetworkX"""
    return nx.read_edgelist(edges_path, delimiter=";", create_using=create_using)


def visualize_networkx(graph_networkx, name):
    """Visualize a NetworkX graph and saves a plot under the name name"""
    plt.figure(0)
    nx.draw(graph_networkx, with_labels=True)
    plt.savefig("global_{}".format(name))


def visualize_graphviz(graph, name, dic_path):
    """Visualize the graph using Graphviz"""
    dot = graphviz.Digraph(comment=name)
    with open(dic_path, 'rb') as dic_id:
        mydict = pickle.load(dic_id)
        for node in graph.Nodes():
            node_id = node.GetId()
            player = list(mydict.keys())[list(mydict.values()).index(node_id)]
            dot.node(str(node_id), player)
        for edge in graph.Edges():
            a = str(edge.GetSrcNId())
            b = str(edge.GetDstNId())
            dot.edge(a, b)
    dot.render('test-output/tennis-men.gv', view=True)


def out_deg_distribution(graph, fig_name):
    """Plot the out-degree distribution of nodes in graph"""
    snap.PlotOutDegDistr(graph, fig_name, "Distribution of out-degrees of nodes")


def in_deg_distribution(graph, fig_name):
    """Plot the in-degree distribution of nodes in graph"""
    snap.PlotInDegDistr(graph, fig_name, "Distribution of in-degrees of nodes")


if __name__ == '__main__':
    pass