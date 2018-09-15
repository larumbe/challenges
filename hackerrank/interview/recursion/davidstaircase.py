# https://www.hackerrank.com/challenges/ctci-recursive-staircase/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=recursion-backtracking

sdic = {1:1, 2:2, 3:4}

def stepPerms(n):
    if n <= 2:
        return n
    if n is 3:
        return 4
    else:
        res1 = sdic.get(n-1)
        if (res1 is None):
            res1 = stepPerms(n-1)
            sdic[n-1] = res1
        res2 = sdic.get(n-2)
        if (res2 is None):
            res2 = stepPerms(n-2)
            sdic[n-2] = res2
        res3 = sdic.get(n-3)
        if (res3 is None):
            res3 = stepPerms(n-3)
            sdic[n-3] = res3

        return (res1+res2+res3)%10000000007
