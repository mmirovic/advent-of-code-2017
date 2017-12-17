#!/Users/mmirovic/venv/bin/python3
# Advent of code 2017 by mmirovic

def parse(fname):

    r = {}
    rep = {'<->': '', ',': ''}

    f = open(fname, 'r')
    for l in f:
        l = replace(l, rep).split()
        r[int(l[0])] = list(map(int, l[1:]))

    return r

def replace(text, dic):
    for i, j in dic.items():
        text = text.replace(i, j)
    return text


def part1(data, i=0):

    v = [i]
    i = 0

    while (i<len(v)):
        for el in data[v[i]]:
            if el not in v:
                v += [el]
        i += 1

    return set(v)


def part2(data):

    p = set(range(2000))
    g = 0

    while (len(p)>0):
        p -= part1(data,p.pop())
        g += 1

    return g


if __name__ == '__main__':
    data = parse('input')
    #print (data)

    print ('Result for part 1 is:', len(part1(data)))
    print ('Result for part 2 is:', part2(data))
