def read_file(filename):
    with open(filename, 'r') as file:
        lines = []
        for line in file:
            sublines = []
            for subline in line.split():
                sublines.append(int(subline))
            lines.append(sublines)

        return lines


def get_contrast(x, y):
    return abs(x - y)



def task_one():
    lines = read_file('przyklad.txt')
    the_lightest = 0
    the_darkest = 0

    for line in lines:
        if max(line) > the_lightest:
            the_lightest = max(line)
        if min(line) < the_darkest:
            the_darkest = min(line)
    
    return f"najjasniejszy: {the_lightest}, najciemniejszy: {the_darkest}"


def task_two():
    lines = read_file('przyklad.txt')
    lowest_count_to_delete = 0

    for line in lines:
        for i in range(320):
            if line[i] != line[319-i]:
                lowest_count_to_delete += 1
                break
    return f"najmniejsza liczba usunietych pikseli: {lowest_count_to_delete}"

def task_three():
    lines = read_file('przyklad.txt')
    contrast_pixels = 0

    for line in lines:
        for i in range(319):
            if get_contrast(line[i], line[i+1]) > 128:
                contrast_pixels += 1

    for i in range(199):
        for j in range(319):
            if get_contrast(lines[i][j], lines[i+1][j]) > 128:
                contrast_pixels += 1

    return f"liczba pikseli o duzym kontrascie: {contrast_pixels}"

print(task_three())