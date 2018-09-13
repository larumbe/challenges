def generateSubstrings(s):
    sss = []

    for i in range(1, len(s)):
        j = 0
        while (j+i < len(s)+1):
            sss.append(s[j:j+i])
            j += 1
    sss.append(s)

    return sss


def substrCount(n, s):
    spalin = []

    for ss in generateSubstrings(s):
        if isSpecialPalindrome(ss):
            spalin.append(ss)
    return len(spalin)


def isSpecialPalindrome(s):

    if (len(s) == 1):
        return True
    if (len(s) % 2 == 0):
        if (s.count(s[0]) == len(s)):
            return True
        else:
            return False
    else:
        ns = s[:len(s)//2] + s[(len(s)//2)+1:]
        if (ns.count(ns[0]) == (len(ns))):
            return True
        else:
            return False
