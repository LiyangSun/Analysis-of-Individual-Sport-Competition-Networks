import utils
import pickle
import pandas as pd
from os import listdir
from pathlib import Path


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


if __name__ == '__main__':
    dic_path = "../datasets/chess/chess_ids.pkl"
    csv_path = "../datasets/chess/csv/"
    # utils.player_dictionary(csv_path, dic_path, "White Player #", "Black Player #", False)
    # get_edges_txt(csv_path, "../datasets/chess/edges.txt")
    # get_weights(csv_path, "../datasets/chess/weights.pkl")
    # utils.get_uniq_edges_txt("../datasets/chess/weights.pkl", "../datasets/chess/uniq_edges.txt")

    # Create graphs for time evolution analysis (every 10 months)
    time = range(0, 101, 10)
    for i in range(len(time)-1):
        month_begin = time[i]
        month_end = time[i+1]
        get_edges_txt_10months(csv_path, month_begin, month_end,
                               csv_path[:-4] + "evolution/{}_{}.txt".format(month_begin+1, month_end))
