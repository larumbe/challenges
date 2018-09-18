# https://www.hackerrank.com/challenges/ctci-ice-cream-parlor/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=search

def indexOfPairs(n, s, b, e):
    """binary search for n"""
    if (b > e):
        return None
    if (b >= len(s) or e < 0):
        return None
    if (b == e and s[b][0] == n):
        return b
    
    sm = ((e-b) // 2) + b             # sublist midpoint

    if (s[sm][0] == n):
        return sm
    elif (s[sm][0] > n):
        return indexOfPairs(n, s, b, sm-1)
    else:
        return indexOfPairs(n, s, sm+1, e)

def printPair(a, b):
    if (a[1] < b[1]):
        x = a[1] + 1
        y = b[1] + 1
    else:
        y = a[1] + 1
        x = b[1] + 1
    print("{} {}".format(x,y))
    
def whatFlavors(cost, money):
    sc = sorted(list(zip(cost, range(len(cost)))))  # sort them and keep indices
    
    for i in range(len(sc)):
        comp = money - sc[i][0]    # complementary
        idx = indexOfPairs(comp, sc, i+1, len(sc)-1)
        if (idx is not None):
            printPair(sc[i], sc[idx])
            while(sc[idx+1][0] == comp):
                printPair(sc[i], sc[idx+1])
                idx += 1

def whatFlavorsBad(cost, money):
    for i in range(len(cost)):
        if (money-cost[i]) in cost[i+1:]:
            print("{} {}".format(i+1, cost[i+1:].index(money-cost[i])+2+i))
