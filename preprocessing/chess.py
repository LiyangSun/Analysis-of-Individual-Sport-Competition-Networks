import utils
import pickle
import pandas as pd
from os import listdir


def get_edges_txt(csv_dir, dic_path, edges_path):
    """Get a txt file with all match results from csv_dir, first column is loser id, second is winner id
    This is so that when creating the directed graph, the loser references the winner"""

    with open(dic_path, 'rb') as dic_id:
        dic = pickle.load(dic_id)
        with open(edges_path, 'w') as edges:
            for f in listdir(csv_dir):
                df = pd.read_csv(csv_dir + f, header=0)
                for w, b, s in zip(list(df.loc[:, 'White Player #'].values), list(df.loc[:, 'Black Player #'].values)):
                    if s == 1:
                        w_id = dic[w]
                        b_id = dic[b]
                        edges.write(str(b_id) + ";" + str(w_id) + "\n")
                    elif s == 0:
                        w_id = dic[w]
                        b_id = dic[b]
                        edges.write(str(w_id) + ";" + str(b_id) + "\n")


if __name__ == '__main__':
    dic_path = "../datasets/chess/chess_ids.pkl"
    csv_path = "../datasets/chess/"
    # utils.player_dictionary(csv_path, dic_path, "White Player #", "Black Player #", False)
    get_edges_txt(csv_path, dic_path, "../datasets/chess/edges.txt")