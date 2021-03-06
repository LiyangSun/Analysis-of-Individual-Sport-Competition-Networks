from __future__ import division
import snap


def path_proba(graph, name, n=1000):
    """Calculate the probability that a path exists between two uniformly random nodes (n simulations)"""
    p = 0
    for i in range(n):
        a = graph.GetRndNId()
        b = graph.GetRndNId()
        while a == b:
            b = graph.GetRndNId()
        NIdToDistH = snap.TIntH()
        snap.GetShortPath(graph, a, NIdToDistH, True)
        if b in NIdToDistH:
            p += 1
    print 'Using {} random pairs, the probability that a path exists between two nodes is ' \
          '{} for the {} network'.format(n, p / n, name)
    return p/n


def diameter_metrics(graph, name, n=1000):
    """Calculate:
    effective diameter (90-th percentile of the distribution of shortest path lengths)
    full diameter (longest-shortest path)
    avg shortest path length
    probability of a path existing"""
    results = {}
    eff, _, diam, s_path = snap.GetBfsEffDiamAll(graph, n, True)
    proba = path_proba(graph, name, n)

    results["a. Diameter"] = diam
    results["b. Effective diameter"] = eff
    results["c. Average shortest path length"] = s_path
    results["d. Path probability"] = proba

    return results
