from aoc_tools import aoc_input
from re import findall, split as split_regex

cards = [
    [findall("\d+", chars) for chars in split_regex(": | \| ", lines)][1:]
    for lines in aoc_input(day=4, is_test=False)
]

n_matches = [len(set(c[0]) & set(c[1])) for c in cards]
points = [2 ** (n - 1) if n > 0 else n for n in n_matches]

print(sum(points))