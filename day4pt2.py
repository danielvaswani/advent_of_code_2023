from aoc_tools import aoc_input
from re import findall, split as split_regex

cards = [
    [findall("\d+", chars) for chars in split_regex(": | \| ", lines)][1:]
    for lines in aoc_input(day=4, is_test=True)
]

n_matches = [len(set(c[0]) & set(c[1])) for c in cards]

indexes_to_check = []

for index, card in enumerate(n_matches):
    for n in range(card):
        indexes_to_check.append(n+1+index)
        print(n+1+index+1, end=' ')
    if card != 0: print() 

for i in indexes_to_check:
    break