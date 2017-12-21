#!/Users/mmirovic/venv/bin/python3
# Advent of code 2017 by mmirovic

import math

def parse(fname):
    r = []
    f = open(fname, 'r')
    for l in f:
        r += [list(l)]

    return r


def part12(data):

    txt = ''
    d = math.pi / 2
    p = [0,data[0].index('|')]
    s = 0

    while data[p[0]][p[1]] != ' ':

        # if it's a character A-Z
        chr = data[p[0]][p[1]]
        if  ord(chr) >= 65 and ord(chr) <= 90 :
            txt += chr

        # left or right turn
        if data[p[0]][p[1]] == '+':
            if data[p[0] + round(math.sin(d+math.pi/2)) ][p[1] + round(math.cos(d+math.pi/2)) ] != ' ':
                d += math.pi/2
            else:
                d += -math.pi/2

        p = [p[0] + round(math.sin(d)), p[1] + round(math.cos(d)) ]
        s +=1

    return txt, s


if __name__ == '__main__':
    data = parse('input')

    print ('Results for part 1 and 2 are:', part12(data))
