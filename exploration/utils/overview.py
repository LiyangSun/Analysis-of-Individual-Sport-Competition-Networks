import snap
import pickle


def quick_properties(graph, name, dic_path):
    """Get quick properties of the graph "name". dic_path is the path of the dict {players: id} """
    n_edges = graph.GetEdges()
    n_nodes = graph.GetNodes()
    print("##########")
    print("Quick overview of {} Network".format(name))
    print("##########")
    print("{} Nodes, {} Edges").format(n_nodes, n_edges)
    print("{} Self-edges ".format(snap.CntSelfEdges(graph)))
    print("{} Directed edges, {} Undirected edges".format(snap.CntUniqDirEdges(graph),
                                                          snap.CntUniqUndirEdges(graph)))
    print("{} Reciprocated edges".format(snap.CntUniqBiDirEdges(graph)))
    print("{} 0-out-degree nodes, {} 0-in-degree nodes".format(snap.CntOutDegNodes(graph, 0),
                                                               snap.CntInDegNodes(graph, 0)))
    node_in = graph.GetNI(snap.GetMxInDegNId(graph))
    node_out = graph.GetNI(snap.GetMxOutDegNId(graph))
    print("Maximum node in-degree: {}, maximum node out-degree: {}".format(node_in.GetDeg(), node_out.GetDeg()))
    print("###")
    components = snap.TCnComV()
    snap.GetWccs(graph, components)
    max_wcc = snap.GetMxWcc(graph)
    print "{} Weakly connected components".format(components.Len())
    print "Largest Wcc: {} Nodes, {} Edges".format(max_wcc.GetNodes(), max_wcc.GetEdges())
    prankH = snap.TIntFltH()
    snap.GetPageRank(graph, prankH)
    sorted_prankH = sorted(prankH, key=lambda key: prankH[key], reverse=True)
    NIdHubH = snap.TIntFltH()
    NIdAuthH = snap.TIntFltH()
    snap.GetHits(graph, NIdHubH, NIdAuthH)
    sorted_NIdHubH = sorted(NIdHubH, key=lambda key: NIdHubH[key], reverse=True)
    sorted_NIdAuthH = sorted(NIdAuthH, key=lambda key: NIdAuthH[key], reverse=True)
    with open(dic_path, 'rb') as dic_id:
        mydict = pickle.load(dic_id)
        print("3 most central players by PageRank scores: {}, {}, {}".format(list(mydict.keys())[list(mydict.values()).index(sorted_prankH[0])],
                                                                             list(mydict.keys())[
                                                                                 list(mydict.values()).index(
                                                                                     sorted_prankH[1])],
                                                                             list(mydict.keys())[
                                                                                 list(mydict.values()).index(
                                                                                     sorted_prankH[2])]))
        print("Top 3 hubs: {}, {}, {}".format(list(mydict.keys())[list(mydict.values()).index(sorted_NIdHubH[0])],
                                                                             list(mydict.keys())[
                                                                                 list(mydict.values()).index(
                                                                                     sorted_NIdHubH[1])],
                                                                             list(mydict.keys())[
                                                                                 list(mydict.values()).index(
                                                                                     sorted_NIdHubH[2])]))
        print("Top 3 authorities: {}, {}, {}".format(list(mydict.keys())[list(mydict.values()).index(sorted_NIdAuthH[0])],
                                                                             list(mydict.keys())[
                                                                                 list(mydict.values()).index(
                                                                                     sorted_NIdAuthH[1])],
                                                                             list(mydict.keys())[
                                                                                 list(mydict.values()).index(
                                                                                     sorted_NIdAuthH[2])]))


def visu(graph, fig_name):
    snap.PlotOutDegDistr(graph, fig_name, "Distribution of out-degrees of nodes")