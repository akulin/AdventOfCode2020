import os
import re
import math
import collections



def main():
	lines = read_lines()
	delta_x, delta_y = 3, 1
	deltas = [(1,1), (3,1), (5,1), (7,1), (1,2)]
	ans = 1
	for delta_x, delta_y in deltas:
		ans *= solve(lines, delta_x, delta_y)
	print(ans)

def solve(lines, delta_x, delta_y):
	x, y = 0, 0
	ans = 0
	width = len(lines[0])
	while y < len(lines):
		if lines[y][x] == '#':
			ans += 1
		x += delta_x
		x %= width
		y += delta_y
	return ans

def read_lines():
	with open('input.txt', 'r') as f:
		return list(map(lambda s: s.strip(), f.readlines()))

def read_numbers():
	with open('input.txt', 'r') as f:
		return list(map(lambda s: int(s.strip()), f.readlines()))

if __name__ == '__main__':
	main()