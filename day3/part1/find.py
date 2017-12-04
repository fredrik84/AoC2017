#!/usr/bin/python3
import time

with open("input") as f:
	data = int(f.readline().strip())

def move_right(x,y):
	return x+1, y

def move_down(x,y):
	return x,y-1

def move_left(x,y):
	return x-1,y

def move_up(x,y):
	return x,y+1

def gen_points(end):
	from itertools import cycle
	_moves = cycle(moves)
	n = 1
	pos = 0,0
	times_to_move = 1

	yield n,pos

	while True:
		for _ in range(2):
			move = next(_moves)
			for _ in range(times_to_move):
				if n >= end:
					return
				pos = move(*pos)
				n+=1
				yield n,pos

		times_to_move+=1

moves = [move_right, move_down, move_left, move_up]

grid = list(gen_points(int(data)))
if grid[data-1][1][0] < 0:
  x = -1*grid[data-1][1][0]
else:
  y = grid[data-1][1][0]
if grid[data-1][1][1] < 0:
  y = -1*grid[data-1][1][1]
else:
  y = grid[data-1][1][1]
print("%s" % str(int(x)+int(y)))
