# Advent of code 2017 by mmirovic


from collections import Counter


def parse(fname):
    r = []
    rep = {'(': '', ')': '', '->': '', ',': ''}

    f = open(fname, 'r')
    for l in f:
        l = replace(l, rep).split()
        l[1] = int(l[1])
        r += [l]
    return r


def replace(text, dic):
    for i, j in dic.iteritems():
        text = text.replace(i, j)
    return text

class Tree(object):
    "Generic tree node."

    def __init__(self, name):
        self.name = name
        self.value = None
        self.children = []

    def add_children(self, parent, value, l):

        if self.name == parent:
            for el in l:
                self.children.append(Tree(el))
            self.value = value
            return

        for child in self.children:
            child.add_children(parent, value, l)

    def add_value(self, name, value):

        if self.name == name:
            self.value = value
            return

        for child in self.children:
            child.add_value(name, value)

    def find_unbalanced(self):

        l = []
        for child in self.children:
            l += [[child.name, child.find_value(child.name)]]

        if len( Counter( value for name, value in l) ) > 1:
            print l

        for child in self.children:
            child.find_unbalanced()

    def find_value(self, name):

        if self.name == name:
            value = self.value
            for child in self.children:
                value += child.find_value(child.name)
            return value

        for child in self.children:
            child.find_value(name)

    def find_node_value(self, name):

        if self.name == name:
            return self.value

        for child in self.children:
            value = child.find_node_value(name)
            if value is not None:
                return value


def part1(array):
    # Root finder

    nodes = []

    for el in array:
        for el2 in el:
            if isinstance(el2, str):
                nodes += [el2]

    dic = Counter(nodes)

    for key, value in dic.iteritems():
        if value == 1 and key:
            return key


def part2(array):

    # create tree
    root = part1(array)
    t = Tree(root)

    # fill in the tree from the root
    names = [root]

    while len(array) > 0:

        l = find_and_remove(array, names.pop())

        if len(l) > 2:
            names += l[2:]
            t.add_children(l[0],l[1],l[2:])
        elif len(l) == 2:
            t.add_value(l[0], l[1])

    t.find_unbalanced()

def find_and_remove(array, name):
    for i in range(len(array)):
        if array[i][0] == name:
            r = array[i]
            array.pop(i)
            return r

    # in case element is already processed
    return []


if __name__ == '__main__':

    #data = parse('input_test')
    data = parse('input')

    # print data
    print ('Result for part 1 is:', part1(data))
    part2(data)
