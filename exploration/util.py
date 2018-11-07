import snap
import pickle


if __name__ == '__main__':
    dic_path = "../datasets/tennis/men_ids.pkl"
    with open(dic_path, 'rb') as dic_id:
        mydict = pickle.load(dic_id)
        txt_path = "../datasets/tennis/ATP/men/edges.txt"
        graph = snap.LoadEdgeList(snap.PNEANet, txt_path, 0, 1, ';')


