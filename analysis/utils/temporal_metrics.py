from __future__ import division
import snap


def temporal_neighbors(graphs, nodeID, directed=True):
    """Return a snap.TIntV() set of nodes that have been at least once a neighbor of node nodeID in graphs"""
    t_neighbors = snap.TIntV()
    for g in graphs:
        if g.IsNode(nodeID):
            neighbors = snap.TIntV()
            snap.GetNodesAtHop(g, nodeID, 1, neighbors, directed)
            t_neighbors.Union(neighbors)
    return t_neighbors


def temporal_degree(graphs, nodeID, directed=True):
    """Return the temporal degree of node nodeID, which is the size of temporal_neighbors"""
    t_neighbors = temporal_neighbors(graphs, nodeID, directed)
    return t_neighbors.Len()


def temporal_subgraphs(graphs, nodeV):
    """Return the set of induced subgraphs by nodeV from graphs"""
    subgraphs = []
    for g in graphs:
        subgraphs.append(snap.GetSubGraph(g, nodeV))
    return subgraphs


def temporal_clust_coef(graphs, nodeID, directed=True):
    """Return the temporal clustering coefficient of node nodeID during graphs"""
    t_neighbors = temporal_neighbors(graphs, nodeID, directed)
    subgraphs = temporal_subgraphs(graphs, t_neighbors)
    d = len(subgraphs)
    t_degree = t_neighbors.Len()
    c = 0
    for s in subgraphs:
        c += s.GetEdges()
    if directed:
        return c/(d*t_degree*(t_degree-1))
    else:
        return 2*c/(d*t_degree*(t_degree-1))


def charac_temporal_clust_coef(graphs, directed=True):
    """Return the average temporal clustering coefficient of graphs"""
    c = 0
    for node in graphs[0].Nodes():
        nodeID = node.GetId()
        c += temporal_clust_coef(graphs, nodeID, directed)
    return c/graphs[0].GetNodes()

