def galil_giancarlo_algorithm(s):
    n = len(s)
    P = [0] * n
    k, r = 0, 0
    for i in range(n):
        if i < r:
            P[i] = min(r - i, P[k - (i - k)])
        while i + P[i] < n and s[P[i]] == s[i + P[i]]:
            P[i] += 1
        if i + P[i] > r:
            k, r = i, i + P[i]
    return max(P)