from __future__ import division
import snap


def clustering_WS(graph):
    """Computes the clustering coefficient by Watts Strogatz definition"""
    return snap.GetClustCf(graph)


def alternative_clust(graph):
    """Computes the clustering coefficient by taking into account the fraction of inactive nodes"""
    N = graph.GetNodes()
    n0 = snap.CntDegNodes(graph, 0)
    n1 = snap.CntDegNodes(graph, 1)
    f = 1 / (1 - (n0 + n1) / N)
    return f*clustering_WS(graph)
