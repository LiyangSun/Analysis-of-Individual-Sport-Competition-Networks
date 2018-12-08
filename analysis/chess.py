import snap
import pickle
from os import listdir
from os.path import isfile
import utils.time_evolution as evol
import utils.overview as ov
import utils.RoIX as sr
import utils.bfs as bfs
import utils.similarity as sim
import utils.motif_detection as md
import utils.temporal_metrics as tmetrics
import utils.load as load
import utils.visualization as visu


if __name__ == '__main__':
    dic_path = "../datasets/chess/chess_ids.pkl"
    with open(dic_path, 'rb') as dic_id:
        mydict = pickle.load(dic_id)
        G = load.load_global("chess")
        G_simple_directed = load.load_global("chess", multi=False)
        G_simple_undirected = load.load_global("chess", multi=False, directed=False)
        graphs = load.load_temporal("chess", multi=False)

        # Time evolution
        #
        # evol.density_evolution(graphs, "chess", "10-months")
        # evol.clust_evolution(graphs, "chess", "10-months")
        # evol.active_nodes_evolution(graphs, "chess", "10-months")
        # evol.edges_evolution(graphs, "chess", "10-months")
        # evol.max_scc_evolution(graphs, "chess", "10-months")
        # evol.alternate_clust_evolution(graphs, "chess", "10-months")

        # Visualization global
        #
        # nxgraph = visu.load_graph_networkx("../datasets/chess/uniq_edges.txt")
        # visu.visualize_networkx(nxgraph, "chess")

        # Basic properties
        #
        # prop = ov.quick_properties(G, "Chess Multi-directed", dic_path)
        # ov.txt_results(prop, "chess_multi_directed")
        # prop = ov.quick_properties(G_simple_directed, "Chess Simple-directed", dic_path)
        # ov.txt_results(prop, "chess_simple_directed")
        # prop = ov.quick_properties(G_simple_directed, "Chess Simple-undirected", dic_path)
        # ov.txt_results(prop, "chess_simple_undirected")

        # BFS, bowtie-assumptions
        #
        bfs.cumul_BFS(G_simple_directed, "chess")

        # Temporal metrics
        #
        # print(tmetrics.charac_temporal_clust_coef(graphs))
        # print(tmetrics.charac_temporal_alt_clust_coef(graphs))


        # ov.quick_properties(graph, "Chess", dic_path)

        # features = sr.basic_features(graph, True)
        # rec_features = sr.recursive_features(graph, K=2, directed=True)
        # sr.sim_node_max(7848, features, dic_path)
        # sr.sim_node_max(7848, rec_features, dic_path)
        # sr.plot_sim_hist(7848, rec_features, dic_path, bin_width=30)

        # bsf.cumul_BFS(graph, "chess", 1000)
        # bsf.bowtie_components(graph, "tennis")
        # bsf.path_proba(graph, "tennis", 10000)

        # sim.JA_similarity_max(graph_directed, 7848, dic_path, directed=True)
        # sim.CN_similarity_max(graph_directed, 7848, dic_path, directed=True)

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
        # print(CmtyV.Len())

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