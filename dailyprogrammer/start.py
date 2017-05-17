
# https://www.reddit.com/r/dailyprogrammer/comments/69y21t/20170508_challenge_314_easy_concatenated_integers/
# http://www.shiftedup.com/2015/05/07/five-programming-problems-every-software-engineer-should-be-able-to-solve-in-less-than-1-hour

import functools


def sortnum(a,b):
    # define a sorting function taking  digits into account
    
    

def longestvalue(l):
    result = ''
    while (len(l) > 0):
        n = max([str(x) for x in l])
        # how can you pass the sorting function to max?
        del l[l.index(int(n))]
        result += n
    return int(result)
        
        


# l = [53, 254, 2634]

# max([str(x) for x in l])

# n = max([str(x) for x in l])

# l.index(53)

# del l[l.index(53)]


    

    





    

