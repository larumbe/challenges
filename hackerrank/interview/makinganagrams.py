def makeAnakgram(a, b):
    # strategy:
    # find the multiset intersection of a and b
     # remove everything that isn't in it

    ia = [0] * (ord('z') - ord('a') + 1)
    ib = ia[:]
    ic = ia[:]

    # build histograms
    for i in range(len(a)):
        ia[ord(a[i])-ord('a')] += 1

    for i in range(len(b)):
        ib[ord(b[i])-ord('a')] += 1

    for j in range(len(ic)):
        ic[j] = ia[j] - ib[j]

    totalremove = 0
    for i in range(len(ic)):
        totalremove += abs(ic[i])

    return totalremove
