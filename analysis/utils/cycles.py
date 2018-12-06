# Joe's implementation of cycle counting

import snap


def get_unweighted_graph(Graph):
    UnweightedGraph = snap.TNGraph.New()
    for Node in Graph.Nodes():
        UnweightedGraph.AddNode(Node.GetId())
    for Edge in Graph.Edges():
        UnweightedGraph.AddEdge(Edge.GetSrcNId(), Edge.GetDstNId())
    return UnweightedGraph


def count_graph_cycles(Graph, max_length=10):
    '''
    Args:
        graph: TNEANet representing a competitive network
        max_length: the maximum length cycle that should be found

    Returns a map from cycle length to how many cycles of that length are present
    in the graph, up to the max length.
    '''
    # first, construct a new undirected graph
    UnweightedGraph = get_unweighted_graph(Graph)
    endpoints = []
    for Node in UnweightedGraph.Nodes():
        if Node.GetInDeg() == 0 or Node.GetOutDeg() == 0:
            endpoints.append(Node.GetId())
    for endpoint in endpoints:
        UnweightedGraph.DelNode(endpoint)
    nids = sorted(Node.GetId() for Node in UnweightedGraph.Nodes())
    cycle_dict = {}
    for start_nid in nids:
        curr_length = 1
        paths = [[start_nid]]
        while len(paths) > 0 and curr_length <= max_length:
            new_paths = []
            for path in paths:
                end_nid = path[-1]
                for nbr in UnweightedGraph.GetNI(end_nid).GetOutEdges():
                    if nbr == start_nid:
                        cycle_dict[curr_length] = cycle_dict.get(curr_length, 0) + 1
                    elif nbr not in path:
                        new_paths.append(path + [nbr])
            paths = new_paths
            curr_length += 1
        UnweightedGraph.DelNode(start_nid)
    return cycle_dict


def count_pairwise_cycles(Graph):
    '''
    Args:
        graph: TNEANet representing a competitive network

    Returns a map from the id of a node node_a to the number of nodes node_b for
    which there exists a path from node_a to node_b and from node_b to node_a
    '''
    UG = get_unweighted_graph(Graph)
    reachable_nodes_map = {}
    endpoints = []
    for Node in UG.Nodes():
        if Node.GetInDeg() == 0 or Node.GetOutDeg() == 0:
            endpoints.append(Node.GetId())
    for endpoint in endpoints:
        UG.DelNode(endpoint)
    nids = sorted(Node.GetId() for Node in UG.Nodes())
    for nid in nids:
        reachable_nodes_map[nid] = get_reachable_nodes(UG, nid)
    node_cycle_count = {}
    for i in range(len(nids)):
        for j in range(i + 1, len(nids)):
            node_a = nids[i]
            node_b = nids[j]
            if node_a in reachable_nodes_map[node_b] and node_b in reachable_nodes_map[node_a]:
                node_cycle_count[node_a] = node_cycle_count.get(node_a, 0) + 1
                node_cycle_count[node_b] = node_cycle_count.get(node_b, 0) + 1
    return node_cycle_count


def get_reachable_nodes(UG, nid):
    reachable_nodes = set([nid])
    frontier = set([nid])
    while len(frontier) > 0:
        new_frontier = set([])
        for node in frontier:
            for nbr in UG.GetNI(node).GetOutEdges():
                if nbr not in reachable_nodes:
                    reachable_nodes.add(nbr)
                    new_frontier.add(nbr)
        frontier = new_frontier
    return reachable_nodes
