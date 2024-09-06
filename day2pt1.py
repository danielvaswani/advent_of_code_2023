from functools import reduce

def add_items(a, b):
    # Check if color already exists in the result
    for item in a:
        if item[1] == b[1]:
            item[0] = str(int(item[0]) + int(b[0]))  # Sum the numbers for the same color
            return a
    a.append(b)  # If color doesn't exist, append the new color
    return a

total = 0

with open('inputs/input 2.txt', 'r') as file:
    day2 = file.read().split('\n')
    for index, line in enumerate(day2, start=1):
        # print(line[5:line.index(':')])
        # print(index + 1)
        rounds = line[line.index(':') + 2:].split('; ')
        rounds = list(map(lambda r: r.split(', '), rounds))
        rounds = list(map(lambda x : list(map(lambda y: y.split(' '), x)), rounds))
        combined = reduce(lambda a, b: a+b, rounds)
        
        highest = [0,0,0]

        for cubes in combined:
            if cubes[1] == 'red':
                if int(cubes[0]) > int(highest[0]):
                    highest[0] = cubes[0]
            if cubes[1] == 'green':
                if int(cubes[0]) > int(highest[1]):
                    highest[1] = cubes[0]
            if cubes[1] == 'blue':
                if int(cubes[0]) > int(highest[2]):
                    highest[2] = cubes[0]
        
        # if int(highest[0]) <= 12 and int(highest[1]) <= 13 and int(highest[2]) <= 14:
        total += int(highest[0]) * int(highest[1]) * int(highest[2])

print(total)