def isValid(s):
    hist = [0] * (ord('z') - ord('a') + 1)
    for c in s:
        hist[ord(c)-ord('a')] += 1
    hist = [n for n in hist if n > 0]

    d = dict()
    for h in hist:
        if (d.get(h) is None):
            d[h] = 1
        else:
            d[h] += 1

    keys = list(d.keys())
    if (len(keys) == 1):
        return "YES"
    elif (len(keys) > 2):
        return "NO"
    else:
        if ((keys[1] == keys[0] + 1) and (d[keys[1]] == 1)):
            return "YES"
        elif ((keys[0] == 1) and (d[keys[0]] == 1)):
            return "YES"
        else:
            return "NO"
