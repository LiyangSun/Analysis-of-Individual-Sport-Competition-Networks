from __future__ import division
import matplotlib.pyplot as plt
import snap


def density_evolution(graphs, name, time_units, directed=True):
    """Plot the time evolution of the density of snap graph in graphs"""
    Y = []
    for g in graphs:
        e = g.GetEdges()
        n = g.GetNodes()
        if directed:
            Y.append(e / (n * (n - 1)))
        else:
            Y.append(2 * e / (n * (n - 1)))
    plt.plot(Y)
    plt.xlabel("Time in {}".format(time_units))
    plt.ylabel("Density")
    plt.title(name)
    plt.show()


def clust_evolution(graphs, name, time_units):
    """Plot the time evolution of the avg clustring coefficient of snap graph in graphs"""
    Y = []
    for g in graphs:
        Y.append(snap.GetClustCf(g))
    plt.plot(Y)
    plt.xlabel("Time in {}".format(time_units))
    plt.ylabel("Avg Clustering Coefficient")
    plt.title(name)
    plt.show()


def nodes_evolution(graphs, name, time_units):
    """Plot the time evolution of the number of nodes of snap graph in graphs"""
    Y = []
    for g in graphs:
        Y.append(g.GetNodes())
    plt.plot(Y)
    plt.xlabel("Time in {}".format(time_units))
    plt.ylabel("Number of nodes")
    plt.title(name)
    plt.show()


def edges_evolution(graphs, name, time_units):
    """Plot the time evolution of the number of edges of snap graph in graphs"""
    Y = []
    for g in graphs:
        Y.append(g.GetEdges())
    plt.plot(Y)
    plt.xlabel("Time in {}".format(time_units))
    plt.ylabel("Number of edges")
    plt.title(name)
    plt.show()


def max_scc_evolution(graphs, name, time_units):
    """Plot the time evolution of the number of nodes in the largest CC of snap graph in graphs"""
    Y = []
    for g in graphs:
        scc = snap.GetMxScc(g)
        Y.append(scc.GetNodes())
    plt.plot(Y)
    plt.xlabel("Time in {}".format(time_units))
    plt.ylabel("Number of edges")
    plt.title(name)
    plt.show()