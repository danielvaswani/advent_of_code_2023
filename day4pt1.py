import re
from functools import reduce
from aoc_tools import aoc_input

total = 0

for line in aoc_input(day=4, is_test=False):
    n_winning_numbers = len(
        reduce(
            lambda win_nums, our_nums: win_nums & our_nums,
            [
                set(txt.split(" "))
                for txt in " ".join(re.findall("\d+|\|", line.split(": ")[1])).split(
                    " | "
                )
            ],
        )
    )

    # print(line)
    total += 2 ** (n_winning_numbers - 1) if n_winning_numbers > 0 else 0
    # break

print(total)
