import snap
import utils.network_distance as dst

if __name__ == '__main__':
    w1 = "../datasets/tennis/ATP/men/weights.pkl"
    w2 = "../datasets/tennis/ATP/women/weights.pkl"
    men_path = "../datasets/tennis/ATP/men/edges.txt"
    women_path = "../datasets/tennis/ATP/women/edges.txt"
    graph1 = snap.LoadEdgeList(snap.PNGraph, men_path, 0, 1, ';')
    graph2 = snap.LoadEdgeList(snap.PNGraph, women_path, 0, 1, ';')

    print(dst.network_distance(graph1, graph2, w1, w2))