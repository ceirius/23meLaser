#!/usr/bin/env python
# Validation scientist coding challenge, recd: 23 April 2018
# LASER MAZE - Shreyas Krishnan



#import argparse
#
#def run(args):
#	filename = open(args.input) 										
#	output_filename = args.output 										
#	fout = open(args.output, 'w')
#	fout.write(step_count, '\n')
#	fout.write(start_x, start_y)
#	fout.close()
	

#def main():
#	parser=argparse.ArgumentParser(description="Fire a laser through a maze")
#	parser.add_argument("-in",help="txt input file" ,dest="input", type=str, required=True)
#	parser.add_argument("-out",help="txt output filename" ,dest="output", type=str, required=True)
#	parser.set_defaults(func=run)
#	args=parser.parse_args()
#	args.func(args)
#
#if __name__=="__main__":
#	main() 


filename = input("enter a valid file name:   ")
fileinp = open(filename,'r')
input_data = []																			# to hold all data for easy parsing


for line in fileinp:
	data = line.split(" ")							
	input_data.append(data)

x = int(input_data[0][0])
y = int(input_data[0][1])
start_x = int(input_data[1][0])															# coordinates for start position and subsequent player movements
start_y = int(input_data[1][1])
direction = input_data[1][2].rstrip()													# direction of laser


maze = [0] * int(x)																		# creating 2D list/array
for i in range(int(x)):																	# The matrix is created here and populated by 0s 
	maze[i] = [0] * int(y)

	
count = len(input_data)

for i in range(2, count - 1):															# assigning mirrors to matrix
	mirror_x = int(input_data[i][0])													# mirror coordinates
	mirror_y = int(input_data[i][1])
	#print (mirror_x, mirror_y)
	maze[mirror_x][mirror_y] = input_data[i][2].rstrip()
	

print(maze, "\n", maze[mirror_x][mirror_y], input_data[3][2], "count = ",count)
# define function or object that instructs conditions for reaction between laser and mirror and resulting direction	

step_count = 0

def west(direction, start_x, start_y, step_count):
	if start_x - 1 >= 0:																# testing if within bounds
		while maze[start_x - 1][start_y] == 0 or start_x - 1 >= 0:						# testing for no mirror
			#print(direction, start_x, start_y, step_count, "\n\n")						# move player
			start_x -= 1
			step_count += 1																# increase cell counter by one
			print("nineteen", start_x, start_y, step_count, "\n\n")
			if maze[start_x][start_y] != 0:
				if maze[start_x][start_y] == 'A':
					direction = 'N'
					print("eighteen")
					north(direction, start_x, start_y, step_count)	
					
				elif maze[start_x][start_y] == 'B':
					direction = 'S'
					print("seventeen")
					south(direction, start_x, start_y, step_count)		
					
			elif maze[start_x][start_y] == 0 and start_x == 0 or step_count == 20: 	
				print("sisteen")
				end(start_x, start_y, step_count)
				break				
	elif start_x - 1 < 0 or step_count == 20: 	
		print("tw3 two")
		end(start_x, start_y, step_count)				

def east(direction, start_x, start_y, step_count):
	if start_x + 1 < x:																	# testing if within bounds
		while maze[start_x + 1][start_y] == 0 or start_x + 1 < x:						# testing for no mirror
			#print(direction, start_x, start_y, step_count, "\n\n")						# move player
			start_x += 1
			step_count += 1																# increase cell counter by one
			print("fifteen", start_x, start_y, step_count, "\n\n")
			if maze[start_x][start_y] == 'A':
				direction = 'S'
				print("fourteen")
				south(direction, start_x, start_y, step_count)				
			elif maze[start_x][start_y] == 'B':
				direction = 'N'
				print("thirteen")
				north(direction, start_x, start_y, step_count)		
			elif start_x + 1 > x - 1 or step_count == 20: 	
				print("twelve")
				end(start_x, start_y, step_count)	
				break
	elif start_x + 1 > x - 1 or step_count == 20: 	
		print("tw2 one")
		end(start_x, start_y, step_count)
			
def north(direction, start_x, start_y, step_count):
	#while direction == 'N':															# this line is redundant
	#next_y = start_y + 1
	#print("\n", start_y, ", ", start_y+1, ", ", next_y, y, ", ", y-1,"\n\n", maze[start_x][start_y], ",", maze[start_x][start_y + 1], "\n")
	#print(start_x, start_y, "\n\n")
	
	if start_y + 1 < y:																	# testing if within bounds
		while maze[start_x][start_y + 1] == 0 or start_y + 1 < y:						# testing for no mirror
			#print(direction, start_x, start_y, step_count, "\n\n")						# move player
			start_y += 1
			step_count += 1																# increase cell counter by one
			print("eleven", start_x, start_y, step_count, "\n\n")
			if maze[start_x][start_y] == 'A':
				direction = 'W'
				print("ten")
				west(direction, start_x, start_y, step_count)				
			elif maze[start_x][start_y] == 'B':
				direction = 'E'
				print("nine")
				east(direction, start_x, start_y, step_count)		
			elif start_y + 1 >= y-1 or step_count == 20: 	
				print("eight")
				end(start_x, start_y, step_count)
				break
	elif start_y + 1 >= y-1 or step_count == 20: 	
		print("twenty")
		end(start_x, start_y, step_count)

						
def south(direction, start_x, start_y, step_count):
	if start_y - 1 >= 0:																# testing if within bounds
		while maze[start_x][start_y - 1] == 0 or start_y - 1 >= 0:						# testing for no mirror
			#print("one", direction, start_x, start_y, step_count, "\n\n")				# move player
			start_y -= 1
			step_count += 1																# increase cell counter by one
			print("two", start_x, start_y, step_count, "\n\n")

			if maze[start_x][start_y] == 'A':
				direction = 'E'
				print("three")
				east(direction, start_x, start_y, step_count)				
			elif maze[start_x][start_y] == 'B':
				direction = 'W'
				print("four")
				west(direction, start_x, start_y, step_count)		
			elif start_y - 1 < 0 or step_count == 20: 	
				print("seven")
				end(start_x, start_y, step_count)
				break
	elif start_y - 1 < 0 or step_count == 20: 	
		print("tw4 four")
		end(start_x, start_y, step_count)
				
		

def end(start_x, start_y, step_count):
	if (start_x == 0 or start_x == x-1 or start_y == 0 or start_y == y-1):				# if player exits any matrix boundary
		print (step_count, "\n", start_x, " , ", start_y)
		#run(step_count, start_x, start_y)
		print("five")
	else:
		print ("-1", "\n", start_x, " , ", start_y)
		#run(step_count, start_x, start_y)
		print("six")
		
			
if start_x >= 0 or start_x < x or start_y >= 0 or start_y < y and step_count < 20:		# while player is in matrix bounds and step count < 20 
	if direction == 'S':																# call respective direction functions 
		south(direction, start_x, start_y, step_count)
	elif direction == 'N':
		north(direction, start_x, start_y, step_count)
	elif direction == 'E':
		east(direction, start_x, start_y, step_count)
	elif direction == 'W':
		west(direction, start_x, start_y, step_count)	

		
