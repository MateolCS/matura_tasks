def read_file(filename):
    with open(filename, 'r') as file:
        lines = []

        for line in file:
            lines.append(line.strip())

    return lines


def get_letter_distance(letter1, letter2):
    return abs(ord(letter1) - ord(letter2))


def validate_word(word):
    for i in range(len(word) - 1):
        if get_letter_distance(word[i], word[i + 1]) > 10:
            return False
    return True

def task_one():
    lines = read_file('przyklad.txt')
    word = ''

    for i in range(39, len(lines), 40):
        word += lines[i][9]

    return word

def task_two():
    lines = read_file('przyklad.txt')
    selected_word = ''
    unique_letters_count = 0
    word_index = 0

    for i,  line in enumerate(lines):
        if len(set(line)) > unique_letters_count:
            unique_letters_count = len(set(line))
            selected_word = line
            word_index = i
    
    return  f"Word: {selected_word},unique letters: {unique_letters_count}"




def task_three():
    lines = read_file('przyklad.txt')
    selected_words = []

    for line in lines:
        if validate_word(line):
            selected_words.append(line)
    return selected_words       


#print(task_one())
#print(task_two())

print(task_three())