def generateSubstrings(s):
    for l in range(1,len(s)):
        for i in range(len(s)):
            if (i+l > len(s)):
                break
            yield s[i:i+l]

def twoStrings(s1, s2):
    m = min(len(s1), len(s2))
    if (m == len(s1)):
        for ss in generateSubstrings(s1):
            if ss in s2:
                print("YES")
                return
        print("NO")
        return

    if (m == len(s2)):
        for ss in generateSubstrings(s2):
            if ss in s1:
                print("YES")
                return
        print("NO")
        return
