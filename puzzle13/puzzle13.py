#!/Users/mmirovic/venv/bin/python3
# Advent of code 2017 by mmirovic

def parse(fname):
    r = {}
    f = open(fname, 'r')
    for l in f:
        l = list(map(int,l.replace(':','').split()))
        r[l[0]] = l[1]

    return r


def part1(data):

    s = 0

    for t in range(max(data)+1):
        if t in data:
            s += t*data[t] if t%((data[t]-1)*2) == 0 else 0

    return s

def part2(data):

    w = 0

    while True:

        for t in range(max(data)+1):

            if (t in data) and (t+w)%((data[t]-1)*2) == 0:
                w += 1
                break

        if t == max(data):
            return w

if __name__ == '__main__':
    data = parse('input')
    #print (data)
    print ('Result for part 1 is:', part1(data))
    print ('Result for part 2 is:', part2(data))
