#!/Users/mmirovic/venv/bin/python3
# Advent of code 2017 by mmirovic

def parse(fname):
    r = []
    f = open(fname, 'r')
    for l in f:
        r += [l.split()]

    return r

class Cpu:

    def __init__(self, a = 0):

        self.reg = { 'a': a }

        for r in range(ord('b'), ord('h')+1):
            self.reg[chr(r)] = 0

        self.pc = 0
        self.c = 0

    def ins(self, i):


        # convert operands to values
        try:
            o1 = int(i[1])
        except:
            o1 = self.reg[i[1]]

        try:
            o2 = int(i[2])
        except:
            o2 = self.reg[i[2]]

        if i[0] == 'set':
            self.reg[i[1]] = o2

        if i[0] == 'sub':
            self.reg[i[1]] -= o2

        if i[0] == 'mul':
            self.reg[i[1]] *= o2
            self.c += 1

        if i[0] == 'jnz' and o1 != 0:
            self.pc += o2
            return 0

        self.pc += 1
        return 0


def part1(data):

    cpu = Cpu()

    while cpu.pc < len(data):
        cpu.ins(data[cpu.pc])

    return cpu.c

def part2():

    b = 105700
    c = 122700
    h = 0

    for b in range(105700, 122700 + 1, 17):
        exit = False
        for d in range(2, b):
            if exit:
                break

            for e in range(2, b):
                if e * d > b:
                    break
                elif e * d == b:
                    h += 1
                    exit = True
                    #print (h, b, e, d)
                    break

    return h


if __name__ == '__main__':
    data = parse('input')
    #print (data)

    print ('Result for part 1 is:', part1(data))
    print ('Result for part 2 is:', part2())
