# https://www.hackerrank.com/challenges/triple-sum/problem?h_l=interview&playlist_slugs%5B%5D%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D%5B%5D=search

def thoseLesser(n, s, b, e):
    if (b == e):
        if (s[b] <= n): return b + 1
        else: return b
    sm = ((e-b) // 2) + b
    if (s[sm] == n): return sm + 1
    elif (s[sm] > n): return thoseLesser(n, s, b, sm-1)
    else: return thoseLesser(n, s, sm+1, e)

def triplets(a, b, c):
    count = 0
    sa = sorted(list(set(a)))
    sb = sorted(list(set(b)))
    sc = sorted(list(set(c)))

    for p in sb:
        la = thoseLesser(p, sa, 0, len(sa)-1)
        lb = thoseLesser(p, sc, 0, len(sc)-1)
        count += la * lb
    
    return count
