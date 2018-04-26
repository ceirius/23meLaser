#!/usr/bin/env python
# Validation scientist coding challenge, recd: 23 April 2018
# LASER MAZE - Shreyas Krishnan


import sys
import argparse

class Maze(object):
	def __init__(self, maze, x, y, output="laserout.txt"):
		self.maze = maze
		self.x = x
		self.y = y
		self.output = output

	"""
	Four similar functions are defined labeled north, south east and west. The first call to any one of these functions is from within main(). 
	If next coordinate is not within array the program ends. The next position in the grid (depending on the direction) is evaluated. If that position is empty or within the grid, the step counter and coordinate are adjusted accordingly. Immediately the new position is evaluated for mirror type, and coordinates and counters are passed to the respective function. If an edge cell is reached or if counter reached a defined limit (20), then end() is called.
	"""
	def west(self, direction, start_x, start_y, step_count):
		if start_x - 1 >= 0:																
			while self.maze[start_x - 1][start_y] == 0 or start_x - 1 >= 0:					
				start_x -= 1
				step_count += 1																
				if self.maze[start_x][start_y] == "\\":
					direction = 'N'
					self.north(direction, start_x, start_y, step_count)	
				elif self.maze[start_x][start_y] == "/":
					direction = 'S'
					self.south(direction, start_x, start_y, step_count)		
				elif start_x - 1 < 0 or step_count == 20: 	
					self.end(start_x, start_y, step_count)
		elif start_x - 1 < 0 or step_count == 20: 	
			self.end(start_x, start_y, step_count)				

	def east(self, direction, start_x, start_y, step_count):
		if start_x + 1 < self.x:														
			while self.maze[start_x + 1][start_y] == 0 or start_x + 1 < self.x:			
				start_x += 1
				step_count += 1															
				if self.maze[start_x][start_y] == '\\':
					direction = 'S'
					self.south(direction, start_x, start_y, step_count)				
				elif self.maze[start_x][start_y] == '/':
					direction = 'N'
					self.north(direction, start_x, start_y, step_count)		
				elif start_x + 1 > self.x - 1 or step_count == 20: 	
					self.end(start_x, start_y, step_count)	
		elif start_x + 1 > self.x - 1 or step_count == 20: 	
			self.end(start_x, start_y, step_count)
				
	def north(self, direction, start_x, start_y, step_count):

		if start_y + 1 < self.y:														
			while self.maze[start_x][start_y + 1] == 0 or start_y + 1 < self.y:			
				start_y += 1
				step_count += 1															
				if self.maze[start_x][start_y] == '\\':
					direction = 'W'
					self.west(direction, start_x, start_y, step_count)				
				elif self.maze[start_x][start_y] == '/':
					direction = 'E'
					self.east(direction, start_x, start_y, step_count)		
				elif start_y + 1 >= self.y-1 or step_count == 20: 	
					self.end(start_x, start_y, step_count)
		elif start_y + 1 >= self.y-1 or step_count == 20: 	
			self.end(start_x, start_y, step_count)
							
	def south(self, direction, start_x, start_y, step_count):
		if start_y - 1 >= 0:																
			while self.maze[start_x][start_y - 1] == 0 or start_y - 1 >= 0:					
				start_y -= 1
				step_count += 1																
				if self.maze[start_x][start_y] == '\\':
					direction = 'E'
					self.east(direction, start_x, start_y, step_count)				
				elif self.maze[start_x][start_y] == '/':
					direction = 'W'
					self.west(direction, start_x, start_y, step_count)		
				elif start_y - 1 < 0 or step_count == 20: 	
					self.end(start_x, start_y, step_count)
		elif start_y - 1 < 0 or step_count == 20: 	
			self.end(start_x, start_y, step_count)

		"""
		end() is called and outputs counters to output file. File is closed.
		An exit() is forced to prevent the end of loops from reverting to their 
		initiation points and erroneously running counters.
		"""
		
	def end(self, start_x, start_y, step_count):
		fileout = open(self.output, 'w')
		if (start_x == 0 or start_x == self.x-1 or start_y == 0 or start_y == self.y-1):				
			fileout.write("".join(str(x) for x in (step_count, "\n", start_x, " , ", start_y)))
		else:
			fileout.write("".join(str(x) for x in ("-1", "\n", start_x, " , ", start_y)))
		fileout.close()
		sys.exit()

"""
main() defines the arguments that are taken in from command line. The input file is used to populate the array elements with 0s and then mirrors are populated into the array.

"""
def main():
	parser=argparse.ArgumentParser(description="Fire a laser through a maze")
	parser.add_argument("-in",help="txt input file" ,dest="input", type=str, required=True)
	parser.add_argument("-out",help="txt output filename" ,dest="output", type=str, required=True)
	args=parser.parse_args()
	
	fileinp = open(args.input,'r')
	input_data = []																			

	for line in fileinp:
		data = line.strip("\n").split(" ")							
		input_data.append(data)
		
	fileinp.close()

	"""
	dimensions, starting coordinates and initial laser direction are defined.
	"""
	x = int(input_data[0][0])
	y = int(input_data[0][1])
	start_x = int(input_data[1][0])
	start_y = int(input_data[1][1])
	direction = input_data[1][2].rstrip()												

	"""
	maze array is created
	"""
	maze = [0] * int(x)																	
	for i in range(int(x)):																
		maze[i] = [0] * int(y)
		
	count = len(input_data)

	"""
	mirrors are populated
	"""
	for i in range(2, count - 1):														
		mirror_x = int(input_data[i][0])												
		mirror_y = int(input_data[i][1])
		maze[mirror_x][mirror_y] = input_data[i][2].rstrip()
		
	step_count = 0

	mz = Maze(maze, x, y, args.output)
	if start_x >= 0 or start_x < x or start_y >= 0 or start_y < y and step_count < 20:		
		if direction == 'S':																
			mz.south(direction, start_x, start_y, step_count)
		elif direction == 'N':
			mz.north(direction, start_x, start_y, step_count)
		elif direction == 'E':
			mz.east(direction, start_x, start_y, step_count)
		elif direction == 'W':
			mz.west(direction, start_x, start_y, step_count)	
	
if __name__=="__main__":
	main() 
