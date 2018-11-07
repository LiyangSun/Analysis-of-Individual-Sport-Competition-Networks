import snap


if __name__ == '__main__':
    txt_path = "../datasets/tennis/ATP/men/edges.txt"
    graph = snap.LoadEdgeList(snap.PNEANet, txt_path, 0, 1, ';')

    print "{}: Nodes {}, Edges {}".format("Tennis ATP men", graph.GetNodes(), graph.GetEdges())

    print(snap.GetClustCf(graph))
    pass