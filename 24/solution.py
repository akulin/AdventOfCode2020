import os
import re
import math
import collections
import string


DIRECTION2DELTAS = {
	'se': (-1, -2),
	'sw': (-2, -1),
	'e': (1, -1),
	'w': (-1, 1),
	'ne': (2, 1),
	'nw': (1, 2)
}

def parse_tile(line):
	result = []
	cursor = 0
	while cursor < len(line):
		if line[cursor] in ['s', 'n']:
			result.append(line[cursor: cursor + 2])
			cursor += 2
		else:
			result.append(line[cursor])
			cursor += 1
	assert ''.join(result) == line, "parse error"
	return result

def execute_commands(commands):
	x, y = 0, 0
	for command in commands:
		dx, dy = DIRECTION2DELTAS[command]
		x += dx
		y += dy
	return x, y

def simulate_step(black_tiles):
	counter = collections.Counter()
	for tile_x, tile_y in black_tiles:
		for dx, dy in DIRECTION2DELTAS.values():
			counter[(tile_x + dx, tile_y + dy)] += 1
	result = set()
	for tile, count in counter.items():
		if tile in black_tiles:
			if count < 3:
				result.add(tile)
		elif count == 2:
			result.add(tile)
	return result

def main():
	lines = read_lines()
	counter = collections.Counter()

	for line in lines:
		commands = parse_tile(line)
		x, y = execute_commands(commands)
		counter[(x, y)] += 1
	black_tiles = set(key for key, value in counter.items() if value % 2)
	print("part 1:", len(black_tiles))

	for step in range(1, 101):
		black_tiles = simulate_step(black_tiles)
	print('part2:', len(black_tiles))

		


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
