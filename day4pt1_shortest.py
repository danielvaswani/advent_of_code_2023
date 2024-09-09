from re import findall as findr, split as splitr

points = [
    len(set(card[1]) & set(card[0]))  # Get union of our numbers in winning set
    for card in [  # For every card string, split lines on : and |, Get all digits
        [findr("\d+", char) for char in splitr(": | \| ", line)][1:]  # [0] is Card No.
        for line in open("inputs/input 4.txt", "r").read().split("\n")  # For every line
    ]
]  # To sum score, for each element score is 2 ^ (points - 1) as long as points arent 0
print(sum((2 ** (n - 1) if n > 0 else n) for n in points))
