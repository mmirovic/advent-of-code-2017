#!/Users/mmirovic/venv/bin/python3
# Advent of code 2017 by mmirovic

from operator import add

def parse(fname):
    r = []
    f = open(fname, 'r')
    for l in f:

        # line example:
        # p=<-1027,-979,-188>, v=<7,60,66>, a=<9,1,-7>

        l = l.replace('p=<','').replace(' v=<','').replace(' a=<','').replace('>','').strip().split(',')
        l = list(map(int,l))

        r += [Particle(l[:3],l[3:6],l[6:])]

    return r


class Particle:

    def __init__ (self, p, v, a):

        self.p = p
        self.v = v
        self.a = a

        self.o = [self.p, self.v]

    def __str__(self):

        return ('pos: ' + str(self.p) + ' vel: ' + str(self.v) + ' acc: ' + str(self.a))

    def reset(self):

        self.p = self.o[0]
        self.v = self.o[1]

    def move(self):

        # increase v by a and then p by v
        self.v = list(map(add, self.v, self.a))
        self.p = list(map(add, self.p, self.v))

    def distance(self):

        # Manhattan distance
        return sum(map(abs,self.p))


def part1(data):

    for r in range(400):

        min = 0

        for i, p in enumerate(data):
            p.move()
            if p.distance() < data[min].distance():
                min = i

    return min


def part2(data):

    for repeat in range(40):

        # sort by position
        data = sorted(data, key=lambda p: p.p)

        # find all the elements to be removed
        r = []
        for i in range(len(data) - 1):
            if data[i].p == data[i + 1].p:
                r += [data[i], data[i+1]]

        # remove duplicates
        data = [el for el in data if el not in r]

        # move to new positions
        for p in data:
            p.move()

    return len(data)


if __name__ == '__main__':
    data = parse('input')

    print ('Result for part 1 is:', part1(data))

    # return particles to the original places
    for el in data:
        el.reset()

    print ('Result for part 2 is:', part2(data))
