#!/Users/mmirovic/venv/bin/python3
# Advent of code 2017 by mmirovic

def parse(fname):
    r = []
    f = open(fname, 'r')
    for l in f:
        r += [map(int, l.split())]

    return r


def part1(data):

    return 0


def part2(data):

    return 0




if __name__ == '__main__':
    data = parse('input')
    #print (data)
    #print ('Result for part 1 is:', part1(data))
    #print ('Result for part 2 is:', part2(data))
