def KrutMorris(string):
    i = 0
    j = len(string) - 1
    pi = [0] * len(string)
    k = 0

    while j > 0:
        if string[i] == string[j]:
            i += 1
            j -= 1
        elif k > 0:
            k = pi[k - 1]
        else:
            j = 0

        if i == j or i + 1 == j:
            return True

        if string[i] == string[k]:
            k += 1

        pi[j] = k

    return i >= j
