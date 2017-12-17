#!/usr/bin/python
# Advent of code 2017 by mmirovic

def parse(fname):

	r = []
	f = open(fname, 'r')
	for l in f:
		r += [ map(int, l.split()) ]

	return r
	
def part1(array):

	r = 0
	for row in array:
		r += max(row) - min(row)

	return "Result for part 1 is: " + str(r)

def part2(array):

	r = 0
	for row in array:
		r += find_divisible(row)			

	return "Result for part 2 is: " + str(r)

def find_divisible(row):

	# remove 0, remove duplicates, sorts list for simpler division
	row = (set(row))
	row.discard(0)
	row = sorted(list(row))
			
	while ( len(row)>1 ):
		n1 = row.pop()
		
		for n2 in row:	
			if n1%n2 == 0:
				return n1/n2

	return 0


if __name__ == '__main__':
	
	spreadsheet = parse('input')
	print part1(spreadsheet)
	print part2(spreadsheet)

