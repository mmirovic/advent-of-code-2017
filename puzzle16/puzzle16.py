#!/Users/mmirovic/venv/bin/python3
# Advent of code 2017 by mmirovic

def parse(fname):
    r = []
    r = open(fname, 'r').read().strip().split(',')

    return r


def part1(data, g):

    for el in data:

        # x3/15
        if el[0] == 'x':
            d = el.index('/')
            t = g[int(el[1:d])]
            g[int(el[1:d])] = g[int(el[d+1:])]
            g[int(el[d+1:])] = t

        # pc/l
        elif el[0] == 'p':
            e1 = g.index(el[1])
            e2 = g.index(el[3])
            t = g[e1]
            g[e1] = g[e2]
            g[e2] = t

        # s2
        else:
            s = int(el[1:])
            g = g[-s:] + g[:-s]

    return g


def part2(data, g):

    s = g.copy()

    # search for the first repetition of the original string
    g = part1(data, g)
    i = 1
    while (''.join(g) != ''.join(s)):
        g = part1(data,g)
        i += 1

    for c in range(1000000000 % i):
        g = part1(data, g)

    return g

if __name__ == '__main__':
    data = parse('input')
    #print (data)

    g = []
    for i in range(16):
        g += [chr(ord('a')+i)]

    print ('Result for part 1 is:', ''.join(part1(data,list(g))))
    print ('Result for part 2 is:', ''.join(part2(data,list(g))))
