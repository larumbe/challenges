#  https://www.hackerrank.com/challenges/swap-nodes-algo/problem?h_l=interview&playlist_slugs%5B%5D%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D%5B%5D=search

import math

def swapNodesLevel(t, h):
    """swaps nodes at height h
    swaps the childre of all nodes at height h"""

    if (h == int(math.log2(len(t)+1)) - 1):
        return t
      
    sl = 1                 # swap length
    ns = pow(2,h)          # number of swaps
    for i in range(h+1, int(math.log2(len(t)+1))):
        k = (pow(2,i))-1               # skip        
        for j in range(ns):
            t[k+j*sl*2:k+j*sl*2+sl], t[k+j*sl*2+sl:k+j*sl*2+sl+sl] = t[k+j*sl*2+sl:k+j*sl*2+sl+sl], t[k+j*sl*2:k+j*sl*2+sl]
        sl = sl * 2
        
    return t

snl = swapNodesLevel

# is an iterative implementation of inorder possible?
# the tree is complete and leaf nodes are indicated by -1
def inOrder(t, s):
    """inorder travers starting at node index s"""
    if (t[s] == -1):
        return
    else:
        if ((s*2)+1 < len(t)):
            inOrder(t, (s*2)+1)
        print("{} ".format(t[s]), end='')
        if ((s*2)+2 < len(t)):
            inOrder(t, (s*2)+2)

    return
