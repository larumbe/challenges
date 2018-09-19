# https://www.hackerrank.com/challenges/max-array-sum/problem?h_l=interview&playlist_slugs%5B%5D%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D%5B%5D=dynamic-programming


def genNonAdjecent(s):
    for i in range(1, pow(2, len(s))):
        bs = (str(bin(i))[2:])
        if "11" in bs:
            continue
        if bs.count("1") == 1:
            continue
        bs = ("0" * (len(s)-len(bs)) + bs)[::-1]
        subset = []
        for j in range(len(bs)):
            if (bs[j] == '1'):
                subset.append(s[j])
        yield subset


def maxSubsetSum(arr):
    cmax = 0                    # currentmax
    for ss in genNonAdjecent(arr):
        cs = sum(ss)
        if cs > cmax:
            cmax = cs
    return cmax
