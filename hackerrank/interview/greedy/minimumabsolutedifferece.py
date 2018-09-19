import sys

def minimumAbsoluteDifference(arr):
    sa = sorted(arr)            # sorted array

    md = sys.maxsize             # minimum distance
    for i in range(len(sa)-1):
        cd = abs(sa[i] - sa[i+1])  # current distance
        if (cd < md): md = cd
    return md
