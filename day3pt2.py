from functools import reduce
from typing import List, Tuple

def is_digit(n):
    try: 
        int(n)
        return True
    except:
        return False
    
def number_positions(input: List[str]) -> Tuple[List[int], List[List[int]]]:
    numbers = []
    positions = []
    for rowIndex, line in enumerate(input):
        num = ''
        starting = -1
        for i in range(len(line)):
            if is_digit(line[i]):
                num += line[i]
                if starting == -1:
                    starting = i
                if i == len(line) - 1:
                    # print(f"{starting}:{i}, {rowIndex}; Number is {num}")
                    numbers.append(num)
                    positions.append([[i, rowIndex] for i in range(starting, i + 1)])
                    num = ''
                    starting = -1
            elif num != '': 
                if starting != -1:
                    # print(f"{starting}:{i - 1}, {rowIndex}; Number is {num}")
                    numbers.append(num)
                    positions.append([[i, rowIndex] for i in range(starting, i)])
                num = ''
                starting = -1
    return numbers, positions


def star_positions(input):
    positions = []
    for rowIndex, row in enumerate(input): 
        for itemIndex, item in enumerate(row):
            if item == '*':
                positions.append([itemIndex, rowIndex])
    return positions

def bounding_rectangle(positions):
    # , num, stars, debug
    # print(possible_number_positions, end=' ')
    possible_number_positions = positions
    index_before = possible_number_positions[0][0] - 1
    index_after = possible_number_positions[len(possible_number_positions) - 1][0] + 1
    row = possible_number_positions[0][1]
    # print(index_before, index_after, end=' ')
    # print(f"Row: {row}")

    current_row = [[index_before, row]] + possible_number_positions + [[index_after, row]]
    previous_row = list(map(lambda r: [r[0], r[1] -1], current_row))
    next_row = list(map(lambda r: [r[0], r[1] + 1], current_row))

    # rectangles_has_stars = any(list(map(lambda pos: pos in stars, reduce(lambda z, y :z + y, rectangle_rows))))

    # if debug and rectangles_has_stars:

    return previous_row + current_row + next_row

def make_rectanlge_matrix(positions: List[List[int]]) -> List[List[List[int]]]:   
    n = int(len(positions) / 3)
    return [positions[:n], positions[n:n*2], positions[n*2:]]

with open('inputs/input 3.txt', 'r') as file:
    day3: List[str] = file.read().split('\n')

    stars = star_positions(day3)
    numbers, positions = number_positions(day3)
    rectangles = list(map(lambda p: bounding_rectangle(p), positions))

    index_of_stars_with_2_numbers = []

    total = 0
    for s in stars:
        nums_to_multiply = []
        full_bounding_box = []
        for index, r in enumerate(rectangles):
            if s in r:
                nums_to_multiply.append(int(numbers[index]))
                if(len(nums_to_multiply) == 2):
                    total += nums_to_multiply[0] * nums_to_multiply[1]
                    index_of_stars_with_2_numbers.append(index)

    for rowIndex, line in enumerate(day3):
        for itemIndex, item in enumerate(line):
            current_position = [itemIndex, rowIndex]
            if current_position in stars:
                print('*', end='')
            elif is_digit(item):
                print(item, end='')
            else: print('.', end='')
        print()

    print(total)
