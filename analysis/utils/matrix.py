import pickle
import numpy as np


def adjacency_matrix(graph, weights_path):
    """Returns the adjacency matrix of graph whose nodes need to be enumerated from 0 to n !"""
    n = graph.GetNodes()
    adj = np.zeros((n, n))
    with open(weights_path, 'rb') as w:
        weights = pickle.load(w)
        for i in range(n):
            for j in range(n):
                if (i, j) in weights.keys():
                    adj[i, j] = weights[(i, j)]
    return adj


def in_deg_matrix(graph):
    """Returns the in-degree matrix of graph
    If the graph is undirected, results coincide"""
    n = graph.GetNodes()
    in_deg = np.zeros((n, n))
    for node in graph.Nodes():
        id = node.GetId()
        in_deg[id, id] = node.GetInDeg()
    return in_deg


def out_deg_matrix(graph):
    """Returns the out-degree matrix of graph
    If the graph is undirected, results coincide"""
    n = graph.GetNodes()
    out_deg = np.zeros((n, n))
    for node in graph.Nodes():
        id = node.GetId()
        out_deg[id, id] = node.GetOutDeg()
    return out_deg


def laplacian_matrix(graph, weights_path, in_degree=True):
    """Returns the Laplacian matrix defined by: Adj matrix - in/out degree matrix"""
    adj = adjacency_matrix(graph, weights_path)
    if in_degree:
        return in_deg_matrix(graph) - adj
    else:
        return out_deg_matrix(graph) - adj


def sorted_laplacian_eigen(graph, weights_path, in_degree=True):
    """Returns the eigen-vectors and values (sorted by values) of the Laplacian matrix of graph"""
    laplacian = laplacian_matrix(graph, weights_path, in_degree)
    values, vectors = np.linalg.eig(laplacian)
    idx = values.argsort()[::-1]
    values = values[idx]
    vectors = vectors[:, idx]
    return values, vectors
