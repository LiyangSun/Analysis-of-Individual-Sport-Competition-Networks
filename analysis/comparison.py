import snap
import utils.network_distance as dst
import utils.load as load


if __name__ == '__main__':
    wo1 = "../datasets/tennis/ATP/men/weights.pkl"
    wo2 = "../datasets/tennis/ATP/women/weights.pkl"
    men_path = "../datasets/tennis/ATP/men/edges.txt"
    women_path = "../datasets/tennis/ATP/women/edges.txt"
    graph1 = snap.LoadEdgeList(snap.PNGraph, men_path, 0, 1, ';')
    graph2 = snap.LoadEdgeList(snap.PNGraph, women_path, 0, 1, ';')

    graphs = load.load_temporal("tennis_men", multi=False)
    w1 = "../datasets/tennis/ATP/men/evolution/weights/2000.pkl"
    w2 = "../datasets/tennis/ATP/men/evolution/weights/2001.pkl"

    print(dst.network_distance(graph1, graph2, wo1, wo1))