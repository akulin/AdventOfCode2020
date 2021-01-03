import os
import re
import math
import collections
import string
import itertools



# def make_counts(max_s): # число чисел с суммой s без 0
# 	result = [0] * (max_s + 1)

# 	return  result


# counts = make_counts(8) # counts[i] - количество чисел без 0 с суммой i

# условия:
# - сумма <= 10
# - нет 0
# - последние две цифры равны

def G():
	result = 0
	for s in range(2, 11):
		result += F(s)
	print(result)



# условия:
# - сумма == s
# - нет 0
# - последние две цифры равны

def F(s):
	result = 0
	for last_digit in range(1, s // 2 + 1):
		result += H(s, last_digit)
	return result

# условия:
# - сумма == s
# - нет 0
# - последние две цифры равны last_digit
# s
# _____xx

def H(s, last_digit):
	rest_s = s - last_digit * 2
	return P(rest_s)

# условия
# нет 0
# сумма равна rest_s

def P(rest_s):
	if rest_s < 0:
		return 0
	if rest_s == 0:
		return 1
	result = 0
	for first_digit in range(1, 10):
		result += P(rest_s - first_digit)

	return result





















def main():
	lines = read_lines()
	lines = list(map(lambda x: ['.'] + list(x) + ['.'], lines))
	lines = [['.'] * len(lines[0])] + lines + [['.'] * len(lines[0])]

	old_state = lines
	new_state = simulate_round_part2(old_state)
	while old_state != new_state:
		old_state, new_state = new_state, simulate_round_part2(new_state)

	ans = sum(row.count('#') for row in new_state)
	print(ans)


def get_occupation_found(state_value, old_occupation_found):
	if state_value == 'L':
		return False
	return old_occupation_found or state_value == '#'

def get_visible_occupation_counts(state):
	visible_occupation_counts = [[0] * len(state[0]) for i in range(len(state))]
	vertical_borders = list(itertools.product(range(len(state)),[0, len(state[0]) - 1]))
	horizontal_borders = list(itertools.product([0, len(state) - 1], range(1, len(state[0]) - 1)))
	contour = vertical_borders + horizontal_borders

	for start_row, start_column in contour:
		for dy, dx in itertools.product([1, 0, -1], repeat=2):
			if dx == 0 and dy == 0:
				continue
			if start_column == 0 and dx == 0:
				continue
			if start_row == 0 and dy == 0:
				continue
			i, j = start_row, start_column
			occupation_found = False
			while -1 < i < len(state) and -1 < j < len(state[0]):
				if occupation_found:
					visible_occupation_counts[i][j] += 1
				occupation_found = get_occupation_found(state[i][j], occupation_found)
				i += dy
				j += dx

	return visible_occupation_counts


def simulate_round_part2(state):
	visible_occupation_counts = get_visible_occupation_counts(state)
	result = []
	for i in range(len(state)):
		result_row = ['.'] * len(state[i])
		for j in range(len(result_row)):
			if state[i][j] == '.':
				continue
			occupied_seats_count = visible_occupation_counts[i][j]
			result_row[j] = state[i][j]
			if occupied_seats_count == 0:
				result_row[j] = '#'
			elif occupied_seats_count >= 5 and state[i][j] == '#':
				result_row[j] = 'L'
		result.append(result_row)
	return result


def simulate_round_part1(state):
	result = []
	for i in range(len(state)):
		result_row = ['.'] * len(state[i])
		for j in range(len(result_row)):
			if state[i][j] == '.':
				continue
			occupied_seats_count = count_occupied_seats_near(state, j, i)
			result_row[j] = state[i][j]
			if occupied_seats_count == 0:
				result_row[j] = '#'
			elif occupied_seats_count >= 4 and state[i][j] == '#':
				result_row[j] = 'L'
		result.append(result_row)
	return result


def count_occupied_seats_near(state, x, y):
	result = 0
	for dx, dy in itertools.product([-1, 0, 1], repeat=2):
		if dx == 0 and dy == 0:
			continue
		if state[y + dy][x + dx] == '#':
			result += 1
	return result

def print_state(state):
	for line in state:
		print(''.join(map(str, line)))

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