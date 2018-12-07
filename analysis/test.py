import snap
import utils.temporal_metrics as tmetrics


if __name__ == '__main__':
    graph = snap.TNGraph.New()
    for i in range(1, 6):
        graph.AddNode(i)
    graph.AddEdge(1, 2)
    graph.AddEdge(2, 1)
    graph.AddEdge(1, 4)
    graph.AddEdge(5, 2)

    graph2 = snap.TNGraph.New()
    for i in range(1, 6):
        graph2.AddNode(i)
    graph2.AddEdge(1, 4)
    graph2.AddEdge(4, 3)
    graph2.AddEdge(3, 5)
    graph2.AddEdge(5, 2)
    graph2.AddEdge(2, 3)

    nodes = snap.TIntV()
    nodes.Add(1)
    nodes.Add(2)
    nodes.Add(4)
    subgraph = snap.GetSubGraph(graph, nodes)

    print(subgraph.GetNodes(), subgraph.GetEdges())

    v1 = snap.TIntV()
    v1.Add(1)
    v1.Add(2)
    v1.Add(3)

    v1.Union(nodes)
    print(v1.Len())

    print(tmetrics.charac_temporal_clust_coef([graph, graph2]))