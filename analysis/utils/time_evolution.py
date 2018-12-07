from __future__ import division
import matplotlib.pyplot as plt
import snap
from clustering import alternative_clust


def density_evolution(graphs, name, time_units, directed=True, verbose=False, duration=None):
    """Plot the time evolution of the density of snap graph in graphs"""
    Y = []
    for g in graphs:
        e = g.GetEdges()
        n = g.GetNodes()
        if directed:
            Y.append(e / (n * (n - 1)))
        else:
            Y.append(2 * e / (n * (n - 1)))
    X = range(len(Y))
    if duration is not None:
        X = range(duration[0], duration[1]+1)
    plt.plot(X, Y)
    plt.xlabel("Time in {}".format(time_units))
    plt.ylabel("Density")
    plt.title("Density evolution of {} graphs".format(name))
    plt.savefig("density_time_{}".format(name))
    if verbose:
        plt.show()


def clust_evolution(graphs, name, time_units, verbose=False, duration=None):
    """Plot the time evolution of the avg clustering coefficient (Watts Strogatz definition) of snap graph in graphs"""
    Y = []
    for g in graphs:
        Y.append(snap.GetClustCf(g))
    X = range(len(Y))
    if duration is not None:
        X = range(duration[0], duration[1]+1)
    plt.plot(X, Y)
    plt.xlabel("Time in {}".format(time_units))
    plt.ylabel("Avg Clustering Coefficient")
    plt.title("Avg Clustering coefficient of {} graphs".format(name))
    plt.savefig("clust_time_{}".format(name))
    if verbose:
        plt.show()


def alternate_clust_evolution(graphs, name, time_units, verbose=False, duration=None):
    """Plot the time evolution of the alternate avg clustering coefficient of snap graph in graphs"""
    Y = []
    for g in graphs:
        Y.append(alternative_clust(g))
    X = range(len(Y))
    if duration is not None:
        X = range(duration[0], duration[1]+1)
    plt.plot(X, Y)
    plt.xlabel("Time in {}".format(time_units))
    plt.ylabel("Alternate Clustering Coefficient")
    plt.title("Alternate Clustering coefficient of {} graphs".format(name))
    plt.savefig("clustAlt_time_{}".format(name))
    if verbose:
        plt.show()


def active_nodes_evolution(graphs, name, time_units, verbose=False, duration=None):
    """Plot the time evolution of the number of nodes with degree of at least one of snap graph in graphs"""
    Y = []
    for g in graphs:
        Y.append(g.GetNodes()-snap.CntDegNodes(g, 0))
    X = range(len(Y))
    if duration is not None:
        X = range(duration[0], duration[1]+1)
    plt.plot(X, Y)
    plt.xlabel("Time in {}".format(time_units))
    plt.ylabel("Number of active nodes")
    plt.title("Active nodes evolution of {} graphs".format(name))
    plt.savefig("nodes_time_{}".format(name))
    if verbose:
        plt.show()


def edges_evolution(graphs, name, time_units, verbose=False, duration=None):
    """Plot the time evolution of the number of edges of snap graph in graphs"""
    Y = []
    for g in graphs:
        Y.append(g.GetEdges())
    X = range(len(Y))
    if duration is not None:
        X = range(duration[0], duration[1]+1)
    plt.plot(X, Y)
    plt.xlabel("Time in {}".format(time_units))
    plt.ylabel("Number of edges")
    plt.title("Edges evolution of {} graphs".format(name))
    plt.savefig("edges_time_{}".format(name))
    if verbose:
        plt.show()


def max_scc_evolution(graphs, name, time_units, verbose=False, duration=None):
    """Plot the time evolution of the number of nodes in the largest SCC of snap graph in graphs"""
    Y = []
    for g in graphs:
        scc = snap.GetMxScc(g)
        Y.append(scc.GetNodes())
    X = range(len(Y))
    if duration is not None:
        X = range(duration[0], duration[1]+1)
    plt.plot(X, Y)
    plt.xlabel("Time in {}".format(time_units))
    plt.ylabel("Number of nodes in largest SCC")
    plt.title("SCC nodes evolution of {} graphs".format(name))
    plt.savefig("SCCnodes_time_{}".format(name))
    if verbose:
        plt.show()