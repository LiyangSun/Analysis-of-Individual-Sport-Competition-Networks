import utils
import pickle
import pandas as pd
from os import listdir
from pathlib import Path
import snap
from os.path import isfile


def get_edges_txt(csv_dir, edges_path):
    """Get a txt file with all match results from csv_dir, first column is loser id, second is winner id
    This is so that when creating the directed graph, the loser references the winner"""

    with open(edges_path, 'w') as edges:
        for f in listdir(csv_dir):
            df = pd.read_csv(csv_dir + f, header=0)
            for w, b, s in zip(list(df.loc[:, 'White Player #'].values),
                               list(df.loc[:, 'Black Player #'].values),
                               list(df.loc[:, 'Score'].values)):
                if s == 1:
                    edges.write(str(b) + ";" + str(w) + "\n")
                elif s == 0:
                    edges.write(str(w) + ";" + str(b) + "\n")


def get_edges_txt_10months(csv_dir, month_begin, month_end, edges_path):
    """Get a txt file with all match results from csv_dir which happened between month_begin and month_end"""
    with open(edges_path, 'w') as edges:
        for f in listdir(csv_dir):
            df = pd.read_csv(csv_dir + f, header=0)
            for m, w, b, s in zip(list(df.loc[:, 'Month #'].values),
                                  list(df.loc[:, 'White Player #'].values),
                                  list(df.loc[:, 'Black Player #'].values),
                                  list(df.loc[:, 'Score'].values)):
                if month_begin < m <= month_end:
                    if s == 1:
                        edges.write(str(b) + ";" + str(w) + "\n")
                    elif s == 0:
                        edges.write(str(w) + ";" + str(b) + "\n")


def get_weights(csv_dir, weights_path):
    """Save a dictionary {edges: weights} from csv_dir and dic_path into weights_path"""
    weights_dic = {}
    try:
        my_abs_path = Path(weights_path).resolve()
    except OSError as e:
        pass
    else:
        with open(weights_path, 'rb') as f:
            weights_dic = pickle.load(f)

    for f in listdir(csv_dir):
        df = pd.read_csv(csv_dir + f, header=0)
        for w, b, s in zip(list(df.loc[:, 'White Player #'].values),
                           list(df.loc[:, 'Black Player #'].values),
                           list(df.loc[:, 'Score'].values)):
            if s != 0.5:
                x, y = w, b
                if s == 0:
                    x, y = b, w
                if (x, y) not in weights_dic.keys():
                    weights_dic[(x, y)] = 1
                else:
                    weights_dic[(x, y)] += 1

    with open(weights_path, 'wb') as f:
        pickle.dump(weights_dic, f, pickle.HIGHEST_PROTOCOL)


def get_single_weights(csv_dir, month_begin, month_end, weights_path):
    """Save a dictionary {edges: weights} from csv_dir and dic_path into weights_path
    for matches between month_begin and month_end"""
    weights_dic = {}
    try:
        my_abs_path = Path(weights_path).resolve()
    except OSError as e:
        pass
    else:
        with open(weights_path, 'rb') as f:
            weights_dic = pickle.load(f)

    for f in listdir(csv_dir):
        df = pd.read_csv(csv_dir + f, header=0)
        for m, w, b, s in zip(list(df.loc[:, 'Month #'].values),
                              list(df.loc[:, 'White Player #'].values),
                              list(df.loc[:, 'Black Player #'].values),
                              list(df.loc[:, 'Score'].values)):
            if month_begin < m <= month_end:
                if s != 0.5:
                    x, y = w, b
                    if s == 0:
                        x, y = b, w
                    if (x, y) not in weights_dic.keys():
                        weights_dic[(x, y)] = 1
                    else:
                        weights_dic[(x, y)] += 1

    with open(weights_path, 'wb') as f:
        pickle.dump(weights_dic, f, pickle.HIGHEST_PROTOCOL)


if __name__ == '__main__':
    pass
    # dic_path = "../datasets/chess/chess_ids.pkl"
    # csv_path = "../datasets/chess/csv/"
    # utils.player_dictionary(csv_path, dic_path, "White Player #", "Black Player #", False)
    # get_edges_txt(csv_path, "../datasets/chess/edges.txt")
    # get_weights(csv_path, "../datasets/chess/weights.pkl")
    # utils.get_uniq_edges_txt("../datasets/chess/weights.pkl", "../datasets/chess/uniq_edges.txt")

    # Create graphs for time evolution analysis (every 10 months)
    # time = range(0, 101, 10)
    # for i in range(len(time)-1):
    #     month_begin = time[i]
    #     month_end = time[i+1]
    #     get_edges_txt_10months(csv_path, month_begin, month_end,
    #                            csv_path[:-4] + "evolution/{}_{}.txt".format(month_begin+1, month_end))
    #     get_single_weights(csv_path, month_begin, month_end,
    #                        csv_path[:-4] + "evolution/weights/{}_{}.pkl".format(month_begin+1, month_end))

    # txt_path = "../datasets/chess/edges.txt"
    # multi_graph = snap.LoadEdgeList(snap.PNEANet, txt_path, 0, 1, ';')
    # graph_undirected = snap.LoadEdgeList(snap.PUNGraph, txt_path, 0, 1, ';')
    # graph_directed = snap.LoadEdgeList(snap.PNGraph, txt_path, 0, 1, ';')
    #
    # multi_FOut = snap.TFOut("../graphs/chess/100months_multi_directed_unweighted.graph")
    # multi_graph.Save(multi_FOut)
    # multi_FOut.Flush()
    # undirected_FOut= snap.TFOut("../graphs/chess/100months_simple_undirected_unweighted.graph")
    # graph_undirected.Save(undirected_FOut)
    # undirected_FOut.Flush()
    # directed_FOut = snap.TFOut("../graphs/chess/100months_simple_directed_unweighted.graph")
    # graph_directed.Save(directed_FOut)
    # directed_FOut.Flush()
    #
    # temp_edges_path = "../datasets/chess/evolution/"
    # for f in sorted(listdir(temp_edges_path)):
    #     if isfile(temp_edges_path + f):
    #         multi = snap.LoadEdgeList(snap.PNEANet, temp_edges_path + f, 0, 1, ';')
    #         undirected = snap.LoadEdgeList(snap.PUNGraph, temp_edges_path + f, 0, 1, ';')
    #         directed = snap.LoadEdgeList(snap.PNGraph, temp_edges_path + f, 0, 1, ';')
    #
    #         for node in multi_graph.Nodes():
    #             nId = node.GetId()
    #             if not multi.IsNode(nId):
    #                 multi.AddNode(nId)
    #             if not undirected.IsNode(nId):
    #                 undirected.AddNode(nId)
    #             if not directed.IsNode(nId):
    #                 directed.AddNode(nId)
    #
    #         multi_FOut = snap.TFOut("../graphs/chess/temporal/multi_directed_unweighted/{}.graph".format(f[:-4]))
    #         multi.Save(multi_FOut)
    #         multi_FOut.Flush()
    #         undirected_FOut = snap.TFOut(
    #             "../graphs/chess/temporal/simple_undirected_unweighted/{}.graph".format(f[:-4]))
    #         undirected.Save(undirected_FOut)
    #         undirected_FOut.Flush()
    #         directed_FOut = snap.TFOut(
    #             "../graphs/chess/temporal/simple_directed_unweighted/{}.graph".format(f[:-4]))
    #         directed.Save(directed_FOut)
    #         directed_FOut.Flush()

