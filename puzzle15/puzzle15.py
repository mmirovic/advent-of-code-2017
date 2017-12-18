#!/Users/mmirovic/venv/bin/python3
# Advent of code 2017 by mmirovic

def parse(fname):
    r = []
    f = open(fname, 'r')
    for l in f:
        r += [int(l.split()[4])]

    return r


def part1(data):

    c = 0

    A = data[0]
    B = data[1]

    for i in range (40000000):
        A = (A * 16807) % 2147483647
        B = (B * 48271) % 2147483647
        #print (A,B)
        if A & 65535 == B & 65535:
            c += 1

    return c


def part2(data):

    c = 0

    A = data[0]
    B = data[1]

    for i in range (5000000):
        A = (A * 16807) % 2147483647
        B = (B * 48271) % 2147483647

        while A & 3 != 0:
            A = (A * 16807) % 2147483647
        while B & 7 != 0:
            B = (B * 48271) % 2147483647
        #print (A,B)
        if A & 65535 == B & 65535:
            c += 1

    return c


if __name__ == '__main__':

    #data = [65,8921] # test data
    data = parse('input')

    #print ('Result for part 1 is:', part1(data))
    print ('Result for part 2 is:', part2(data))
