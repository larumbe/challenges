# https://www.hackerrank.com/challenges/ctci-merge-sort/problem?h_l=interview&playlist_slugs%5B%5D%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D%5B%5D=sorting

# first implement merge sort
# then keep global variable of number of 2 list swaps

def countInversions(arr):
    return mergeSort(arr)[1]


def mergeSort(s):
    
    if (len(s) == 1):
        return (s,0)
    if (len(s) == 2):           # a swap could happen
        if (s[0] <= s[1]):
            return (s,0)
        else:
            return ([s[1], s[0]], 1)
        
    midpoint = len(s)//2
    r1 = mergeSort(s[:midpoint])
    r2 = mergeSort(s[midpoint:])
    s1 = r1[0]
    s2 = r2[0]
    c = r1[1] + r2[1]

    srt = []
    i, j = 0, 0
    while (i < len(s1) and j < len(s2)):
        if s1[i] <= s2[j]:
            srt.append(s1[i])
            i += 1
        else:
            srt.append(s2[j])
            j += 1
            c += 1
    if (i < len(s1)):
        srt.extend(s1[i:])
    elif (j < len(s2)):
        srt.extend(s2[j:])
      
    return (srt, c)
