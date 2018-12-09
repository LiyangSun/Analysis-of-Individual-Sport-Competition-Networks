from __future__ import division
import snap
import matplotlib.pyplot as plt
import numpy as np


def cumul_BFS(graph, name, N=1000):
    """Get n random nodes and find the number of nodes in their inward and outward BFS trees.
    Plot the cumulative number of nodes reached in the BFS runs"""

    X_in, X_out = [], []
    for i in range(N):
        n = graph.GetRndNId()

        g_out = snap.GetBfsTree(graph, n, True, False)
        g_in = snap.GetBfsTree(graph, n, False, True)

        X_in.append(g_in.GetNodes())
        X_out.append(g_out.GetNodes())

    X_in, X_out = sorted(X_in), sorted(X_out)

    x = np.linspace(0.0, 1.0, N)
    plt.subplot(1, 2, 1)
    plt.plot(x, X_in)
    plt.title('{}, using inlinks'.format(name))

    plt.subplot(1, 2, 2)
    plt.plot(x, X_out)
    plt.title('{}, using outlinks'.format(name))

    plt.savefig("../results/reachability_bfs/reachability_{}".format(name), bbox_inches="tight")


def bowtie_components(graph, name):
    """Give sizes of DISCONNECTED, IN, OUT, SCC"""
    results = {}

    N = graph.GetNodes()

    SCC = snap.GetMxScc(graph)
    n = SCC.GetRndNId()

    disc = N - snap.GetMxWcc(graph).GetNodes()
    scc = SCC.GetNodes()
    SCC_in = snap.GetBfsTree(graph, n, False, True)
    SCC_out = snap.GetBfsTree(graph, n, True, False)
    in1 = SCC_in.GetNodes() - scc
    out = SCC_out.GetNodes() - scc
    tt = N - disc - scc - in1 - out

    results["a. SCC"] = scc
    results["b. IN"] = in1
    results["c. OUT"] = out
    results["d. TENDRILS + TUBES"] = tt
    results["e. DISCONNECTED"] = disc

    print 'Total nodes in {} network: {}'.format(name, N)
    print 'DISCONNECTED: {}'.format(disc)
    print 'SCC: {}'.format(scc)
    print 'IN: {}'.format(in1)
    print 'OUT: {}'.format(out)
    print 'TENDRILS + TUBES: {}'.format(tt)

    return results

if __name__ == '__main__':
    pass
