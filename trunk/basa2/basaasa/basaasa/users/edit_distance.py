from numpy import zeros, int32

def edit_distance(s1, s2):
    l1 = len(s1) + 1
    l2 = len(s2) + 1
    t = zeros((l1, l2), dtype=int32)
    for i in range(l1):
        t[i, 0] = i
    for j in range(l2):
        t[0, j] = j
    for i in range(1, l1):
        for j in range(1, l2):
            if s1[i - 1] == s2[j - 1]:
                cost = 0
            else:
                cost = 1
            t[i, j] = min(t[i - 1, j] + 1, \
                          t[i, j - 1] + 1, \
                          t[i - 1, j - 1] + cost)    
    return t[l1 - 1, l2 - 1]