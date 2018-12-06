import pickle
import snap
from os import listdir


def load_global(sport, multi=True, directed=True, unweighted=True):
    """Load binary graph from graphs directory"""
    s = ""
    if sport == "chess":
        if multi:
                s = "../graphs/chess/100months_multi_directed_unweighted.graph"
        else:
            if directed:
                s = "../graphs/chess/100months_simple_directed_unweighted.graph"
            else:
                s = "../graphs/chess/100months_simple_undirected_unweighted.graph"

    elif sport == "fencing":
        if multi:
            s = "../graphs/fencing/2017_2018_multi_directed_unweighted.graph"
        else:
            if directed:
                s = "../graphs/fencing/2017_2018_simple_directed_unweighted.graph"
            else:
                s = "../graphs/fencing/2017_2018_simple_undirected_unweighted.graph"
    elif sport == "tennis_men":
        if multi:
            s = "../graphs/tennis/men/men_2000_2018_multi_directed_unweighted.graph"
        else:
            if directed:
                s = "../graphs/tennis/men/men_2000_2018_simple_directed_unweighted.graph"
            else:
                s = "../graphs/tennis/men/men_2000_2018_simple_undirected_unweighted.graph"
    elif sport == "tennis_women":
        if multi:
            s = "../graphs/tennis/women/women_2007_2018_multi_directed_unweighted.graph"
        else:
            if directed:
                s = "../graphs/tennis/women/women_2007_2018_simple_directed_unweighted.graph"
            else:
                s = "../graphs/tennis/women/women_2007_2018_simple_undirected_unweighted.graph"

    FIn = snap.TFIn(s)
    if multi:
        return snap.TNEANet.Load(FIn)
    else:
        if directed:
            return snap.TNGraph.Load(FIn)
        else:
            return snap.TUNGraph.Load(FIn)


def load_temporal(sport, multi=True, directed=True, unweighted=True):
    """Load a set of binary graphs from graphs directory"""
    directory = ""
    graphs = []
    if sport == "chess":
        if multi:
            directory = "../graphs/chess/temporal/multi_directed_unweighted/"
        else:
            if directed:
                directory = "../graphs/chess/temporal/simple_directed_unweighted/"
            else:
                directory = "../graphs/chess/temporal/simple_undirected_unweighted/"
    elif sport == "tennis_men":
        if multi:
            directory = "../graphs/tennis/men/temporal/multi_directed_unweighted/"
        else:
            if directed:
                directory = "../graphs/tennis/men/temporal/simple_directed_unweighted/"
            else:
                directory = "../graphs/tennis/men/temporal/simple_undirected_unweighted/"
    elif sport == "tennis_women":
        if multi:
            directory = "../graphs/tennis/women/temporal/multi_directed_unweighted/"
        else:
            if directed:
                directory = "../graphs/tennis/women/temporal/simple_directed_unweighted/"
            else:
                directory = "../graphs/tennis/women/temporal/simple_undirected_unweighted/"
    for f in sorted(listdir(directory)):
        FIn = snap.TFIn(directory + f)
        if multi:
            graphs.append(snap.TNEANet.Load(FIn))
        else:
            if directed:
                graphs.append(snap.TNGraph.Load(FIn))
            else:
                graphs.append(snap.TUNGraph.Load(FIn))
    return graphs


# def load_weightedgraph(weights_path, uniq_edges_path):
#     """Load competitive dataset as a directed weighted simple graph using weights dict at weights_path"""
#     graph = snap.LoadEdgeList(snap.PNEANet, uniq_edges_path, 0, 1, ';')
#     attr = "number of defeats"
#     graph.AddIntAttrE(attr)
#     with open(weights_path, 'rb') as weights:
#         w_dic = pickle.load(weights)
#         for edge in graph.Edges():
#             x = edge.GetSrcNId()
#             y = edge.GetDstNId()
#             w = w_dic[(x, y)]
#             graph.AddIntAttrDatE(edge, w, attr)
#     return graph
