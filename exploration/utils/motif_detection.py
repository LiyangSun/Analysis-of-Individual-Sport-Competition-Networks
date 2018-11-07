import snap
import numpy as np
from itertools import permutations
from matplotlib import pyplot as plt
from random import randint
import copy


def load_3_subgraphs():
    """Loads a list of all 13 directed 3-subgraphs."""
    return [snap.LoadEdgeList(snap.PNGraph, "../datasets/subgraphs/{}.txt".format(i), 0, 1) for i in range(13)]


def match_3(G1, G2):
    """This function compares two graphs of size 3 (number of nodes) and checks if they are isomorphic."""
    if G1.GetEdges() > G2.GetEdges():
        G = G1
        H = G2
    else:
        G = G2
        H = G1
    for p in permutations(range(3)):
        edge = G.BegEI()
        matches = True
        while edge < G.EndEI():
            if not H.IsEdge(p[edge.GetSrcNId()], p[edge.GetDstNId()]):
                matches = False
                break
            edge.Next()
        if matches:
            break
    return matches


def count_iso(G, sg, motifs, verbose=False):
    """Given a set of 3 node id in sg, obtains the subgraph from the original graph.
    It then matches this graph with one of the 13 graphs in directed_3."""
    if verbose:
        print(sg)
    nodes = snap.TIntV()
    for NId in sg:
        nodes.Add(NId)
    # This call requires latest version of snap (4.1.0)
    SG = snap.GetSubGraphRenumber(G, nodes)
    for i in range(len(motifs)):
        if match_3(motifs[i], SG):
            motif_counts[i] += 1


def gen_config_model_rewire(graph, iterations=10000):
    """Generate Configuration model by random rewiring from graph"""
    config_graph = graph
    clustering_coeffs = []
    count = 1
    clustering_coeffs.append(snap.GetClustCf(config_graph))
    while count <= iterations:
        if count % 100 == 0:
            clustering_coeffs.append(snap.GetClustCf(config_graph))
        a = config_graph.GetRndNId()
        b = config_graph.GetRndNId()
        while not config_graph.IsEdge(a, b):
            a = config_graph.GetRndNId()
            b = config_graph.GetRndNId()
        c = config_graph.GetRndNId()
        d = config_graph.GetRndNId()
        while (not config_graph.IsEdge(c, d)) or (a, b) == (c, d):
            c = config_graph.GetRndNId()
            d = config_graph.GetRndNId()
        e1, e2 = (a, b), (c, d)
        i, j = randint(0, 1), randint(0, 1)
        u, v, w, x = e1[i], e1[1-i], e2[j], e2[1-j]
        if not(config_graph.IsEdge(u, w) or config_graph.IsEdge(v, x)):
            if (u != w) and (v != x):
                config_graph.DelEdge(a, b)
                config_graph.DelEdge(c, d)
                config_graph.AddEdge(u, w)
                config_graph.AddEdge(v, x)
                count += 1
    return config_graph, clustering_coeffs


def plot_rewiring_clust(clustering_coeffs):
    """Plot the evolution of clustering coefficient of the graph against the number of iterations of rewiring"""
    plt.plot(np.linspace(0, 10000, len(clustering_coeffs)), clustering_coeffs)
    plt.xlabel('Iteration')
    plt.ylabel('Average Clustering Coefficient')
    plt.title('Random edge rewiring: Clustering Coefficient')
    plt.show()


def enumerate_subgraph(G, motifs, k=3, verbose=False):
    """Main function of ESU algorithm"""
    global motif_counts
    motif_counts = [0] * len(motifs)
    for node in G.Nodes():
        id = node.GetId()
        neighbors = snap.TIntV()
        snap.GetNodesAtHop(G, id, 1, neighbors, False)
        v_ext = [n for n in neighbors if n>id]
        extend_subgraph(G, k, [id], v_ext, id, motifs, verbose)
    return


def extend_subgraph(G, k, sg, v_ext, node_id, motifs, verbose=False):
    """Recursive function in the ESU algorithm"""
    if len(sg) is k:
        count_iso(G, sg, motifs, verbose)
        return
    while len(v_ext) != 0:
        w = v_ext[0]
        del v_ext[0]
        v_ext_bis = copy.deepcopy(v_ext)
        neighbors = snap.TIntV()
        snap.GetNodesAtHop(G, w, 1, neighbors, False)
        for node in neighbors:
            if not (node in sg):
                if node > node_id:
                    bool = False
                    nb = snap.TIntV()
                    snap.GetNodesAtHop(G, node, 1, nb, False)
                    for n in sg:
                        b = (n in nb)
                        bool = bool | b
                    if not bool:
                        v_ext_bis.append(node)
        sg_bis = copy.deepcopy(sg)
        sg_bis.append(w)
        extend_subgraph(G, k, sg_bis, v_ext_bis, node_id, motifs, verbose)
    return


def zscores_3(graph_path, mot):
    """Plot the Z-scores of the 3-directed subgraphs in G"""

    motifs = np.zeros((10, 13))
    for i in range(10):
        G = snap.LoadEdgeList(snap.PNGraph, graph_path, 0, 1, ';')
        instance, _ = gen_config_model_rewire(G, 8000)
        enumerate_subgraph(instance, mot)
        motifs[i, :] = motif_counts

    G = snap.LoadEdgeList(snap.PNGraph, graph_path, 0, 1, ';')
    enumerate_subgraph(G, mot, 3)

    Z = [0] * len(directed_3)

    for i in range(len(directed_3)):
        sampled = motifs[:, i]
        m = np.mean(sampled)
        s = np.std(sampled)
        Z[i] = (motif_counts[i]-m)/s

    x = np.linspace(1, 13, 13)
    plt.plot(x, Z, 'x')
    plt.title("Z scores of the grid network")
    plt.xlabel('Motif ID')
    plt.ylabel('Z-score')
    plt.grid(True)
    plt.show()


if __name__ == "__main__":
    directed_3 = load_3_subgraphs()
    motif_counts = [0] * len(directed_3)
