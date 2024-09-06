from functools import reduce

def add_items(a, b):
    # Check if color already exists in the result
    for item in a:
        if item[1] == b[1]:
            item[0] = str(int(item[0]) + int(b[0]))  # Sum the numbers for the same color
            return a
    a.append(b)  # If color doesn't exist, append the new color
    return a

with open('inputs/test input 2.txt', 'r') as file:
    day2 = file.read().split('\n')
    for index, line in enumerate(day2):
        # print(line[5:line.index(':')])
        # print(index + 1)
        rounds = line[line.index(':') + 2:].split('; ')
        rounds = list(map(lambda r: r.split(', '), rounds))
        rounds = list(map(lambda x : list(map(lambda y: y.split(' '), x)), rounds))
        combined = reduce(lambda a, b: a+b, rounds)
        print(combined)
        totals = reduce(add_items, combined, [])
        print(totals)
        print()