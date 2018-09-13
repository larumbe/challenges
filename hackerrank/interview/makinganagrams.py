def makeAnagram(a, b):
    
    hist = [0] * (ord('z') - ord('a') + 1)

    # build histograms
    for i in range(len(a)):
        hist[ord(a[i])-ord('a')] += 1

    for i in range(len(b)):
        hist[ord(b[i])-ord('a')] -= 1

    return sum([abs(i) for i in hist])
