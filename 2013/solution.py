
def read_file(filename):
    with open(filename, 'r') as file:
        lines = []
        for line in file:
            lines.append(line.strip())
    return lines


def validate_string(string):
    for i in range(len(string)-1):
        if string[i] > string[i+1]:
            return False
    return True
    
def task_one():
    lines = read_file('dane.txt')
    counter = 0
    for line in lines:
        if line[0] == line[-1]:
            counter += 1
    return counter

def task_two():
    lines = read_file('dane.txt')
    decimal_numbers = []
    counter = 0
    for line in lines:
        decimal_numbers.append(str(int(line, 8)))
    
    for number in decimal_numbers:
        if number[0] == number[-1]:
            counter += 1

    return counter


def task_three():
    lines = read_file('dane.txt')
    valid_numbers = []
    decimal_numbers = []
    min_index = 0
    max_index = 0
    for line in lines:
        if validate_string(line):
            valid_numbers.append(line)
    for number in valid_numbers:
        decimal_numbers.append(int(number, 8))

    min_index = decimal_numbers.index(min(decimal_numbers))
    max_index = decimal_numbers.index(max(decimal_numbers))

    return valid_numbers[min_index], valid_numbers[max_index], len(valid_numbers)


#print(task_one())
#print(task_two())
#print(task_three())