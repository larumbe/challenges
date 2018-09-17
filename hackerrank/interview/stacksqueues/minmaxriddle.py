# https://www.hackerrank.com/challenges/min-max-riddle/problem?h_l=interview&playlist_slugs%5B%5D%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D%5B%5D=stacks-queues

def riddle(arr):
    maxval = []
    for l in range(1, len(arr)+1):
        cw = []                 # currentwindow
        for i in range(len(arr)-l+1):
            cw.append(min(arr[i:i+l]))
        maxval.append(max(cw))

    return maxval
