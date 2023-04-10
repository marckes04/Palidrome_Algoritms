def kruskal_morris_algorithm(s):
    n = len(s)
    P = [0] * n
    k, r = 0, 0
    for i in range(1, n):
        if i < r:
            P[i] = min(r - i, P[k - (i - k)])
        while i + P[i] < n and s[i + P[i]] == s[i - P[i]]:
            P[i] += 1
        if i + P[i] > r:
            k, r = i, i + P[i]
    return max(P)