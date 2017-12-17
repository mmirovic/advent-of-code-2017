#!/Users/mmirovic/venv/bin/python3
# Advent of code 2017 by mmirovic

#import sys
#sys.path.append('../puzzle10')
#from puzzle10 import part2 as knot

from puzzle10.puzzle10 import part2 as knot
import numpy as np

def bitcount(n):
    count = 0
    while n > 0:
        count = count + 1
        n = n & (n-1)
    return count


def part1(data):

    c = 0
    m = np.zeros((128, 128), dtype=np.int)

    for i in range(128):
        s = data + '-' + str(i)
        d = int(knot( list(map(ord,s)) ),16)
        c += bitcount(d)

        b = '{0:0128b}'.format(d)
        m[i,] = [-1 if e=='1' else 0 for e in b]

    return c, m


def part2(data):

    g = 0

    for y in range(128):
        for x in range(128):
            if data[y,x] == -1:
                g += 1
                populate(data,g,(y,x))

    return g


def populate (data, g, l):

    v = [l]

    while(len(v)) > 0:

        data[v[0]] = g
        c = v.pop(0)

        # numpy accepts negative indexes, we will not use them since they wrap the matrix
        for n in { (max(0,c[0]-1), c[1]), (c[0]+1, c[1]), (c[0], max(0,c[1]-1)), (c[0], c[1]+1) }:
            try:
                if data[n] == -1:
                    v += [n]
            except:
                pass

    return


if __name__ == '__main__':

    #data = 'flqrgnkx' # test input
    data = 'jzgqcdpd'

    r, m = part1(data)
    print ('Result for part 1 is:', r)
    print ('Result for part 2 is:', part2(m))
