__author__ = 'Ruslan'


def prefix(p):
    m = len(p)
    pref = [0 for i in range(m)]
    pref[0] = 0
    k = 0
    for q in range(1, m):
        while k > 0 and p[k] != p[q]:
            k = pref[k - 1]
        if p[k] == p[q]:
                k += 1
        pref[q] = k
    return pref


def matcher(t, p):
    n = len(t)
    m = len(p)
    pref = prefix(p)
    q = 0
    match = []
    for i in range(n):
        while q > 0 and p[q] != t[i]:
            q = pref[q - 1]
        if p[q] == t[i]:
            q += 1
        if q == m:
            match.append(i - m + 1)
            q = pref[q - 1]
    return match

