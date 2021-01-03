import os
import re
import math
import collections
import string
import itertools


RAW_MONSTER = '''                  # \n#    ##    ##    ###\n #  #  #  #  #  #   '''

def main():
	tiles = {tile_id: tile for tile_id, tile in read_tiles()}
	border_to_tile_ids, tile_id_to_neighbors = build_neighborhood(tiles)

	result = 1
	for tile_id, neighbors in tile_id_to_neighbors.items():
		if len(neighbors) == 2:
			result *= tile_id
	print('part 1:', result)

	image = build_image(tiles, tile_id_to_neighbors, border_to_tile_ids)
	monster = get_monster_image()
	matched_cells = set()
	for form in get_all_form_of_image(monster):
		matched_cells = matched_cells.union(get_matches(image, form))
	print('part 2:', count_symbol(image, '#') - len(matched_cells))


def count_symbol(image, symbol):
	result = 0
	for line in image:
		result += line.count(symbol)
	return result

def get_monster_image():
	return RAW_MONSTER.split('\n')

def get_matches(image, fragment):
	matches = set()
	for start_raw, start_column in itertools.product(range(len(image) - len(fragment)), range(len(image[0]) - len(fragment[0]))):
		current_monster_matches = []
		for fragment_row, fragment_column in itertools.product(range(len(fragment)), range(len(fragment[0]))):
			if fragment[fragment_row][fragment_column] == '#':
				if image[start_raw + fragment_row][start_column + fragment_column] == '#':
					current_monster_matches.append((start_raw + fragment_row, start_column + fragment_column))
				else:
					break
		else:
			matches.update(current_monster_matches)
	return matches


def build_image(tiles, tile_id_to_neighbors, border_to_tile_ids):
	result = []
	row_start = prepare_first_tile(tiles, tile_id_to_neighbors, border_to_tile_ids)

	while row_start is not None:
		row = build_image_row(tiles, border_to_tile_ids, row_start)
		result.append(row)
		row_start = find_bottom_neighbor(row_start, tiles, border_to_tile_ids)
	for row_index in range(len(result)):
		for column_index in range(len(result[0])):
			result[row_index][column_index] = remove_borders(result[row_index][column_index])

	return connect_tiles(result)

def connect_tiles(tiles):
	result = []
	for row in tiles:
		for line_index in range(len(row[0])):
			line = ''.join([tile[line_index] for tile in row])
			result.append(line)
	return result


def build_image_row(tiles, border_to_tile_ids, current):
	row = []
	while current is not None:
		row.append(current[1])
		current = find_right_neighbor(current, tiles, border_to_tile_ids)
	return row

def find_bottom_neighbor(current, tiles, border_to_tile_ids):
	current_tile_id, current_tile = current
	current_bottom_border = get_bottom_border(current_tile)
	tile_ids = border_to_tile_ids[current_bottom_border][::]
	tile_ids.remove(current_tile_id)
	if not len(tile_ids):
		return None
	next_tile_id = tile_ids[0]
	next_tile = tiles[next_tile_id]
	for form in get_all_form_of_image(next_tile):
		if get_top_border(form) == current_bottom_border:
			return next_tile_id, form
	# fix
	# while get_top_border(next_tile) != current_bottom_border:
	# 	next_tile = rotate90(next_tile)
	# return next_tile_id, next_tile

def find_right_neighbor(current, tiles, border_to_tile_ids):
	current_tile_id, current_tile = current
	current_right_border = get_right_border(current_tile)
	tile_ids = border_to_tile_ids[current_right_border][::]
	tile_ids.remove(current_tile_id)
	if not len(tile_ids):
		return None
	next_tile_id = tile_ids[0]
	next_tile = tiles[next_tile_id]
	for form in get_all_form_of_image(next_tile):
		if get_left_border(form) == current_right_border:
			return next_tile_id, form
	# fix
	# while get_left_border(next_tile) != current_right_border:
	# 	next_tile = rotate90(next_tile)
	# return next_tile_id, next_tile


def prepare_first_tile(tiles, tile_id_to_neighbors, border_to_tile_ids):
	first_tile_id = find_first_tile(tile_id_to_neighbors)
	first_tile = tiles[first_tile_id]
	outside_borders = [border for border in get_all_borders(first_tile) if len(border_to_tile_ids[border]) == 1]
	for form in get_all_form_of_image(first_tile):
		if get_top_border(form) in outside_borders and get_left_border(form) in outside_borders:
			return first_tile_id, form

def find_first_tile(tile_id_to_neighbors):
	for tile_id, neighbors in tile_id_to_neighbors.items():
		if len(neighbors) == 2:
			return tile_id

def build_neighborhood(tiles):
	border_to_tile_ids = dict()
	for tile_id, tile in tiles.items():
		for border in get_all_borders(tile):
			border_to_tile_ids.setdefault(border, []).append(tile_id)

	tile_id_to_neighbors = dict()
	for _, neighbors in border_to_tile_ids.items():
		if len(neighbors) == 1:
			continue
		for first, second in itertools.combinations(neighbors, r=2):
			tile_id_to_neighbors.setdefault(first, set()).add(second)
			tile_id_to_neighbors.setdefault(second, set()).add(first)
	return border_to_tile_ids, tile_id_to_neighbors

def remove_borders(tile):
	return [line[1:-1] for line in tile][1:-1]

def get_all_form_of_image(image):
	for i in range(4):
		yield image
		yield flip(image)
		image = rotate90(image)

def flip(image):
	return [''.join(row)[::-1] for row in image]

def rotate90(image):
	return [''.join(row)[::-1] for row in zip(*image)]

def get_top_border(tile):
	return tile[0]

def get_left_border(tile):
	return ''.join(row[0] for row in tile)

def get_bottom_border(tile):
	return tile[-1]

def get_right_border(tile):
	return ''.join(row[-1] for row in tile)

def get_borders(tile):
	yield get_top_border(tile)
	yield get_left_border(tile)
	yield get_bottom_border(tile)
	yield get_right_border(tile)

def get_all_borders(tile):
	for border in get_borders(tile):
		yield border
		yield border[::-1]

def read_tiles():
	lines = read_lines()
	tile_id = None
	tile = []
	for line in lines:
		if not line:
			yield tile_id, tile
			tile_id = None
			tile = []
			continue
		if line.startswith('Tile'):
			tile_id = int(line[5:-1])
			continue
		tile.append(line)
	yield tile_id, tile

def print_tile(tile):
	for line in tile:
		print(line)

def read_full_input():
	with open('input.txt', 'r') as f:
		return f.read()

def read_lines():
	with open('input.txt', 'r') as f:
		return map(lambda s: s.strip(), f.readlines())

def read_numbers():
	with open('input.txt', 'r') as f:
		return list(map(lambda s: int(s.strip()), f.readlines()))

if __name__ == '__main__':
	main()