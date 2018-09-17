def checkMagazine(magazine, note):
    # build dictionary first
    d = dict()
    for w in magazine:
        if d.get(w) is None:
            d[w] = 1
        else:
            d[w] += 1
    
    for word in note:
        f = d.get(word)
        if (f is None or f == 0):
            print("No")
            return
        else:
            d[word] -= 1
        
    print("Yes")
    return
        
    
