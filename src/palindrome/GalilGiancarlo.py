def Giacarlo(string):
    t = string + string[::-1]
    n = len(t)
    z = [0] * n
    l = r = 0

    for i in range(1, n):
        if i <= r:
            z[i] = min(r - i + 1, z[i - l])
        while i + z[i] < n and t[z[i]] == t[i + z[i]]:
            z[i] += 1
        if i + z[i] - 1 > r:
            l = i
            r = i + z[i] - 1
        if z[i] == len(string):
            return True

    return False
