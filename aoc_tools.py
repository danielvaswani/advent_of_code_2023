def aoc_input(day: int, is_test: bool):
    return open(f"inputs/{'' if not is_test else 'test '}input {str(day)}.txt").read().split("\n")