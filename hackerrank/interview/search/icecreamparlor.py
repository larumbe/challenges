# https://www.hackerrank.com/challenges/ctci-ice-cream-parlor/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=search

def indexOf(n, s, b, e):
    """binary search for n"""
    if (b > e):
        return None
    if (b >= len(s) or e < 0):
        return None
    if (b == e and s[b] == n):
        return b
    
    sm = ((e-b) // 2) + b             # sublist midpoint

    if (s[sm] == n):
        return sm
    elif (s[sm] > n):
        return indexOf(n, s, b, sm-1)
    else:
        return indexOf(n, s, sm+1, e)


def whatFlavors(cost, money):
    for i in range(len(cost)):
        if (money-cost[i]) in cost[i+1:]:
            print("{} {}".format(i+1, cost[i+1:].index(money-cost[i])+2+i))

#  do it again with binary search
def whatFlavoursBin(cost, money):
    sc = sorted(cost)           # sorted costs
    # gotta keep the original indices
    
    for i in range(len(cost)):
        comp = money - sc[i]    # complementary
        idx = indexOf(comp, sc, i+1, len(sc)-1)
        if (idx is not None):
            print("{} {}".format(sc[i], sc[idx]))
            while(sc[idx+1] == comp):
                print("{} {}".format(sc[i], sc[idx+1]))
                idx += 1
