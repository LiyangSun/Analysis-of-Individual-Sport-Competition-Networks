import pickle
import snap
import util


if __name__ == '__main__':
    dic_path = "../datasets/tennis/women_ids.pkl"
    with open(dic_path, 'rb') as dic_id:
        mydict = pickle.load(dic_id)
        txt_path = "../datasets/tennis/ATP/women/edges.txt"
        graph = snap.LoadEdgeList(snap.PNEANet, txt_path, 0, 1, ';')
        graph_undirected = snap.LoadEdgeList(snap.PUNGraph, txt_path, 0, 1, ';')
        graph_directed = snap.LoadEdgeList(snap.PNGraph, txt_path, 0, 1, ';')

        # util.out_deg_distribution(graph, "tenniswomen")
        # util.in_deg_distribution(graph, "tenniswomen")