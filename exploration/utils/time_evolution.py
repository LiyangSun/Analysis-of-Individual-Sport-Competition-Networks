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
    X = range(len(Y))
    plt.plot(X, Y)
    plt.xlabel("Time in {}".format(time_units))
    plt.ylabel("Density")
    plt.title(name)
    plt.show()


def clust_evolution(graphs, name, time_units):
    """Plot the time evolution of the avg clustring coefficient of snap graph in graphs"""
    Y = []
    for g in graphs:
        Y.append(snap.GetClustCf(g))
    X = range(len(Y))
    plt.plot(X, Y)
    plt.xlabel("Time in {}".format(time_units))
    plt.ylabel("Avg Clustering Coefficient")
    plt.title(name)
    plt.show()



