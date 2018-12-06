import snap
import pickle
from os import listdir
from os.path import isfile
import utils.overview as ov
import utils.structural_role as sr
import utils.bfs as bsf
import utils.similarity as sim
import utils.motif_detection as md
import utils.load as ld
import utils.time_evolution as evol
import utils.temporal_metrics as tmetrics
import utils.load as load


if __name__ == '__main__':
    dic_path = "../datasets/tennis/men_ids.pkl"
    with open(dic_path, 'rb') as dic_id:
        mydict = pickle.load(dic_id)
        G = load.load_global("tennis_men")
        graphs = load.load_temporal("tennis_men", multi=False)
        # evol.density_evolution(graphs_time, "test", "years")
        # evol.clust_evolution(graphs_time, "test", "years")
        # evol.nodes_evolution(graphs_time, "", "")
        # evol.edges_evolution(graphs_time, "", "")
        # evol.max_scc_evolution(graphs_time, "", "")
        # print(tmetrics.temporal_clust_coef(graphs_time, 1))
        # print(tmetrics.temporal_clust_coef(graphs_time, 1, False))
        # print(snap.GetNodeClustCf(graph, 1))


        # ov.quick_properties(graph, "Tennis ATP Men", dic_path)
        # ov.quick_properties(graph_directed, "Tennis ATP Men", dic_path)

        # features = sr.basic_features(graph, True)
        # rec_features = sr.recursive_features(graph, K=2, directed=True)
        # sr.sim_node_max("Nadal R.", features, dic_path)
        # sr.sim_node_max("Nadal R.", rec_features, dic_path)
        # sr.plot_sim_hist("Federer R.", rec_features, dic_path, bin_width=30)

        # bsf.cumul_BFS(graph, "tennis men")
        # bsf.bowtie_components(graph, "tennis")
        # bsf.path_proba(graph, "tennis", 10000)

        # sim.JA_similarity_max(graph_directed, "Federer R.", dic_path, directed=True)
        # sim.CN_similarity_max(graph_directed, "Federer R.", dic_path, directed=True)

        # directed_3 = md.load_3_subgraphs()
        # motif_counts = [0] * len(directed_3)
        # config_graph, clustering_coeffs = md.gen_config_model_rewire(graph_directed, 1000)
        # md.plot_rewiring_clust(clustering_coeffs)
        # md.enumerate_subgraph(graph_directed, directed_3, 3, verbose=True)
        # if True:
        #    print(motif_counts)
        # md.zscores_3(txt_path, directed_3)



        # Basic info on graph
        # snap.PrintInfo(graph, "Tennis ATP Men", "infotennis", False)

        # Get approximate of ... using BFS on 100 rdm starting nodes:
        # effective diameter (90-th percentile of the distribution of shortest path lengths)
        # full diameter (longest-shortest path)
        # avg shortest path length
        # print snap.GetBfsEffDiamAll(graph, 10000, True)

        # Uses the Clauset/Newman/Moore community detection method for large networks.
        # At every step of the algo two communities that contribute max positive value to global modularity are merged.
        # Fills CmtyV with all the communities detected and returns the modularity of the network.
        # CmtyV = snap.TCnComV()
        # print(snap.CommunityCNM(graph_undirected, CmtyV))
        # print(CmtyV.Len())

        # Same but with Girvan/Newman method
        # CmtyV = snap.TCnComV()
        # print snap.CommunityGirvanNewman(graph_undirected, CmtyV)

        # print snap.GetClustCf(graph)

        # Get nb of triads, subgraphs formed by 3 nodes
        # print snap.GetTriads(graph)

        # Get nb of closed triads and open triads, graph considered as undirected
        # print snap.GetTriadsAll(graph)

        # Computes SngVals largest singular values of the adjacency matrix representing the directed graph Graph
        # SngVals = 4
        # SngValV = snap.TFltV()
        # snap.GetSngVals(graph_directed, SngVals, SngValV)
        # for item in SngValV:
        #     print item