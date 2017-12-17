# Advent of code 2017 by mmirovic

def parse(fname):
    r = []
    f = open(fname, 'r').read()
    r = list(map(int, f.strip().split('	')))

    return r


def part12(array):

    List = []
    Step = 0

    while ( array not in List ):

        List += [array[:]]

        Max = max(array)
        Pos = array.index(Max)
        Len = len(array)

        Dist = [Max // Len] * Len
        Dist2 = [1] * (Max % Len) + [0] * (Len - Max % Len)

        Dist3 = [x+y for x,y in zip(Dist,Dist2)]
        Dist3 = rotate(Dist3,Pos+1)

        array[Pos] = 0
        array = [x+y for x,y in zip(array,Dist3)]

        Step += 1

    return Step, len(List) - List.index(array)

def rotate(array,pos):

    # function rotates left, we need rotation to the right
    pos = len(array) - pos

    return array[pos:] + array[:pos]


if __name__ == '__main__':

    data = parse('input')
    # data = [0, 2, 7, 0]

    print ("Results for part 1 and 2 are: ", part12(data))
