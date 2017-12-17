#!/Users/mmirovic/venv/bin/python3
# Advent of code 2017 by mmirovic

def parse(fname):

    r = open(fname, 'r').read().strip()
    return list(r)

def part12(data):

    # replace char after '!' with '.'
    for i in range(len(data)):
        if data[i] == '!':
            data[i+1] = '.'

    # remove '<...>' parts
    n = 0
    while ('<' in data ):
        b = data.index('<')
        e = data.index('>') + 1
        n += e - b - 2 - data[b:e].count('!')*2
        data[b:e] = []

    # remove ','
    data = [c for c in data if c != ',']

    # calculate result
    r = 0
    v = 0
    for i in range(len(data)):
        if data[i] == '{':
            v += 1
        else:
            r += v
            v -= 1

    print ('Result for part 1 is:', r)
    print ('Result for part 2 is:', n)

    return

if __name__ == '__main__':
    
    data = parse('input')
    part12(data)
