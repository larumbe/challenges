# https://www.hackerrank.com/challenges/angry-children/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=greedy-algorithms
import sys


def maxMin(k, arr):
    sa = sorted(arr)
    minunfair = sys.maxsize

    for i in range(len(sa)-k+1):
        cu = sa[i+k-1] - sa[i]
        if (cu < minunfair):
            minunfair = cu
    return minunfair
