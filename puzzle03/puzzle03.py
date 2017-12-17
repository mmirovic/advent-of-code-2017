#!/usr/bin/python
# Advent of code 2017 by mmirovic

import math, numpy as np

	
def part1(n):

	spiral = int( math.ceil(math.sqrt(n)) )
	distance = spiral ** 2 - n - 1
	
	return "Result for part 1 is: " + str(distance)

def part2(matrix, value):

	pos = matrix.shape
	pos = (pos[0]/2,pos[1]/2)
	
	direction = 0 # facing east

	matrix[pos] = 1

	while ( matrix[pos] <= value ):

		pos = trig_move(pos, direction)

		matrix[pos] = matrix[pos[0]-1:pos[0]+2,pos[1]-1:pos[1]+2].sum()

		# direction change?
		if ( matrix[trig_move(pos,direction-math.pi/2)] == 0) :
			direction += -math.pi/2

	return "Result for part 2 is: " + str(matrix[pos])


def trig_move(pos, direction):

	return ( pos[0] + int(round(math.sin(direction))) , pos[1] + int(round(math.cos(direction))) )



if __name__ == '__main__':


#	value = 800
#	matrix = np.zeros((10,10), dtype=np.int)

	value = 289326
	matrix = np.zeros((30,30), dtype=np.int)

	
	print part1(value)
	print part2(matrix, value)



