def commonChild(s1, s2):
    c = []
    i = 0

    while (i < len(s1)):
        br = False 
        j = 0
        while (j < len(s2)):
            if (s1[i] == s2[j]):
                s2 = s2[:j]+s2[j+1:]
                br = True
                break
            j += 1
        if (br == True):
            c.append(s1[i])
        i += 1

    print(c)
    return len(c)
