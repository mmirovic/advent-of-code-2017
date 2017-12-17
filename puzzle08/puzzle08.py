#!/Users/mmirovic/venv/bin/python3
# Advent of code 2017 by mmirovic

from collections import defaultdict

def parse(fname):
    r = []
    f = open(fname, 'r')
    for l in f:
        l = l.split()
        l[2] = int(l[2])
        l[6] = int(l[6])
        r += [l]

    return r

def part12(input):

    # dictionary which accepts keys which are not present
    regs = defaultdict(int)
    m = 0

    ops = {"!=": (lambda x, y: x != y),
           "==": (lambda x, y: x == y),
           '<':  (lambda x, y: x < y),
           '>':  (lambda x, y: x > y),
           '>=': (lambda x, y: x >= y),
           '<=': (lambda x, y: x <= y),
           'inc':(lambda x, y: x + y),
           'dec':(lambda x, y: x - y)}

    for l in input:
        if ops[l[5]](regs[l[4]],l[6]):
            regs[l[0]] = ops[l[1]](regs[l[0]],l[2])
            m = max(regs[l[0]],m)

    return max(regs.values()), m

if __name__ == '__main__':
    data = parse('input')
    print ('Results for part 1 and 2 are:', part12(data))
