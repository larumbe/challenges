# https://www.hackerrank.com/challenges/ctci-ice-cream-parlor/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=search

def whatFlavors(cost, money):
    for i in range(len(cost)):
        if (money-cost[i]) in cost[i+1:]:
            print("{} {}".format(i+1, cost[i+1:].index(money-cost[i])+2+i))
