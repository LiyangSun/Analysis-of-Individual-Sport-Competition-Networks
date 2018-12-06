from __future__ import division
import snap
import pickle
from collections import Counter


def JA_similarity_max(graph, player, dic_path, n=5, directed=False):
    """Find the n most similar players to player by JA metrics"""
    with open(dic_path, 'rb') as dic_id:
        mydict = pickle.load(dic_id)
        player_id = mydict[player]

        player_neighbor = snap.TIntV()
        snap.GetNodesAtHop(graph, player_id, 1, player_neighbor, directed)

        player_ja = {}
        for node in graph.Nodes():
            nodeId = node.GetId()
            node_neighbor = snap.TIntV()
            snap.GetNodesAtHop(graph, nodeId, 1, node_neighbor, directed)
            if nodeId != player_id:
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


def CN_similarity_max(graph, player, dic_path, n=5, directed=False):
    """Find the n most similar players to player by CN metrics"""
    with open(dic_path, 'rb') as dic_id:
        mydict = pickle.load(dic_id)
        player_id = mydict[player]

        player_neighbor = snap.TIntV()
        snap.GetNodesAtHop(graph, player_id, 1, player_neighbor, directed)

        player_cn = {}
        for node in graph.Nodes():
            nodeId = node.GetId()
            node_neighbor = snap.TIntV()
            snap.GetNodesAtHop(graph, nodeId, 1, node_neighbor, directed)
            if nodeId != player_id:
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