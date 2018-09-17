# https://www.hackerrank.com/challenges/count-triplets-1/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=dictionaries-hashmaps

powers = dict()

def powerOf(r, n):
    e = powers.get((r, n))
    if (e is not None):
        return e
    else:       # calculate exponent e such that (r**e == n)
        i = 0
        z = n
        while (z > 1):
            if (z % r != 0):
                return None
            i += 1
            # look up table again
            z = z // r
            j = powers.get((r, z))
            if (j is not None):
                return i + j
    powers[(r, n)] = i          # memorise it
    return i

def countTriplets(arr, r):
    tc = 0                      # triplet count
    # calculate consecutive powers
    for i in range(len(arr)-2):
        e1 = powerOf(r, arr[i])
        if (e1 is None): continue
        for j in range(i+1, len(arr)-1):
            e2 = powerOf(r, arr[j])
            if (e2 is None or (e2 != e1 + 1)): continue
            for k in range(j+1, len(arr)):
                e3 = powerOf(r, arr[k])
                if (e3 is not None and (e3 == e2 + 1)):
                    tc += 1
    return tc

def countTriplets2(arr, r):
    # what's with radix number 1
    pr = dict()                 # powers of r and their positions in arr
    tc = 0
    
    for x in range(len(arr)):
        e = powerOf(r, arr[x])
        if (e is not None):
            il = pr.get(e)
            if (il is not None):
                il.append(x)
                pr[e] = il
            else:
                pr[e] = [x]

    # could you sort the lists of powers in nln for better performance?
    for i in range(len(arr)-2):
        p1 = powerOf(r, arr[i])
        if (p1 is None): continue
        l2 = pr.get(p1+1)
        l3 = pr.get(p1+2)
        if (l2 is None or l3 is None): continue
        for j in l2:
            for k in l3:
                if (j > i and k > j):
                    tc += 1
    return tc
