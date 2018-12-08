import snap
import pickle


def txt_results(dic, name):
    """Write results for a network in a txt file"""
    with open("summary_{}.txt".format(name), "w+") as txt_file:
        txt_file.write("########## ")
        txt_file.write("Summary of {} network".format(name))
        txt_file.write(" ##########\n\n")
        for key in sorted(dic.keys()):
            txt_file.write("{}: {}\n".format(key, dic[key]))


def add_results(txt_path, dic):
    """Add results for a network in the txt file txt_path"""
    with open(txt_path, "a+") as txt_file:
        for key in dic.keys():
            txt_file.write("{}: {}\n".format(key, dic[key]))


def add_text(txt_path, s):
    """Add text s to txt_path"""
    with open(txt_path, "a+") as txt_file:
        txt_file.write(s)


def name_from_index(indexV, i, dic):
    """Get name of player which ID is given by indexV[i]
    dic is the {player: ID} dictionary"""
    return list(dic.keys())[list(dic.values()).index(indexV[i])]


def quick_properties(graph, name, dic_path):
    """Get quick properties of the graph "name". dic_path is the path of the dict {players: id} """
    results = {}
    n_edges = graph.GetEdges()
    n_nodes = graph.GetNodes()
    n_self_edges = snap.CntSelfEdges(graph)
    n_directed_edges, n_undirected_edges = snap.CntUniqDirEdges(graph), snap.CntUniqUndirEdges(graph)
    n_reciprocated_edges = snap.CntUniqBiDirEdges(graph)
    n_zero_out_nodes, n_zero_in_nodes = snap.CntOutDegNodes(graph, 0), snap.CntInDegNodes(graph, 0)
    max_node_in = graph.GetNI(snap.GetMxInDegNId(graph)).GetDeg()
    max_node_out = graph.GetNI(snap.GetMxOutDegNId(graph)).GetDeg()
    components = snap.TCnComV()
    snap.GetWccs(graph, components)
    max_wcc = snap.GetMxWcc(graph)
    results["a. Nodes"] = n_nodes
    results["b. Edges"] = n_edges
    results["c. Self-edges"] = n_self_edges
    results["d. Directed edges"] = n_directed_edges
    results["e. Undirected edges"] = n_undirected_edges
    results["f. Reciprocated edges"] = n_reciprocated_edges
    results["g. 0 out-degree nodes"] = n_zero_out_nodes
    results["h. 0 in-degree nodes"] = n_zero_in_nodes
    results["i. Maximum node out-degree"] = max_node_out
    results["j. Maximum node in-degree"] = max_node_in
    results["k. Weakly connected components"] = components.Len()
    results["l. Nodes, edges of largest WCC"] = (max_wcc.GetNodes(), max_wcc.GetEdges())
    print("##########")
    print("Quick overview of {} Network".format(name))
    print("##########")
    print("{} Nodes, {} Edges".format(n_nodes, n_edges))
    print("{} Self-edges ".format(n_self_edges))
    print("{} Directed edges, {} Undirected edges".format(n_directed_edges, n_undirected_edges))
    print("{} Reciprocated edges".format(n_reciprocated_edges))
    print("{} 0-out-degree nodes, {} 0-in-degree nodes".format(n_zero_out_nodes, n_zero_in_nodes))
    print("Maximum node in-degree: {}, maximum node out-degree: {}".format(max_node_in, max_node_out))
    print("###")
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
        print("3 most central players by PageRank scores: {}, {}, {}".format(name_from_index(sorted_prankH, 0, mydict),
                                                                             name_from_index(sorted_prankH, 1, mydict),
                                                                             name_from_index(sorted_prankH, 2, mydict)))
        print("Top 3 hubs: {}, {}, {}".format(name_from_index(sorted_NIdHubH, 0, mydict),
                                              name_from_index(sorted_NIdHubH, 1, mydict),
                                              name_from_index(sorted_NIdHubH, 2, mydict)))
        print("Top 3 authorities: {}, {}, {}".format(name_from_index(sorted_NIdAuthH, 0, mydict),
                                                     name_from_index(sorted_NIdAuthH, 1, mydict),
                                                     name_from_index(sorted_NIdAuthH, 2, mydict)))
        results["m. Three top PageRank"] = (name_from_index(sorted_prankH, 0, mydict),
                                            name_from_index(sorted_prankH, 1, mydict),
                                            name_from_index(sorted_prankH, 2, mydict))
        results["n. Three top hubs"] = (name_from_index(sorted_NIdHubH, 0, mydict),
                                        name_from_index(sorted_NIdHubH, 1, mydict),
                                        name_from_index(sorted_NIdHubH, 2, mydict))
        results["o. Three top authorities"] = (name_from_index(sorted_NIdAuthH, 0, mydict),
                                               name_from_index(sorted_NIdAuthH, 1, mydict),
                                               name_from_index(sorted_NIdAuthH, 2, mydict))
    return results


if __name__ == '__main__':
    txt_results({"Bonjour": 474}, "test")
    pass
