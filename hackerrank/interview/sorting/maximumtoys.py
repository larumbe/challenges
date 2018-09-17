def maximumToys(prices, k):
    srpr = sorted(prices)       # sorted prices
    i, toys = 0, 0
    accum = 0
    
    for p in srpr:
        if ((p > k) or (p + accum > k)):
            return toys
        else :
            accum += p
            toys += 1
    return toys

