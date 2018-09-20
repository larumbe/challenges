# https://www.hackerrank.com/challenges/poisonous-plants/problem?h_l=interview&playlist_slugs%5B%5D%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D%5B%5D=stacks-queues


def poisonousPlants(p):
    d = 1
    while True:
        c = [p[0]]
        deaths = 0
        for i in range(len(p)-1):
            if p[i+1] <= p[i]:
                c.append(p[i+1])
            else:
                deaths += 1
                print(c)
        if deaths is 0:
            break
        else:
            p = c
            d += 1
    return d-1
