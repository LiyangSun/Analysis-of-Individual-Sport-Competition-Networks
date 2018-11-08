import imp
import snap
import pickle

import matplotlib.pyplot as plt
fencing_preprocessing = imp.load_source('preprocessing', '../preprocessing/fencing.py')

if __name__ == '__main__':
    fencing_graph, fencing_name_map = fencing_preprocessing.get_fencing_graph_and_name_map()
    dic_path = "../datasets/tennis/men_ids.pkl"
    with open(dic_path, 'rb') as dic_id:
        mydict = pickle.load(dic_id)
        txt_path = "../datasets/tennis/ATP/men/edges.txt"
        utxt_path = "../datasets/tennis/ATP/men/uniq_edges.txt"
        tennis_graph = snap.LoadEdgeList(snap.PNEANet, txt_path, 0, 1, ';')
    print fencing_graph.GetNodes(), tennis_graph.GetNodes()
    print snap.GetMxSccSz(fencing_graph), snap.GetMxSccSz(tennis_graph)
