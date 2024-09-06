def is_integer(x):
    try:
        int(x)
        return True
    except ValueError:
        return False

# With recursion, find and replace
# remove_nums deletes the word if number is found so twone1fhiwef will become 2ne1fhiwef

# def remove_nums(line):
#     letters_to_numbers = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
#     for i in range(len(line)):
#         for index, word in enumerate(letters_to_numbers):
#             if line[i: i + len(word)] == word:
#                 return remove_nums(line[:i] + str(index+1) + line[i + len(word):])
#     return line


# Without recursion, find and count all occurences without replace
# get_num accepts the word if number is found so twone1fhiwef will become 211fhiwef

def get_nums(line):
    letters_to_numbers = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    nums = ''
    for i in range(len(line)):
        try:
            nums += str(int(line[i]))
        except:
            pass
        for index, word in enumerate(letters_to_numbers):
            if line[i: i + len(word)] == word:
                nums += str(index+1)
    return nums

with open('inputs/input 1.txt', 'r') as file:
    day1 = file.read().split('\n')
    
    total = 0
    for index, line in enumerate(day1):
        print(line, end=' ')
        line = get_nums(line)
        print(line, end=' ')
        numbers = list(filter(is_integer , list(line)))
        first_and_last = 0
        if len(numbers) > 0:
            first_and_last = numbers[0] + numbers[len(numbers)-1]
            print(first_and_last)
        total += int(first_and_last)
    print(total)


