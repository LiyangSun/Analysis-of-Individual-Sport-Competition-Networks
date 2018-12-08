import snap
import pickle
from os import listdir
from os.path import isfile
import utils.overview as ov
import utils.RoIX as sr
import utils.bfs as bfs
import utils.similarity as sim
import utils.motif_detection as md
import utils.load as ld
import utils.time_evolution as evol
import utils.temporal_metrics as tmetrics
import utils.load as load
import utils.visualization as visu


if __name__ == '__main__':
    dic_path = "../datasets/tennis/men_ids.pkl"
    with open(dic_path, 'rb') as dic_id:
        mydict = pickle.load(dic_id)
        G = load.load_global("tennis_men")
        G_simple_directed = load.load_global("tennis_men", multi=False)
        G_simple_undirected = load.load_global("tennis_men", multi=False, directed=False)
        graphs = load.load_temporal("tennis_men", multi=False)
        results_multi = "../results/summary_tennismen_multi_directed.txt"
        results_directed = "../results/summary_tennismen_simple_directed.txt"
        results_undirected = "../results/summary_tennismen_simple_undirected.txt"

        # Time evolution
        #
        # evol.density_evolution(graphs, "tennismen", "years", duration = [2000, 2018])
        # evol.clust_evolution(graphs, "tennismen", "years", duration = [2000, 2018])
        # evol.active_nodes_evolution(graphs, "tennismen", "years", duration = [2000, 2018])
        # evol.edges_evolution(graphs, "tennismen", "years", duration = [2000, 2018])
        # evol.max_scc_evolution(graphs, "tennismen", "years", duration = [2000, 2018])
        # evol.alternate_clust_evolution(graphs, "tennismen", "years", duration=[2000, 2018])

        # Visualization global
        #
        # nxgraph = visu.load_graph_networkx("../datasets/tennis/ATP/men/uniq_edges.txt")
        # visu.visualize_networkx(nxgraph, "tennismen")
        # visu.in_deg_distribution(graphs[0], "test")

        # Basic properties
        #
        # prop = ov.quick_properties(G, "Tennis ATP Men Multi-directed", dic_path)
        # ov.txt_results(prop, "tennismen_multi_directed")
        # prop = ov.quick_properties(G_simple_directed, "Tennis ATP Men Simple-directed", dic_path)
        # ov.txt_results(prop, "tennismen_simple_directed")
        # prop = ov.quick_properties(G_simple_directed, "Tennis ATP Men Simple-undirected", dic_path)
        # ov.txt_results(prop, "tennismen_simple_undirected")

        # BFS, bowtie-assumptions
        #
        # bfs.cumul_BFS(G_simple_directed, "tennismen")
        ov.add_text(results_multi, "\n## Bowtie Analysis")
        ov.add_text(results_directed, "\n## Bowtie Analysis")
        ov.add_text(results_undirected, "\n## Bowtie Analysis")
        res = bfs.bowtie_components(G, "tennismen_multi")
        res_dir = bfs.bowtie_components(G_simple_directed, "tennismen_simple_directed")
        res_undir = bfs.bowtie_components(G_simple_undirected, "tennismen_simple_undirected")
        ov.add_results(results_multi, res)
        ov.add_results(results_directed, res_dir)
        ov.add_results(results_undirected, res_undir)

        # Other properties
        #




        # Temporal metrics
        #
        # print(tmetrics.charac_temporal_clust_coef(graphs))
        # print(tmetrics.charac_temporal_alt_clust_coef(graphs))

        # print(tmetrics.temporal_clust_coef(graphs_time, 1))
        # print(tmetrics.temporal_clust_coef(graphs_time, 1, False))
        # print(snap.GetNodeClustCf(graph, 1))

        # features = sr.basic_features(graph, True)
        # rec_features = sr.recursive_features(graph, K=2, directed=True)
        # sr.sim_node_max("Nadal R.", features, dic_path)
        # sr.sim_node_max("Nadal R.", rec_features, dic_path)
        # sr.plot_sim_hist("Federer R.", rec_features, dic_path, bin_width=30)

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