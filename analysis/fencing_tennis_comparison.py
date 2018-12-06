import imp
import snap
import pickle

import matplotlib.pyplot as plt
fencing_preprocessing = imp.load_source('preprocessing', '../preprocessing/fencing.py')

if __name__ == '__main__':
    fencing_graph, fencing_name_map = fencing_preprocessing.get_fencing_graph_and_name_map()
    reverse_name_map = {}
    for name in fencing_name_map:
        reverse_name_map[fencing_name_map[name]]=name
    dic_path = "../datasets/tennis/men_ids.pkl"
    with open(dic_path, 'rb') as dic_id:
        mydict = pickle.load(dic_id)
        txt_path = "../datasets/tennis/ATP/men/edges.txt"
        utxt_path = "../datasets/tennis/ATP/men/uniq_edges.txt"
        tennis_graph = snap.LoadEdgeList(snap.PNEANet, txt_path, 0, 1, ';')
    print 'nodes:', fencing_graph.GetNodes(), tennis_graph.GetNodes()
    print 'edges:', fencing_graph.GetEdges(), tennis_graph.GetEdges()
    print 'mxscc:', snap.GetMxScc(fencing_graph).GetNodes(), snap.GetMxScc(tennis_graph).GetNodes()
    print 'max degree:', fencing_graph.GetNI(snap.GetMxDegNId(fencing_graph)).GetDeg(), tennis_graph.GetNI(snap.GetMxDegNId(tennis_graph)).GetDeg()

    f_comp_dist = snap.TIntPrV()
    t_comp_dist = snap.TIntPrV()
    snap.GetSccSzCnt(fencing_graph, f_comp_dist)
    snap.GetSccSzCnt(tennis_graph, t_comp_dist)
    print 'fencing'
    for comp in f_comp_dist:
        print 'size:', comp.GetVal1(), 'count:', comp.GetVal2()
    print 'tennis'
    for comp in t_comp_dist:
        print 'size:', comp.GetVal1(), 'count:', comp.GetVal2()

    prank_f = snap.TIntFltH()
    prank_t = snap.TIntFltH()
    snap.GetPageRank(snap.GetMxScc(fencing_graph), prank_f)
    snap.GetPageRank(snap.GetMxScc(tennis_graph), prank_t)
    pr_y_f = sorted([prank_f[x] for x in prank_f])
    pr_y_t = sorted([prank_t[x] for x in prank_t])

    #get some best player ids
    bf_ids =  [x for x in prank_f if prank_f[x] in pr_y_f[-5:]]
    bt_ids =  [x for x in prank_t if prank_t[x] in pr_y_t[-5:]]

    i_pr_y_f = [sum(pr_y_f[:i+1]) for i in range(len(pr_y_f))]
    i_pr_y_t = [sum(pr_y_t[:i+1]) for i in range(len(pr_y_t))]
    pr_x_f = [float(i+1)/len(pr_y_f) for i in range(len(pr_y_f))]
    pr_x_t = [float(i+1)/len(pr_y_t) for i in range(len(pr_y_t))]

    plt.figure()
    plt.plot(pr_x_f, i_pr_y_f, 'r.')
    plt.plot(pr_x_t, i_pr_y_t, 'b.')
    plt.title("Cumulative PageRank vs. Node Fraction")
    plt.legend(["Fencing Network", "Tennis Network"])
    plt.xlabel("Node Fraction")
    plt.ylabel("Cumulative PageRank")
    plt.show()

    Rnd = snap.TRnd(42)
    Rnd.Randomize()

    while float(fencing_graph.GetEdges())/fencing_graph.GetNodes() < float(tennis_graph.GetEdges())/tennis_graph.GetNodes():
        tennis_graph.DelEdge(tennis_graph.GetRndEId(Rnd))

    print 'nodes:', fencing_graph.GetNodes(), tennis_graph.GetNodes()
    print 'edges:', fencing_graph.GetEdges(), tennis_graph.GetEdges()
    print 'mxscc:', snap.GetMxScc(fencing_graph).GetNodes(), snap.GetMxScc(tennis_graph).GetNodes()
    print 'max degree:', fencing_graph.GetNI(snap.GetMxDegNId(fencing_graph)).GetDeg(), tennis_graph.GetNI(snap.GetMxDegNId(tennis_graph)).GetDeg()
