from typing import List, Set

class Card:

    def __init__(self, line: str) -> None:
        self.game = re.match(r"Card\s+(\d+):", line).groups()[0]
        line = re.sub(r"Card\s+\d+: ", "", line)
        self.winning_numbers = set(re.findall(r'\d+', line.split(" | ")[0]))
        self.chosen_numbers = set(re.findall(r'\d+', line.split(" | ")[1]))
        
    @property
    def union(self) -> Set[int]:
        return self.winning_numbers & self.chosen_numbers

    @property
    def score(self) -> int:
        return 2**(len(self.union) - 1) if len(self.union) > 0 else 0



with open('inputs/test input 4.txt', 'r') as file:
    inp: List[str] = file.read().split('\n')
    print(sum([Card(line).score for line in inp]))