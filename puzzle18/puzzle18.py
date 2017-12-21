#!/Users/mmirovic/venv/bin/python3
# Advent of code 2017 by mmirovic

def parse(fname):
    r = []
    f = open(fname, 'r')
    for l in f:
        r += [l.split()]

    return r

class Cpu:

    def __init__(self, p = 0):
        self.reg = {'p': p}
        self.pc = 0
        self.q = []
        self.c = 0

    def ins(self, i, cpu):

        # initialize to 0
        if i[1] not in self.reg:
            self.reg[i[1]] = 0

        if i[0] == 'snd':
            cpu.q += [self.reg[i[1]]]
            self.c += 1
            self.pc += 1
            return 0

        if i[0] == 'rcv':

            if len(self.q) > 0:
                self.reg[i[1]] = self.q.pop(0)
                self.pc += 1
                return 1
            else:
                return -1

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

        if i[0] == 'add':
            self.reg[i[1]] += o2

        if i[0] == 'mul':
            self.reg[i[1]] *= o2

        if i[0] == 'mod':
            self.reg[i[1]] %= o2

        if i[0] == 'jgz' and o1 > 0:
            self.pc += o2
            return 0

        self.pc += 1
        return 0


def part1(data):

    cpu = Cpu()

    while cpu.ins(data[cpu.pc], cpu) != 1:
        pass

    return cpu.q[-1]


def part2(data):

    cpu0 = Cpu()
    cpu1 = Cpu(1)

    while cpu0.ins(data[cpu0.pc], cpu1) != -1 or cpu1.ins(data[cpu1.pc], cpu0) != -1:
        pass

    return cpu1.c


if __name__ == '__main__':
    data = parse('input')

    print ('Result for part 1 is:', part1(data))
    print ('Result for part 2 is:', part2(data))
