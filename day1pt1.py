def is_integer(x):
    try:
        int(x)
        return True
    except ValueError:
        return False

with open('inputs/input 1.txt', 'r') as file:
    day1 = file.read().split('\n')
    total = 0
    for index, line in enumerate(day1):
        numbers = list(filter(is_integer , list(line)))
        first_and_last = numbers[0] + numbers[len(numbers)-1]
        total += int(first_and_last)
    print(total)


