# https://www.hackerrank.com/challenges/maximum-subarray-sum/problem?h_l=interview&playlist_slugs%5B%5D%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D%5B%5D=search
import math

# naive combinatorial implementation
def genSubsets(s):
    for i in range(1, pow(2, len(s))):
        bs = (str(bin(i))[2:])
        bs = ("0" * (len(s)-len(bs)) + bs)[::-1]
        subset = []
        for j in range(len(bs)):
            if (bs[j] == '1'):
                subset.append(s[j])
        yield subset

def maximumSum(a, m):
    top = 0
    for s in genSubsets(a):
        su = sum(s) % m
        if (su > top):
            top = su
    return top
