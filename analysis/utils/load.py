import pickle
import snap


def load_multigraph(edges_path):
    """Load competitive dataset as an unweighted directed multi-graph using edges.txt files"""
    return snap.LoadEdgeList(snap.PNEANet, edges_path, 0, 1, ';')


def load_simplegraph(uniq_edges_path, directed=True):
    """Load competitive dataset as an unweighted simple graph using edges.txt files"""
    if directed:
        return snap.LoadEdgeList(snap.PNGraph, uniq_edges_path, 0, 1, ';')
    else:
        return snap.LoadEdgeList(snap.PUNGraph, uniq_edges_path, 0, 1, ';')


def load_weightedgraph(weights_path, uniq_edges_path):
    """Load competitive dataset as a directed weighted simple graph using weights dict at weights_path"""
    graph = snap.LoadEdgeList(snap.PNEANet, uniq_edges_path, 0, 1, ';')
    attr = "number of defeats"
    graph.AddIntAttrE(attr)
    with open(weights_path, 'rb') as weights:
        w_dic = pickle.load(weights)
        for edge in graph.Edges():
            x = edge.GetSrcNId()
            y = edge.GetDstNId()
            w = w_dic[(x, y)]
            graph.AddIntAttrDatE(edge, w, attr)
    return graph

#FIn = snap.TFIn("test.graph")
#G4 = snap.TNGraph.Load(FIn)