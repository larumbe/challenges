# https://www.hackerrank.com/challenges/recursive-digit-sum/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=recursion-backtracking

d = dict()

def superDigit(n, k):
    return superDigitRec(sum([int(i) for i in str(n)])*k)

def superDigitRec(n):
    if n < 10:
        return n

    s = sum([int(i) for i in str(n)])
    e = d.get(s)
    if (e is None):
        e = superDigitRec(s)
        d[s] = e
    return e
