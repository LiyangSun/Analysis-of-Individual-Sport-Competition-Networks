from __future__ import division
import snap
import pickle
from collections import Counter


def JA_similarity(graph, id1, id2, directed=True):
    """Computes JA similarity between nodes id1 and id2 in graph"""
    if id1 == id2:
        return 1
    else:
        neighbors1 = snap.TIntV()
        snap.GetNodesAtHop(graph, id1, 1, neighbors1, directed)
        neighbors2 = snap.TIntV()
        snap.GetNodesAtHop(graph, id2, 1, neighbors2, directed)

        Inter = snap.TIntV()
        Union = snap.TIntV()
        neighbors1.Intrs(neighbors2, Inter)
        neighbors1.Union(neighbors2, Union)
        x = Inter.Len()
        y = Union.Len()
        return x / y


def CN_similarity(graph, id1, id2, directed=True):
    """Computes CN similarity between nodes id1 and id2 in graph"""
    neighbors1 = snap.TIntV()
    snap.GetNodesAtHop(graph, id1, 1, neighbors1, directed)
    neighbors2 = snap.TIntV()
    snap.GetNodesAtHop(graph, id2, 1, neighbors2, directed)

    Inter = snap.TIntV()
    neighbors1.Intrs(neighbors2, Inter)
    x = Inter.Len()
    return x


def JA_similarity_max(graph, player, dic_path, n=5, directed=True):
    """Find the n most similar players to player by JA metrics"""
    with open(dic_path, 'rb') as dic_id:
        mydict = pickle.load(dic_id)
        player_id = mydict[player]

        player_neighbor = snap.TIntV()
        snap.GetNodesAtHop(graph, player_id, 1, player_neighbor, directed)

        player_ja = {}
        for node in graph.Nodes():
            nodeId = node.GetId()
            if nodeId != player_id:
                node_neighbor = snap.TIntV()
                snap.GetNodesAtHop(graph, nodeId, 1, node_neighbor, directed)
                Inter = snap.TIntV()
                Union = snap.TIntV()
                player_neighbor.Intrs(node_neighbor, Inter)
                player_neighbor.Union(node_neighbor, Union)
                x = Inter.Len()
                y = Union.Len()
                player_ja[nodeId] = x / y

        player_ja = Counter(player_ja)

        print("5 most similar players to {} by JA metrics:".format(player))
        for k, v in player_ja.most_common(n):
            print('{}: {}'.format(list(mydict.keys())[list(mydict.values()).index(k)], v))


def CN_similarity_max(graph, player, dic_path, n=5, directed=True):
    """Find the n most similar players to player by CN metrics"""
    with open(dic_path, 'rb') as dic_id:
        mydict = pickle.load(dic_id)
        player_id = mydict[player]

        player_neighbor = snap.TIntV()
        snap.GetNodesAtHop(graph, player_id, 1, player_neighbor, directed)

        player_cn = {}
        for node in graph.Nodes():
            nodeId = node.GetId()
            if nodeId != player_id:
                node_neighbor = snap.TIntV()
                snap.GetNodesAtHop(graph, nodeId, 1, node_neighbor, directed)
                Inter = snap.TIntV()
                player_neighbor.Intrs(node_neighbor, Inter)
                x = Inter.Len()
                player_cn[nodeId] = x

        player_cn = Counter(player_cn)

        print("5 most similar players to {} by CN metrics:".format(player))
        for k, v in player_cn.most_common(n):
            print('{}: {}'.format(list(mydict.keys())[list(mydict.values()).index(k)], v))


if __name__ == '__main__':
    pass