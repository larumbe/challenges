# https://www.hackerrank.com/challenges/pairs/problem?h_l=interview&playlist_slugs%5B%5D%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D%5B%5D=search

def pairs(k, arr):
    total = 0
    for i in range(len(arr)):
        for j in range(i, len(arr)):
            if (abs(arr[i]-arr[j]) == k):
                total += 1
    return total

# sort the list:
# for every n in sorted(arr):

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

def pairs2(k, arr):
    total = 0
    sarr = sorted(arr)          # nlog(n)
    for i in range(len(sarr)):
        a1 = sarr[i] + k
        j = i+1
        while(True):
            idx = indexOf(a1, sarr, j, len(sarr)-1)
            if (idx is None):
                break
            total += 1
            j = idx + 1

        a2 = sarr[i] - k
        if (a2 > 0):
            j = i+1
            while (True):
                idx = indexOf(a2, sarr, j, len(sarr)-1)
                if (idx is None):
                    break
                total += 1
                j = idx + 1
                
    return total
