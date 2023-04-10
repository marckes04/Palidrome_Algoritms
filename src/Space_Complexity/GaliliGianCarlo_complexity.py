def space_complexity_galil_giancarlo(n):
    b = 0
    c = 1
    k = 2
    s = [0] * n
    p = [0] * n
    while k < n:
        if b + c == 0:
            p[k] = k + 1
            c = 1
            k += 1
        elif k + c == n + 1:
            p[k] = k - 1
            b = s[k] = c = 0
            k += 1
        elif s[k - b - 1] == c - b:
            c += 1
            p[k] = p[k - 1]
            k += 1
        else:
            s[k] = c - b
            c = max(0, s[b - 1])
            b = k - c
            k = max(k + 1, b + 1)
            while k < n and c < n - k + 1 and s[k - b - 1] == c:
                c += 1
                p[k] = k - 1
                k += 1
    return sum([8 * n.bit_length() for n in s]) + sum([8 * n.bit_length() for n in p])