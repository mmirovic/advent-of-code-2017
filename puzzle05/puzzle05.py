#!/usr/bin/python
# Advent of code 2017 by mmirovic

def parse():
    fname = 'input'

    r = []
    f = open(fname, 'r')

    r = [int(el) for el in f]

    return r


def puzzle(array, part=1):

    pos = 0
    steps = 0

    while (pos >= 0 and pos < len(array)):
        pos_old = pos
        pos += array[pos]

        if part == 1:
            array[pos_old] += 1
        else:
            array[pos_old] += -1 if array[pos_old] >= 3 else 1

        steps += 1

    return "Result for part " + str(part) + " is: " + str(steps)


if __name__ == '__main__':
    data = parse()
    # data = [0, 3, 0, 1, -3]

    # we do not want to change the list
    print puzzle(data[:])
    print puzzle(data[:], 2)
