# Validation scientist coding challenge, recd: 23 April 2018
# LASER MAZE - Shreyas Krishnan


filename = input("enter a valid file name:   ")
fileinp = open(filename,'r')
input_data = []										# to hold all data for easy parsing

for line in fileinp:
	data = line.split(" ")							
	input_data.append(data)

x = int(input_data[0][0])
y = int(input_data[0][1])
start_x = int(input_data[1][0])												# coordinates for start position and subsequent player movements
start_y = int(input_data[1][1])
direction = input_data[1][2].rstrip()									# direction of laser


maze = [0] * int(x)														# creating 2D list/array
for i in range(int(x)):													# The matrix is created here and populated by 0s 
	maze[i] = [0] * int(y)

#maze[start_x][start_y] = direction							# 

	
count = len(input_data)

for i in range(2, count - 1):
	mirror_x = input_data[i][0]											# mirror coordinates
	mirror_y = input_data[i][1]
	maze[int(mirror_x)][int(mirror_y)] = input_data[i][2].rstrip()		# assigning mirrors to matrix

	
# define function or object that instructs conditions for reaction between laser and mirror and resulting direction	

step_count = 0

def south(direction, start_x, start_y, step_count):
	if direction == 'S':	
		while maze[start_x - 1][start_y] == 0:				
			start_x -= 1												# move player
			step_count += 1												# increase cell counter by one
		if maze[start_x - 1][start_y] == '\'':
			start_x -= 1												# move player
			direction = 'E'
			step_count += 1												# increase cell counter by one
			east(direction, start_x, start_y, step_count)				# call function east
		elif maze[start_x - 1][start_y] == '/':
			start_x -= 1												# move player
			direction = 'W'
			step_count += 1												# increase cell counter by one
			west(direction, start_x, start_y, step_count)				# call function west

def north(direction, start_x, start_y, step_count):
	if direction == 'N':	
		while maze[start_x + 1][start_y] == 0:
			start_x += 1
			step_count += 1												#increase cell counter by one
		if maze[start_x + 1][start_y] == '\'':
			start_x += 1
			direction = 'W'
			step_count += 1												#increase cell counter by one
			west(direction, start_x, start_y, step_count)														# call function east
		elif maze[start_x + 1][start_y] == '/':
			start_x += 1
			direction = 'E'
			step_count += 1												#increase cell counter by one
			east(direction, start_x, start_y, step_count)		
			
def east(direction, start_x, start_y, step_count):
	if direction == 'E':	
		while start_y + 1 <= y:
			while maze[start_x][start_y + 1] == 0:
				start_y += 1
				step_count += 1												#increase cell counter by one
			if maze[start_x][start_y + 1] == '\'':
				start_y += 1
				direction = 'S'
				step_count += 1												#increase cell counter by one
				south(direction, start_x, start_y, step_count)														# call function east
			elif maze[start_x][start_y + 1] == '/':
				start_y += 1
				direction = 'N'
				step_count += 1												#increase cell counter by one
				north(direction, start_x, start_y, step_count)		
						
def west(direction, start_x, start_y, step_count):
	if direction == 'W':	
		while maze[start_x][start_y - 1] == 0:
			start_y -= 1
			step_count += 1												#increase cell counter by one
		if maze[start_x][start_y - 1] == '\'':
			start_y -= 1
			direction = 'N'
			step_count += 1												#increase cell counter by one
			north(direction, start_x, start_y, step_count)														# call function east
		elif maze[start_x][start_y - 1] == '/':
			start_y -= 1
			direction = 'S'
			step_count += 1												#increase cell counter by one
			south(direction, start_x, start_y, step_count)		

			
while start_x >= 0 or start_x <= x or start_y >= 0 or start_y <= y and step_count < 20:							# while player is in matrix bounds and step count < 20 
	if direction == 'S':																						# call respective direction functions 
		south(direction, start_x, start_y, step_count)
	elif direction == 'N':
		north(direction, start_x, start_y, step_count)
	elif direction == 'E':
		east(direction, start_x, start_y, step_count)
	elif direction == 'W':
		west(direction, start_x, start_y, step_count)	

		
if (start_x < 0 or start_x > x or start_y < 0 or start_y > y):												# if player exits any matrix boundary
	print (step_count, "\n", start_x, " , ", start_y)
else:
	print ("-1", "\n", start_x, " , ", start_y)