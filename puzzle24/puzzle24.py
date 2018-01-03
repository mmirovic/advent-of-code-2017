#!/Users/mmirovic/venv/bin/python3
# Advent of code 2017 by mmirovic

def parse(fname):
    r = []
    f = open(fname, 'r')
    for l in f:
        r += [list(map(int, l.split('/')))]

    return r


def part12(data):

    b = [[0]]
    p = [data]
    i = 0

    while i < len(b):

        # find matching next links
        l = []
        for el in p[i]:
            if b[i][-1] in el:
                l += [el]

        # add new chains to the list
        for el in l:
            if b[i][-1] == el[0]:
                b += [b[i] + el]
            else:
                b += [b[i] + el[::-1]]

            p += [[e for e in p[i] if e != el]]

        i += 1

    m = 0
    l = []
    ml = 0
    for el in b:
        m = max(sum(el), m)
        if len(el) > ml:
            ml = len(el)
            l = [el]
        if len(el) == ml:
            l += [el]

    m2 = 0
    for el in l:
        m2 = max(sum(el), m2)

    return m, m2


if __name__ == '__main__':
    data = parse('input')
    #print (data)

    print ('Result for parts 1 and 2 are:', part12(data))

