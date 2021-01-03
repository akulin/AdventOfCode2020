import os
import re
import math
import collections
import string
import itertools

def evaluate_part2(expr):
	tokens = expr.replace(' ', '')
	result, _ = evaluate_subexpr_part2(tokens, 0)
	return result

def evaluate_subexpr_part2(tokens, index):
	accumulator, index = evaluate_operand_part2(tokens, index)
	while index < len(tokens) and tokens[index] != ')':
		operation = tokens[index]
		if operation == '*':
			right_value, index = evaluate_subexpr_part2(tokens, index + 1)
			accumulator *= right_value
		else:
			right_value, index = evaluate_operand_part2(tokens, index + 1)
			accumulator += right_value
	return accumulator, index

def evaluate_operand_part2(tokens, index):
	if tokens[index] == '(':
		node, index = evaluate_subexpr_part2(tokens, index + 1)
		return node, index + 1
	return int(tokens[index]), index + 1

def evaluate_part1(expr):
	tokens = expr.replace(' ', '')
	result, _ = evaluate_subexpr_part1(tokens, 0)
	return result

def evaluate_operand_part1(tokens, index):
	if tokens[index] == '(':
		value, index = evaluate_subexpr_part1(tokens, index + 1)
		return value, index + 1
	return int(tokens[index]), index + 1

def evaluate_subexpr_part1(tokens, index):
	accumulator, index = evaluate_operand_part1(tokens, index)
	while index < len(tokens) and tokens[index] != ')':
		operation = tokens[index]
		operand, index = evaluate_operand_part1(tokens, index + 1)
		if operation == '*':
			accumulator *= operand
		else:
			accumulator += operand
	return accumulator, index


def main():
	lines = read_lines()
	result = 0
	for line in lines:
		result += evaluate_part2(line)
	print(result)

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