import pandas as pd
from os import listdir
import pickle
from pathlib import Path
import snap
from os.path import isfile
import utils


def excel_to_csv(data_dir, year_begin, year_end):
    """Convert Excel sheets from dir 'data_dir/excel/' into csv files in dir 'data_dir/csv/' """

    for i in range(year_begin, year_end):
        if i <= 2012:
            data_xls = pd.read_excel(data_dir + "excel/" + str(i) + '.xls', 0, index_col=None)
            data_xls.to_csv(data_dir + "csv/" + str(i) + '.csv', encoding='utf-8')
        else:
            data_xls = pd.read_excel(data_dir + "excel/" + str(i) + '.xlsx', 0, index_col=None)
            data_xls.to_csv(data_dir + "csv/" + str(i) + '.csv', encoding='utf-8')


def get_edges_txt(csv_dir, dic_path, edges_path):
    """Get a txt file with all match results from csv_dir, first column is loser id, second is winner id
    This is so that when creating the directed graph, the loser references the winner"""

    with open(dic_path, 'rb') as dic_id:
        dic = pickle.load(dic_id)
        with open(edges_path, 'w') as edges:
            for f in listdir(csv_dir):
                df = pd.read_csv(csv_dir + f, header=0)
                for w, l in zip(list(df.loc[:, 'Winner'].values), list(df.loc[:, 'Loser'].values)):
                    w_id = dic[w]
                    l_id = dic[l]
                    edges.write(str(l_id) + ";" + str(w_id) + "\n")


def get_single_edges_txt(csv_dir, csv_file, dic_path, edges_path):
    """Get a single txt file with all match results in csv_file, which is in directory csv_dir.
    First column is loser id, second is winner id"""
    with open(dic_path, 'rb') as dic_id:
        dic = pickle.load(dic_id)
        with open(edges_path, 'w') as edges:
            df = pd.read_csv(csv_dir + csv_file, header=0)
            for w, l in zip(list(df.loc[:, 'Winner'].values), list(df.loc[:, 'Loser'].values)):
                w_id = dic[w]
                l_id = dic[l]
                edges.write(str(l_id) + ";" + str(w_id) + "\n")


def get_weights(csv_dir, dic_path, weights_path):
    """Save a dictionary {edges: weights} from csv_dir and dic_path into weights_path"""
    weights_dic = {}
    try:
        my_abs_path = Path(weights_path).resolve()
    except OSError as e:
        pass
    else:
        with open(weights_path, 'rb') as f:
            weights_dic = pickle.load(f)

    with open(dic_path, 'rb') as dic_id:
        name_dic = pickle.load(dic_id)
        for f in listdir(csv_dir):
            df = pd.read_csv(csv_dir + f, header=0)
            for w, l in zip(list(df.loc[:, 'Winner'].values), list(df.loc[:, 'Loser'].values)):
                w_id = name_dic[w]
                l_id = name_dic[l]
                if (l_id, w_id) not in weights_dic.keys():
                    weights_dic[(l_id, w_id)] = 1
                else:
                    weights_dic[(l_id, w_id)] += 1

    with open(weights_path, 'wb') as f:
        pickle.dump(weights_dic, f, pickle.HIGHEST_PROTOCOL)


def get_single_weights(csv_dir, csv_file, dic_path, weights_path):
    """Save a dictionary {edges: weights} from csv_dir and dic_path into weights_path for file csv_file"""
    weights_dic = {}
    try:
        my_abs_path = Path(weights_path).resolve()
    except OSError as e:
        pass
    else:
        with open(weights_path, 'rb') as f:
            weights_dic = pickle.load(f)

    with open(dic_path, 'rb') as dic_id:
        name_dic = pickle.load(dic_id)
        df = pd.read_csv(csv_dir + csv_file, header=0)
        for w, l in zip(list(df.loc[:, 'Winner'].values), list(df.loc[:, 'Loser'].values)):
            w_id = name_dic[w]
            l_id = name_dic[l]
            if (l_id, w_id) not in weights_dic.keys():
                weights_dic[(l_id, w_id)] = 1
            else:
                weights_dic[(l_id, w_id)] += 1

    with open(weights_path, 'wb') as f:
        pickle.dump(weights_dic, f, pickle.HIGHEST_PROTOCOL)


