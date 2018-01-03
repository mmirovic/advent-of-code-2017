#!/Users/mmirovic/venv/bin/python3
# Advent of code 2017 by mmirovic

def parse(fname):
    r = []
    f = open(fname, 'r')
    for l in f:
        r += [l]

    return r


def part1(data):

    i = 0
    d = {}

    while i < len(data):

        if 'Begin in state' in data[i]:
            s = data[i].strip('.\n').split()[3]

        if 'Perform a diagnostic checksum' in data[i]:
            r = int(data[i].split()[5])

        if 'In state' in data [i]:
            n = data[i].strip(':\n').split()[2]
            v = []

            i += 2
            v += [[int(data[i].strip('.\n').split()[4]), 1 if data[i+1].strip('.\n').split()[6] == 'right' else -1, data[i+2].strip('.\n').split()[4]],
                [int(data[i+4].strip('.\n').split()[4]), 1 if data[i+5].strip('.\n').split()[6] == 'right' else -1, data[i+6].strip('.\n').split()[4]]]

            d[n] = v

        i += 1

    t = [0] * 100001
    p = len(t) //2

    for _ in range(r):
        if t[p] == 0:
            t[p] = d[s][0][0]
            p += d[s][0][1]
            s = d[s][0][2]
        else:
            t[p] = d[s][1][0]
            p += d[s][1][1]
            s = d[s][1][2]

    return sum(t)


if __name__ == '__main__':
    data = parse('input')
    #print (data)

    print ('Result for part 1 is:', part1(data))
