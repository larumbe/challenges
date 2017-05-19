
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

def nextlargestnumber2(numlist):
    return int("".join([str(n) for n in sorted(numlist, key=functools.cmp_to_key(lambda x,y: int(str(x)+str(y)) - int(str(y) + str(x))) , reverse=True)]))

# Problem 1
# Write three functions that compute the sum of the numbers in a given list using a for-loop, a while-loop, and recursion.

def funcfor(nlist):
    res = 0
    for i in range (0,len(nlist)):
        res += nlist[i]
    return res

def funcwhile(nlist):
    res, i = 0, 0
    while (i < len(nlist)):
        res += nlist[i]
        i += 1
    return res

def funcrec(nlist):
    if (nlist == []):
        return 0
    else:
        return nlist[0] + funcrec(nlist[1:])

# Problem 2
# Write a function that combines two lists by alternatingly taking
# elements. For example: given the two lists [a, b, c] and [1, 2, 3],
# the function should return [a, 1, b, 2, c, 3].
def combelem (l1, l2):
    res = []
    for i in range(max(len(l1),len(l2))):
        res.append(l1[i])
        res.append(l2[i])
    return res

def combelemrec(l1,l2):
    if (l1 == l2 == []):
        return []
    else:
        return [l1[0],l2[0]] + combelemrec(l1[1:],l2[1:])


# Problem 3 Write a function that computes the list of the first 100
# Fibonacci numbers. By definition, the first two numbers in the
# Fibonacci sequence are 0 and 1, and each subsequent number is the
# sum of the previous two. As an example, here are the first 10
# Fibonnaci numbers: 0, 1, 1, 2, 3, 5, 8, 13, 21, and 34.

def fibo100():
    res = [1, 1]
    while (len(res) < 100):
        res.append(res[-1] + res[-2])
    return res

# Problem 5

# Write a program that outputs all possibilities to put + or - or
# nothing between the numbers 1, 2, ..., 9 (in this order) such that the
# result is always 100. For example: 1 + 2 + 34 – 5 + 67 – 8 + 9 = 100.


