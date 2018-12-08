from __future__ import division
import numpy as np
import scipy.integrate as integrate
import matrix as mx


def step(x):
    """Step function with step at 0"""
    if x >= 0:
        return 1
    else:
        return 0


def step_function(x):
    """Vectorized step function"""
    vstep = np.vectorize(step)
    return vstep(x)


def cumul_distrib_function(x, eigenvector, complex=True):
    """Cumulative distribution function with x any number and eigenvector a numpy array"""
    n = len(eigenvector)
    xvector = np.array([x]*n)
    if complex:
        return sum(step_function(xvector-np.real(eigenvector))*step_function(xvector-np.imag(eigenvector)))/n
    else:
        return sum(step_function(xvector-eigenvector))/n


def norm1_distrib(x, ev1, ev2):
    """Returns the absolute of the difference between cumulative distributions of ev1 and ev2"""
    return abs(cumul_distrib_function(x, ev1) - cumul_distrib_function(x, ev2))


def distribution_kruglov_distance(ev1, ev2):
    """Returns the Kruglov distance of the cumulative distribution of ev1 and ev2, with absolute function"""
    return integrate.quad(lambda x: norm1_distrib(x, ev1, ev2), -np.inf, np.inf)[0]


def network_distance(g1, g2, weights_path_1, weights_path_2, in_degree=True):
    """Return the distance between graphs g1 and g2 defined by the functions above"""
    n1 = g1.GetNodes()
    n2 = g2.GetNodes()
    n = min(n1, n2)
    _, ev1 = mx.sorted_laplacian_eigen(g1, weights_path_1, in_degree)
    _, ev2 = mx.sorted_laplacian_eigen(g2, weights_path_2, in_degree)
    dist = 0
    for i in range(n):
        dist += distribution_kruglov_distance(ev1[:, i], ev2[:, i])
    dist = dist / n
    return dist