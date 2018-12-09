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


def triads(graph):
    """Get number of closed and open triads in graph"""
    closed, _, open = snap.GetTriadsAll(graph)
    return snap.GetTriads(graph), closed, open


def cluster_metrics(graph):
    """Return a dictionary with all results above"""
    results = {}
    results["a. Clustering coefficient"] = clustering_WS(graph)
    results["b. Alternate clustering coefficient"] = alternative_clust(graph)
    triad, closed, open = triads(graph)
    results["c. Number of triads"] = triad
    results["d. Closed triads"] = closed
    results["e. Open triads"] = open
    return results