import sys

def init_files():
    if len(sys.argv) < 2: sys.argv.append(input("Day: "))
    open(f"inputs/input {sys.argv[1]}.txt", "w").write("")
    open(f"inputs/test input {sys.argv[1]}.txt", "w").write("")
    open(f"day{sys.argv[1]}pt1.py", "w").write(template := file_template(sys.argv[1]))
    open(f"day{sys.argv[1]}pt2.py", "w").write(template)

def file_template(day):
    return f"""from aoc_tools import aoc_input

day, is_test, total = {day}, False, 0

for line in aoc_input(day, is_test):
    break
print(total)
"""

if __name__ == "__main__":
    init_files()
    

def aoc_input(day: int, is_test: bool):
    return open(f"inputs/{'' if not is_test else 'test '}input {str(day)}.txt").read().split("\n")