# https://www.hackerrank.com/challenges/crossword-puzzle/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=recursion-backtracking

# this is obviously a backtracking problem

def crosswordPuzzle(crossword, words):
    words = words.split(';')

    gaps = findGaps()
