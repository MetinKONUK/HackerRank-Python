def alternate(s):
    unique = list(set(s))
    combs = list()
    for i in range(len(unique)):
        for j in range(i+1, len(unique)):
            combs.append([unique[i], unique[j]])
    strs = list()
    for (a, b) in combs:
        res = ""
        for x in s:
            if x == a or x == b:
                res += x
        strs.append(res)
    longest = 0
    for st in strs:
        res, turn = True, st[0]
        for i in range(1, len(st)):
            if st[i] == turn: 
                res = False
                break
            turn = st[i]
        if res == True and len(st) > longest:
            longest = len(st)
    return longest
  #This is a O(N^2), brute-force solution.
