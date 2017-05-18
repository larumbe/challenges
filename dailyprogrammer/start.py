
# https://www.reddit.com/r/dailyprogrammer/comments/69y21t/20170508_challenge_314_easy_concatenated_integers/
# http://www.shiftedup.com/2015/05/07/five-programming-problems-every-software-engineer-should-be-able-to-solve-in-less-than-1-hour

# DONE

import functools

def probsort(a,b):
    if (len(str(a)) == len(str(b))):
        return a - b
    c , d = max(a,b), min(a,b)
    if (str(c)[:len(str(d))] == str(d)):
        if (str(c)[len(str(d))] > str(d)[0]):
            if (c == b): return -1
            else: return 1
        else:
            if (c == b): return 1
            else: return -1
    else:
        minlen = len(str(min(a,b)))
        return (int(str(a)[:minlen]) - int(str(b)[:minlen]))

def nextlargestnumber(numlist):
    return int("".join([str(n) for n in sorted(numlist, key=functools.cmp_to_key(probsort), reverse=True)]))

def nextsmallestnumber(numlist):
    return int("".join([str(n) for n in sorted(numlist, key=functools.cmp_to_key(probsort))]))

