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

def indexOf(n, s):
    """binary search for n"""
    if (s == []):
        return None
    

    
    

def pairs2(k, arr):
    total = 0
    sarr = sorted(arr)          # nlog(n)
    for i in range(len(sarr)):
        a1 = sarr[i] + k
        j = i+1
        while(True):
            idx = indexOf(a1, sarr[j:])
            if (idx is None):
                break
            total += 1
            j = j + idx

        a2 = sarr[i] - k
        if (a2 > 0):
            j = i+1
            while (True):
                idx = indexOf(a2, sarr[j:])
                if (idx is None):
                    break
                total += 1
                j = j + idx
                
    return total
