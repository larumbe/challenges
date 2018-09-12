def minimumBribes(q):
    # swaps array
    swv = [0] * len(q)
    # non-local sorted queue for base case lookups
    sq = list(range(1,len(q)+1))

    # recursife function
    def bribeRec(q, s):
        
        nonlocal sq

        # base case
        if (q == sq):
            return sum(s)

        # pruning
        isSwap = False
        for j in range(len(q)-1):
            if ((s[q[j]-1]) < 2):
                isSwap = True
                break

        if (not isSwap):
            return 0

        localmax = 0
        for i in range(len(q)-1):
            if ((s[q[i]-1]) < 2):  # there's a possible swap here
                # generate local copies of q,s for recursive call
                tq = q[:]
                ts = s[:]
                ts[tq[i]-1] += 1
                tq[i], tq[i+1] = tq[i+1], tq[i]
                res = bribeRec(tq, ts)
                if (res > localmax):
                    localmax = res
        
        return localmax        
                
    
    # start recursion
    return bribeRec(q, swv)




