import pandas as pd
from os import listdir
import pickle
from pathlib import Path


def excel_to_csv(data_dir):
    """Convert Excel sheets from dir 'data_dir/excel/' into csv files in dir 'data_dir/csv/' """

    for i in range(2000, 2019):
        if i <= 2012:
            data_xls = pd.read_excel(data_dir + "excel/" + str(i) + '.xls', 0, index_col=None)
            data_xls.to_csv(data_dir + "csv/" + str(i) + '.csv', encoding='utf-8')
        else:
            data_xls = pd.read_excel(data_dir + "excel/" + str(i) + '.xlsx', 0, index_col=None)
            data_xls.to_csv(data_dir + "csv/" + str(i) + '.csv', encoding='utf-8')


def men_dictionary(csv_dir):
    """Updates a dict where {keys = players, values = integer id} for purposes:
    - graph: nodes ID are integers
    - analysis: keep track of tennis players' IDs

    Add players from csv files in 'csv_dir' if they have not been added yet"""
    dic_path = "../datasets/tennis/men_ids.pkl"
    dic = {}
    try:
        my_abs_path = Path(dic_path).resolve()
    except OSError as e:
        pass
    else:
        with open(dic_path, 'rb') as f:
            dic = pickle.load(f)

    for f in listdir(csv_dir):
        df = pd.read_csv(csv_dir + f, header=0)
        for name in list(df.loc[:, 'Winner'].values):
            if name not in dic.keys():
                ids = len(dic)
                dic[name] = ids
        for name in list(df.loc[:, 'Loser'].values):
            if name not in dic.keys():
                ids = len(dic)
                dic[name] = ids

    with open(dic_path, 'wb') as f:
        pickle.dump(dic, f, pickle.HIGHEST_PROTOCOL)


def get_edges_txt(csv_dir):
    """Get a txt file with all match results from csv_dir, first column is loser id, second is winner id
    This is so that when creating the directed graph, the loser references the winner"""

    with open("../datasets/tennis/men_ids.pkl", 'rb') as dic_id:
        dic = pickle.load(dic_id)
        with open("../datasets/tennis/ATP/men/edges.txt", 'w') as edges:
            for f in listdir(csv_dir):
                df = pd.read_csv(csv_dir + f, header=0)
                for w, l in zip(list(df.loc[:, 'Winner'].values), list(df.loc[:, 'Loser'].values)):
                    w_id = dic[w]
                    l_id = dic[l]
                    edges.write(str(l_id) + ";" + str(w_id) + "\n")


if __name__ == '__main__':
    # excel_to_csv("../datasets/tennis/ATP/men/")
    # men_dictionary("../datasets/tennis/ATP/men/csv/")
    # get_edges_txt("../datasets/tennis/ATP/men/csv/")
    pass