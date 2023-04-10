def colussi(string):
    i = 0
    j = len(string) - 1

    while i < j:
        if string[i] == string[j]:
            i += 1
            j -= 1
        else:
            j = len(string) - 1
            i += 1

    return i >= j