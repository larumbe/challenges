import sys

# the great bottle neck is the number of times everything has to be recomputed
# use memoization

d = dict()

def minimumBribes(q):
    # start recursion
    res =  bribeRec(q, [0]*len(q))
    if (res != None):
        print("{}".format(res))
    else:
        print("Too chaotic")


# recursife function
def bribeRec(q, sw):
    # sw = swaps array
    # q = queue
    global d

    # base case
    if (q == list(range(1,len(q)+1))):
        return sum(sw)

    # pruning
    isSwap = False
    for j in range(len(q)-1):
        if ((sw[q[j]-1]) < 2):
            isSwap = True

    if (not(isSwap)):
        return None

    # explore the graph
    allNone = True
    localmin = sys.maxsize
    
    for i in range(len(q)-1):
        if ((sw[q[i]-1]) < 2):
            # check the table for intermediate results
            entry = d.get(repr(q))
            if (entry):
                res = entry
            else:
                tq = q[:]
                ts = sw[:]
                ts[tq[i]-1] += 1
                tq[i], tq[i+1] = tq[i+1], tq[i]
                res = bribeRec(tq, ts)
            if (res != None):
                allNone = False
                if (res < localmin):
                    localmin = res

    if (not(allNone)):
        # update the dictionary
        d[repr(q)] = localmin
        return localmin
    else:
        return None




