#!/Users/mmirovic/venv/bin/python3
# Advent of code 2017 by mmirovic

import numpy as np

def parse(fname):
    r = {}
    f = open(fname, 'r')
    for l in f:

        s = l.index('/')
        m1 = np.zeros((s, s), dtype=np.int)
        m2 = np.zeros((s+1, s+1), dtype=np.int)

        # example of transformation
        # ../.. => ..#/.#./...

        l = l.replace('.','0').replace('#','1').strip()
        l1 = l[:l.index(' => ')].split('/')
        l2 = l[l.index(' => ')+4:].split('/')

        for i in range(s):
            m1[i,] = list(map(int,list(l1[i])))

        for i in range(s+1):
            m2[i,] = list(map(int,list(l2[i])))

        # fill in search dictionary
        for i in range(4):
            r[hash(np.rot90(m1, i).tostring())] = m2
            r[hash(np.fliplr(np.rot90(m1, i)).tostring())] = m2

    return r


def part12(data):

    a = np.array ([[0,1,0], [0,0,1], [1,1,1]])
    part1 = 0

    for p in range(18):

        size = (np.shape(a)[0])
        i = size//2 if size%2 == 0 else size//3
        s = size//i

        r = []
        for x in range (i):
            for y in range (i):

                subm = a[y*s:s*(y+1), x*s:s*(x+1)]
                subm = data[hash(subm.tostring())]

                if  len(r) <= x:
                    r += [subm]
                else:
                    r[x] = np.concatenate((r[x], subm))

        a = r[0]
        for i in range(1,len(r)):
            a = np.concatenate((a, r[i]), axis=1)

        if p == 4:
            part1 = np.sum(a)

    return part1, np.sum(a)


if __name__ == '__main__':
    data = parse('input')
    #print (data)

    print ('Results for part 1 and 2 are:', part12(data))
