# https://www.hackerrank.com/challenges/sherlock-and-anagrams/problem?h_l=interview&playlist_slugs%5B%5D%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D%5B%5D=dictionaries-hashmaps

def sherlockAnagrams(s):
    count = 0
    for l in range(1, len(s)+1):
        for i in range(len(s)):
            if (i+l > len(s)):
                break
            rest = s[i+1:]
            print("{} -- {}".format(s[i:i+l], rest))
            while (s[i:i+l][::-1] in rest):
                print("MATCH: {} : {}".format(s[i:i+l], rest))
                count += 1
                rest = rest[rest.index(s[i:i+l][::-1])+1:]
    return count
