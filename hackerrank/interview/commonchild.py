# longest common subsequence !

def commonChild(s1, s2):
    c = []
    
    i = 0
    while (i < len(s1)):
        br = False 
        j = 0
        while (j < len(s2)):
            if (s1[i] == s2[j]):
                # s2.replace(s2[j], ' ', 1)
                s2 = s2[:j] + ' ' + s2[j+1:]
                br = True
                break
            j += 1
        if (br == True):
            c.append((s1[i], i, j))
        i += 1

    # find the longest increasing subsequence in c
    if (len(c) == 0):
        return 0

    print(c)
    
    longest = 1
    for i in range(len(c)-1):
        x = i
        y = i+1
        cnt = 1
        while (y < len(c)):
            if ((c[x][1] < c[y][1]) and (c[x][2] < c[y][2])):
                cnt += 1
                x += 1
                y += 1
            else:
                break
        if cnt > longest:
            longest = cnt
            
    return longest
