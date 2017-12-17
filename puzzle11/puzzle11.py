#!/Users/mmirovic/venv/bin/python3
# Advent of code 2017 by mmirovic

def parse(fname):
    r = []
    f = open(fname, 'r').read()
    r = f.strip().split(',')

    return r


def part12(data):

    m = {
        'n':  [0,1,-1],
        'ne': [1,0,-1],
        'se': [1,-1,0],
        's':  [0,-1,1],
        'sw': [-1,0,1],
        'nw': [-1,1,0]
    }

    p = [0,0,0]
    md = 0

    for el in data:
        p = list(x+y for x,y in zip(p,m[el]))
        md = max(md, ( abs(p[0]) + abs(p[1]) + abs(p[2]) )//2)

    d = ( abs(p[0]) + abs(p[1]) + abs(p[2]) )//2

    return d, md


if __name__ == '__main__':
    data = parse('input')
    #print (data)
    r = part12(data)
    print ('Result for part 1 is:', r[0])
    print ('Result for part 2 is:', r[1])
