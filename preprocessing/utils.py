from pathlib import Path
import pickle
import pandas as pd
from os import listdir


def player_dictionary(csv_dir, dic_path, win_col, lose_col, have_names=True):
    """If we have players' names, updates a dict where {keys = players, values = integer id} for purposes:
    - graph: nodes ID are integers
    - analysis: keep track of tennis players' IDs
    Add players from csv files in 'csv_dir' if they have not been added yet

    If not, players' names are their IDs"""
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
        for name in list(df.loc[:, win_col].values):
            if name not in dic.keys():
                if have_names:
                    ids = len(dic)
                    dic[name] = ids
                else:
                    dic[name] = int(name)
        for name in list(df.loc[:, lose_col].values):
            if name not in dic.keys():
                if have_names:
                    ids = len(dic)
                    dic[name] = ids
                else:
                    dic[name] = int(name)

    with open(dic_path, 'wb') as f:
        pickle.dump(dic, f, pickle.HIGHEST_PROTOCOL)


def get_uniq_edges_txt(weights_path, uniq_edges_path):
    """Get a txt file with all match results from weights_path, first column is loser id, second is winner id,
    with NO repetition
    This is so that when creating the directed graph, the loser references the winner"""

    with open(weights_path, 'rb') as wdic_id:
        weights = pickle.load(wdic_id)
        with open(uniq_edges_path, 'w') as edges:
            for (x, y) in weights.keys():
                edges.write(str(x) + ";" + str(y) + "\n")