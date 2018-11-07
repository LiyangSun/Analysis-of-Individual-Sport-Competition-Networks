import snap
import pickle
import utils.overview as ov
import utils.structural_role as sr


if __name__ == '__main__':
    dic_path = "../datasets/tennis/men_ids.pkl"
    with open(dic_path, 'rb') as dic_id:
        mydict = pickle.load(dic_id)
        txt_path = "../datasets/tennis/ATP/men/edges.txt"
        graph = snap.LoadEdgeList(snap.PNEANet, txt_path, 0, 1, ';')

        # ov.quick_properties(graph, "Tennis ATP Men", dic_path)
        # ov.visu(graph, "tennisATPmen")

        # features = sr.basic_features(graph, True)
        # rec_features = sr.recursive_features(graph, K=2, directed=True)
        # sr.sim_node_max("Nadal R.", features, dic_path)
        # sr.sim_node_max("Nadal R.", rec_features, dic_path)
        # sr.plot_sim_hist("Federer R.", rec_features, dic_path, bin_width=30)
