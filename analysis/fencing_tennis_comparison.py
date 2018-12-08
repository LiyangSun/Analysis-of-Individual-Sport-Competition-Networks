import imp
import collections
import snap
import pickle
import utils.load as load
import matplotlib.pyplot as plt

if __name__ == '__main__':

    dic_path = "../datasets/fencing/fencing_ids.pkl"
    with open(dic_path, 'rb') as dic_id:
        mydict = pickle.load(dic_id)
        fencing_graph = load.load_global("fencing")

    dic_path = "../datasets/tennis/men_ids.pkl"
    with open(dic_path, 'rb') as dic_id:
        mydict = pickle.load(dic_id)
        tm_graph = load.load_global("tennis_men")

    dic_path = "../datasets/tennis/women_ids.pkl"
    with open(dic_path, 'rb') as dic_id:
        mydict = pickle.load(dic_id)
        tf_graph = load.load_global("tennis_women")

    dic_path = "../datasets/chess/chess_ids.pkl"
    with open(dic_path, 'rb') as dic_id:
        mydict = pickle.load(dic_id)
        chess_graph = load.load_global("chess")

    graphs = [fencing_graph, tm_graph, tf_graph, chess_graph]
    names = ["Fencing Network", "Men's Tennis Network", "Women's Tennis Network", "Chess Network"]

    print 'names:', names
    print 'nodes:', [graph.GetNodes() for graph in graphs]
    print 'edges:', [graph.GetEdges() for graph in graphs]
    print 'mxscc:', [snap.GetMxScc(graph).GetNodes() for graph in graphs]
    print 'max degree:', [graph.GetNI(snap.GetMxDegNId(graph)).GetDeg() for graph in graphs]

    comp_dists = [snap.TIntPrV() for graph in graphs]
    scc_counts = [snap.GetSccSzCnt(graph, comp_dists[i]) for i, graph in enumerate(graphs)]
    print 'Strongly Connected Components'
    for i, comp_dist in enumerate(comp_dists):
        print names[i]
        for comp in comp_dist:
            print 'size:', comp.GetVal1(), 'count:', comp.GetVal2()

    p_ranks = [snap.TIntFltH() for graph in graphs]
    [snap.GetPageRank(graph, p_ranks[i]) for i, graph in enumerate(graphs)]
    pr_ys = [sorted([p_rank[x] for x in p_rank]) for p_rank in p_ranks]
    i_pr_ys = [[sum(pr_y[:i+1]) for i in range(len(pr_y))] for pr_y in pr_ys]
    pr_xs = [[float(i+1)/len(pr_y) for i in range(len(pr_y))] for pr_y in pr_ys]

    plt.figure()
    [plt.plot(pr_xs[i], i_pr_ys[i], '.', markersize=4) for i in range(len(graphs))]
    plt.title("Cumulative PageRank vs. Node Fraction")
    plt.legend(names)
    plt.xlabel("Node Fraction")
    plt.ylabel("Cumulative PageRank")

    #get node in-degree distribution
    plt.figure()
    for graph in graphs:
        y = sorted([float(node.GetInDeg())/node.GetDeg() for node in graph.Nodes()])
        #y = [float(val-min(y))/(max(y)-min(y)) for val in y]
        x = [float(i+1)/graph.GetNodes() for i in range(len(y))]
        plt.plot(x,y, '.', markersize=4)
        plt.title("Node Distribution by Win Percentage")
        plt.legend(names)
        plt.xlabel("Node Fraction")
        plt.ylabel("Win Percentage")

    Rnd = snap.TRnd(42)
    Rnd.Randomize()

    min_edges_per_node = min([float(graph.GetEdges())/graph.GetNodes() for graph in graphs])

    for graph in graphs:
        while float(graph.GetEdges())/graph.GetNodes() > min_edges_per_node:
            graph.DelEdge(graph.GetRndEId(Rnd))

    print 'names:', names
    print 'nodes:', [graph.GetNodes() for graph in graphs]
    print 'edges:', [graph.GetEdges() for graph in graphs]
    print 'mxscc:', [snap.GetMxSccSz(graph) for graph in graphs]
    print 'max degree:', [graph.GetNI(snap.GetMxDegNId(graph)).GetDeg() for graph in graphs]

    plt.show()
