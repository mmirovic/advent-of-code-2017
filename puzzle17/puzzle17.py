#!/Users/mmirovic/venv/bin/python3
# Advent of code 2017 by mmirovic

def part1(data):

    l = [0]
    i = 0

    for el in range(1, 2018):

        i = (i + data) % len(l)
        l = l[:i+1] + [el] + l[i+1:]
        i += 1

    return l[i+1]


def part2(data):

    # pre-allocate memory
    iter = 50000000 + 1
    l = [0] * iter
    size = 1
    i = 0

    # we do not have to move the data around, just add new values
    for el in range(1, iter):

        i = (i + data) % size
        l[i+1] = el

        size += 1
        i += 1

    return l[1]

def part2b(data):

    iter = 50000000 + 1
    v = None
    size = 1
    i = 0

    # we do not have to move the data around, just record value at pos 1
    for el in range(1, iter):

        i = (i + data) % size

        if i == 0:
            v = el

        size += 1
        i += 1

    return v


if __name__ == '__main__':

    print ('Result for part 1 is:', part1(304))
    print ('Result for part 2 is:', part2b(304))
