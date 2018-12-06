import snap
from math import sqrt
import matplotlib.pyplot as plt
import numpy as np
import pickle
import operator


def basic_features_node(graph, nodeId, directed=False):
    """Compute basic features of node nodeId in graph for Rolx and ReFex (see HW2)"""
    deg = graph.GetNI(nodeId).GetDeg()
    neighbors = snap.TIntV()
    snap.GetNodesAtHop(graph, nodeId, 1, neighbors, directed)
    neighbors.Add(nodeId)
    egonet = snap.ConvertSubGraph(snap.PUNGraph, graph, neighbors, False)
    in_ego = egonet.GetEdges()
    out_ego = -2*in_ego
    for node in neighbors:
        out_ego += graph.GetNI(node).GetDeg()
    return [deg, in_ego, out_ego]


def basic_features(graph, directed=False):
    """Compute basic features for whole graph with Rolx and ReFex"""
    features = {}
    for node in graph.Nodes():
        nodeId = node.GetId()
        features[nodeId] = basic_features_node(graph, nodeId, directed)
    return features


def sim(x, y):
    """Measures cosine similarity between x and y"""
    x_np, y_np = np.array(x), np.array(y)
    x2 = sqrt(sum(x_np ** 2))
    y2 = sqrt(sum(y_np ** 2))
    if x2 == 0 or y2 == 0:
        return 0
    else:
        return (sum(x_np * y_np))/(x2 * y2)


def sim_node(node_id, features):
    """Get dict of similarity between node_id and other nodes using their features"""
    sim_nodes = {}
    x = features[node_id]
    for node in features.keys():
        if node != node_id:
            sim_nodes[node] = sim(x, features[node])
    return sim_nodes


def sim_node_max(name, features, dic_path, n=5):
    """Return n most similar players with player "name" using features"""
    with open(dic_path, 'rb') as dic_id:
        mydict = pickle.load(dic_id)
        node_id = mydict[name]
        sim_nodes = sim_node(node_id, features)
        max_nodes = sorted(sim_nodes, key=sim_nodes.get, reverse=True)[:n]
        max_sim = sorted({key: sim_nodes[key] for key in max_nodes}.items(), key=operator.itemgetter(1), reverse=True)

        print("{} most similar players with {} (by cosine similarity and Relx and ReFex algorithm):".format(n, name))
        for i in range(n):
            id, _ = max_sim[i]
            print("{}. {}".format(i+1, list(mydict.keys())[list(mydict.values()).index(id)]))
        return max_sim


def recursive_features_node_step(graph, node_id, rec_features, directed=False):
    """Recursive step for computing recursive features of node_id using Relx and ReFex"""
    neighbors = snap.TIntV()
    snap.GetNodesAtHop(graph, node_id, 1, neighbors, directed)
    res = rec_features[node_id]
    length = len(res)
    m, s = np.array([0]*length), np.array([0]*length)
    if neighbors.Len() != 0:
        for node in neighbors:
            if node != node_id:
                m += np.array(rec_features[node])
                s += np.array(rec_features[node])
        m = m/neighbors.Len()
    return res + list(m) + list(s)


def recursive_features_step(graph, rec_features, directed=False):
    """Recursive step for computing recursive features of whole graph using Relx and ReFex"""
    res = {}
    for node in graph.Nodes():
        node_id = node.GetId()
        res[node_id] = recursive_features_node_step(graph, node_id, rec_features, directed)
    return res


def recursive_features(graph, K=2, directed=False):
    """Get recursive features of whole graph after K iterations (Relx and ReFex)"""
    if K == 1:
        return basic_features(graph, directed)
    else:
        return recursive_features_step(graph, recursive_features(graph, K-1), directed)


def plot_sim_hist(name, features, dic_path, bin_width=20):
    """Plot similarity distribution between player and other nodes using features"""
    with open(dic_path, 'rb') as dic_id:
        mydict = pickle.load(dic_id)
        node = mydict[name]
        sim_dict = sim_node(node, features)
        sim_values = np.array(sim_dict.values())
        plt.hist(sim_values, bin_width, facecolor='g', alpha=0.75)
        plt.xlabel('Cosine Similarity')
        plt.ylabel('Count')
        plt.title('Histogram of cosine similarity between player {} and other players'.format(name))
        plt.text(60, .025, r'$\mu=100,\ \sigma=15$')
        plt.grid(True)
        plt.show()