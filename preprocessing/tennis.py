import pandas as pd
from os import listdir
import pickle
from pathlib import Path
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


if __name__ == '__main__':
    dic_men_path = "../datasets/tennis/men_ids.pkl"
    dic_women_path = "../datasets/tennis/women_ids.pkl"
    men_csv_path = "../datasets/tennis/ATP/men/csv/"
    women_csv_path = "../datasets/tennis/ATP/women/csv/"

    # Men players preprocessing
    # excel_to_csv("../datasets/tennis/ATP/men/", 2000, 2019)
    # utils.player_dictionary(men_csv_path, dic_men_path, 'Winner', 'Loser', True)
    # get_edges_txt(men_csv_path, dic_men_path, "../datasets/tennis/ATP/men/edges.txt")
    # get_weights(men_csv_path, dic_men_path, "../datasets/tennis/ATP/men/weights.pkl")
    # utils.get_uniq_edges_txt("../datasets/tennis/ATP/men/weights.pkl", "../datasets/tennis/ATP/men/uniq_edges.txt")

    # Women players preprocessing
    # excel_to_csv("../datasets/tennis/ATP/women/", 2007, 2019)
    # utils.player_dictionary(women_csv_path, dic_women_path, 'Winner', 'Loser', True)
    # get_edges_txt(women_csv_path, dic_women_path, "../datasets/tennis/ATP/women/edges.txt")
    # get_weights(women_csv_path, dic_women_path, "../datasets/tennis/ATP/women/weights.pkl")
    # utils.get_uniq_edges_txt("../datasets/tennis/ATP/women/weights.pkl", "../datasets/tennis/ATP/women/uniq_edges.txt")
