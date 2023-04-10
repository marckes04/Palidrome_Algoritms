import sys
import time

def colussi_space(s):
    n = len(s)
    p = [0] * n
    k = 0
    for i in range(1, n):
        while k > 0 and s[k] != s[i]:
            k = p[k - 1]
        if s[k] == s[i]:
            k += 1
        p[i] = k
    return sys.getsizeof(p)