import os
import re
import math
import collections
import string
import itertools
from operator import add


def get_neighbors(*args):
	dim = len(args)
	for delta in itertools.product([-1, 0, 1], repeat=len(args)):
		if all(value == 0 for value in delta):
			continue
		yield tuple(map(add, args, delta))

def simulate_turn(active_cubes):
	result = set()
	candidates_for_activation = set()
	for active_cube in active_cubes:
		active_neighbors_count = 0
		for cube in get_neighbors(*active_cube):
			if cube in active_cubes:
				active_neighbors_count += 1
			else:
				candidates_for_activation.add(cube)
		if 2 <= active_neighbors_count <= 3:
			result.add(active_cube)
	for inactive_cube in candidates_for_activation:
		active_neighbors_count = sum([(cube in active_cubes) for cube in get_neighbors(*inactive_cube)])
		if active_neighbors_count == 3:
			result.add(inactive_cube)
	return result 


def main():
	lines = read_lines()
	active_cubes = set()
	for y, line in enumerate(lines):
		for x, c in enumerate(line):
			if c == '#':
				active_cubes.add((x, y, 0, 0))

	for _ in range(6):
		active_cubes = simulate_turn(active_cubes)
		print("active_cubes", len(active_cubes))


def read_full_input():
	with open('input.txt', 'r') as f:
		return f.read()

def read_lines():
	with open('input.txt', 'r') as f:
		return list(map(lambda s: s.strip(), f.readlines()))

def read_numbers():
	with open('input.txt', 'r') as f:
		return list(map(lambda s: int(s.strip()), f.readlines()))

if __name__ == '__main__':
	main()