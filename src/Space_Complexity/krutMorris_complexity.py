import sys

def kruskal_morris_space(n):
    p = [0] * n
    c = [0] * n
    return sys.getsizeof(p) + sys.getsizeof(c)