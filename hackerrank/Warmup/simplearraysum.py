# Simple Array Sum

import sys

def simpleArraySum(n, ar):
    return sum(ar)

def main():
    n = int(input().strip())
    ar = list(map(int, input().strip().split(' ')))
    result = simpleArraySum(n, ar)
    print(result)
    
