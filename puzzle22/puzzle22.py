#!/Users/mmirovic/venv/bin/python3
# Advent of code 2017 by mmirovic

import math, copy

def parse(fname):

    r = []
    f = open(fname, 'r')

    size = 400
    ln = len(f.readline())-1
    f.seek(0)

    for _ in range(size):
        r += [['.']*(2*size+ln)]

    for l in f:
        r += [['.']*size + list(l.strip()) + ['.']*size]

    for _ in range(size):
        r += [['.']*(2*size+ln)]

    return r


def part1(data):

    # we do not want to modify the list, keep it as is for the 2nd part
    data = copy.deepcopy(data)

    pos = [len(data[0])//2] * 2
    d = math.pi / 2
    inf = 0

    for _ in range(10000):

        # If the current node is infected, it turns to its right. Otherwise, it turns to its left.
        # If the current node is clean, it becomes infected. Otherwise, it becomes cleaned.

        if data[pos[0]][pos[1]] == '#':
            d += - math.pi / 2
            data[pos[0]][pos[1]] = '.'
        else:
            d += math.pi / 2
            data[pos[0]][pos[1]] = '#'
            inf += 1

        # The virus carrier moves forward one node in the direction it is facing.
        # we do '-sin' since our y axis is in opposite direction
        pos = [pos[0] - int(round(math.sin(d))), pos[1] + int(round(math.cos(d)))]

    return inf

def part2(data):

    pos = [len(data[0])//2] * 2
    d = math.pi / 2
    inf = 0

    # dictionary with the updates: next state, direction and infected counter
    s = {'.' : ['w', math.pi/2, 0],
         'w' : ['#', 0, 1],
         '#' : ['f', -math.pi/2, 0],
         'f' : ['.', math.pi, 0]}

    for _ in range(10000000):

        state =  data[pos[0]][pos[1]]

        # update matrix, direction and infected counter using the dict above
        data[pos[0]][pos[1]] = s[state][0]
        d += s[state][1]
        inf += s[state][2]

        # The virus carrier moves forward one node in the direction it is facing.
        # we do '-sin' since our y axis is in opposite direction
        pos = [pos[0] - int(round(math.sin(d))), pos[1] + int(round(math.cos(d)))]

    return inf


if __name__ == '__main__':
    data = parse('input')
    #print (data)
    print ('Result for part 1 is:', part1(data))
    print ('Result for part 2 is:', part2(data))
