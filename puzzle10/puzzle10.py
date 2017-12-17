#!/Users/mmirovic/venv/bin/python3
# Advent of code 2017 by mmirovic

def parse(fname):
    r = []
    f = open(fname, 'r').read()
    l = list(map(int,f.strip().split(',')))

    return l

def parse2(fname):
    r = []
    f = open(fname, 'r').read()
    l = list(map(ord,f.strip()))

    return l


def part1(data, l = list(range(256)), i=0, s=0):

    for el in data:
        l = reverse (l,i,el)
        i = (i + el + s) % len(l)
        s += 1

    return l, i, s


def reverse(data, i, l):

    b = i
    e = i+l

    if e <= len(data):
        data = data[0:b] + list(reversed(data[b:e])) + data[e:]

    else:
        e = e % len(data)
        r = list(reversed(data[b:]+data[:e]))
        data = r[len(data)-i:] + data[e:b] + r[:len(data)-i]

    return data

def part2(data):

    data += [17, 31, 73, 47, 23]
    l = list(range(256))
    i = 0
    s = 0

    for c in range(64):
        l, i, s = part1(data,l,i,s)

    r = ''

    for i in range(16):
        x = 0
        for j in range(16):
            x ^= l[i*16+j]

        r += '%02x' % x

    return r


if __name__ == '__main__':
    data = parse('input')
    r = part1(data)
    print ('Result for part 1 is:', r[0][0]*r[0][1])

    data = parse2('input')
    print ('Result for part 2 is:', part2(data))