if __name__ == '__main__':
    # dic_men_path = "../datasets/tennis/men_ids.pkl"
    # dic_women_path = "../datasets/tennis/women_ids.pkl"
    # men_csv_path = "../datasets/tennis/ATP/men/csv/"
    # women_csv_path = "../datasets/tennis/ATP/women/csv/"

    # Men players edges/weights preprocessing
    #
    # excel_to_csv("../datasets/tennis/ATP/men/", 2000, 2019)
    # utils.player_dictionary(men_csv_path, dic_men_path, 'Winner', 'Loser', True)
    # get_edges_txt(men_csv_path, dic_men_path, "../datasets/tennis/ATP/men/edges.txt")
    # get_weights(men_csv_path, dic_men_path, "../datasets/tennis/ATP/men/weights.pkl")
    # utils.get_uniq_edges_txt("../datasets/tennis/ATP/men/weights.pkl", "../datasets/tennis/ATP/men/uniq_edges.txt")

    # Women players edges/weights preprocessing
    #
    # excel_to_csv("../datasets/tennis/ATP/women/", 2007, 2019)
    # utils.player_dictionary(women_csv_path, dic_women_path, 'Winner', 'Loser', True)
    # get_edges_txt(women_csv_path, dic_women_path, "../datasets/tennis/ATP/women/edges.txt")
    # get_weights(women_csv_path, dic_women_path, "../datasets/tennis/ATP/women/weights.pkl")
    # utils.get_uniq_edges_txt("../datasets/tennis/ATP/women/weights.pkl",
    #                          "../datasets/tennis/ATP/women/uniq_edges.txt")

    # Creating edges/weights for time evolution analysis
    #
    # for f in listdir(men_csv_path):
    #     get_single_edges_txt(men_csv_path, f, dic_men_path, men_csv_path[:-4] + "evolution/" + f[:-3] + "txt")
    #     get_single_weights(men_csv_path, f, dic_men_path, men_csv_path[:-4] + "evolution/weights/" + f[:-3] + "pkl")
    # for f in listdir(women_csv_path):
    #     get_single_edges_txt(women_csv_path, f, dic_women_path, women_csv_path[:-4] + "evolution/" + f[:-3] + "txt")
    #     get_single_weights(women_csv_path, f, dic_women_path,
    #                        women_csv_path[:-4] + "evolution/weights/" + f[:-3] + "pkl")

    # Save as binary graphs
    #
    # edges_men_path = "../datasets/tennis/ATP/men/edges.txt"
    # uedges_men_path = "../datasets/tennis/ATP/men/uniq_edges.txt"
    # multi_graph = snap.LoadEdgeList(snap.PNEANet, edges_men_path, 0, 1, ';')
    # graph_undirected = snap.LoadEdgeList(snap.PUNGraph, edges_men_path, 0, 1, ';')
    # graph_directed = snap.LoadEdgeList(snap.PNGraph, uedges_men_path, 0, 1, ';')
    #
    # multi_FOut = snap.TFOut("../graphs/tennis/men_2000_2018_multi_directed_unweighted.graph")
    # multi_graph.Save(multi_FOut)
    # multi_FOut.Flush()
    # undirected_FOut= snap.TFOut("../graphs/tennis/men_2000_2018_simple_undirected_unweighted.graph")
    # graph_undirected.Save(undirected_FOut)
    # undirected_FOut.Flush()
    # directed_FOut = snap.TFOut("../graphs/tennis/men_2000_2018_simple_directed_unweighted.graph")
    # graph_directed.Save(directed_FOut)
    # directed_FOut.Flush()
    #
    # temp_edges_path = "../datasets/tennis/ATP/men/evolution/"
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
    #         multi_FOut = snap.TFOut("../graphs/tennis/men/temporal/multi_directed_unweighted/{}.graph".format(f[:-4]))
    #         multi.Save(multi_FOut)
    #         multi_FOut.Flush()
    #         undirected_FOut = snap.TFOut(
    #             "../graphs/tennis/men/temporal/simple_undirected_unweighted/{}.graph".format(f[:-4]))
    #         undirected.Save(undirected_FOut)
    #         undirected_FOut.Flush()
    #         directed_FOut = snap.TFOut(
    #             "../graphs/tennis/men/temporal/simple_directed_unweighted/{}.graph".format(f[:-4]))
    #         directed.Save(directed_FOut)
    #         directed_FOut.Flush()
    #
    # edges_women_path = "../datasets/tennis/ATP/women/edges.txt"
    # uedges_women_path = "../datasets/tennis/ATP/women/uniq_edges.txt"
    # multi_graph = snap.LoadEdgeList(snap.PNEANet, edges_women_path, 0, 1, ';')
    # graph_undirected = snap.LoadEdgeList(snap.PUNGraph, edges_women_path, 0, 1, ';')
    # graph_directed = snap.LoadEdgeList(snap.PNGraph, uedges_women_path, 0, 1, ';')
    #
    # multi_FOut = snap.TFOut("../graphs/tennis/women_2007_2018_multi_directed_unweighted.graph")
    # multi_graph.Save(multi_FOut)
    # multi_FOut.Flush()
    # undirected_FOut = snap.TFOut("../graphs/tennis/women_2007_2018_simple_undirected_unweighted.graph")
    # graph_undirected.Save(undirected_FOut)
    # undirected_FOut.Flush()
    # directed_FOut = snap.TFOut("../graphs/tennis/women_2007_2018_simple_directed_unweighted.graph")
    # graph_directed.Save(directed_FOut)
    # directed_FOut.Flush()
    #
    # temp_edges_path = "../datasets/tennis/ATP/women/evolution/"
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
    #         multi_FOut = snap.TFOut("../graphs/tennis/women/temporal/multi_directed_unweighted/{}.graph".format(f[:-4]))
    #         multi.Save(multi_FOut)
    #         multi_FOut.Flush()
    #         undirected_FOut = snap.TFOut(
    #             "../graphs/tennis/women/temporal/simple_undirected_unweighted/{}.graph".format(f[:-4]))
    #         undirected.Save(undirected_FOut)
    #         undirected_FOut.Flush()
    #         directed_FOut = snap.TFOut(
    #             "../graphs/tennis/women/temporal/simple_directed_unweighted/{}.graph".format(f[:-4]))
    #         directed.Save(directed_FOut)
    #         directed_FOut.Flush()
    pass
