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
