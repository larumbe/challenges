# https://www.reddit.com/r/dailyprogrammer/comments/759fha/20171009_challenge_335_easy_consecutive_distance/

# Consecutive distance rating



ss = ["31 63 53 56 96 62 73 25 54 55 64",
      "77 39 35 38 41 42 76 73 40 31 10",
      "30 63 57 87 37 31 58 83 34 76 38",
      "18 62 55 92 88 57 90 10 11 96 12",
      "26 8 7 25 52 17 45 64 11 35 12",
      "89 57 21 55 56 81 54 100 22 62 50"]

def cdr(seq):
    return sum([seq.index(i+1)-seq.index(i) for i in seq if ((i+1) in seq and (seq.index(i+1) > seq.index(i)))])

def main():
    for s in ss: print(cdr([int(i) for i in s.split()]))
