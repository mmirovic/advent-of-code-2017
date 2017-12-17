#!/usr/bin/python
# Advent of code 2017 by mmirovic

def parse(fname):
    r = []
    f = open(fname, 'r')
    for l in f:
        r += [l.split()]

    return r


def part1(array):
    r = 0
    for row in array:
        if len(row) == len(set(row)):
            r += 1

    return "Result for part 1 is: " + str(r)


def part2(array):
    r = 0
    for row in array:
        # sort letters in passphrase words
        row_sort = [''.join(sorted(el)) for el in row]
        if len(row_sort) == len(set(row_sort)):
            r += 1

    return "Result for part 2 is: " + str(r)


if __name__ == '__main__':
    spreadsheet = parse('input')
    print part1(spreadsheet)
    print part2(spreadsheet)
