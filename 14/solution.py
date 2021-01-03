import os
import re
import math
import collections
import string
import itertools


def apply_mask(mask, value):
	for index, digit in enumerate(mask):
		if digit == 'X':
			continue
		value |= 2 ** index
		if digit == '0':
			value -= 2 ** index
	return value


def is_pow_of_two(n):
	return (n & (n-1) == 0) and n != 0

def get_addresses(mask, address, index, value):
	if index == len(mask):
		yield value
		return
	if mask[index] == '0':
		for value in get_addresses(mask, address, index + 1, value + (address & (2 ** index))):
			yield value
		return
	if mask[index] == '1':
		for value in get_addresses(mask, address, index + 1, value + (2 ** index)):
			yield value
		return

	for result in get_addresses(mask, address, index + 1, value + (2 ** index)):
		# print(1, index)
		yield result
	for result in get_addresses(mask, address, index + 1, value):
		# print(2, index)
		yield result


def main():
	memory = dict()
	lines = read_lines()
	mask = None
	for line in lines:
		tokens = line.split()
		if line.startswith('mask'):
			mask = tokens[2][::-1]
		else:
			address_base = int(tokens[0][4:-1])
			value = int(tokens[2])
			addresses = list(get_addresses(mask, address_base, 0, 0))
			if (len(addresses) != len(set(addresses))) and len(addresses) == 16:
				print(mask, address_base, addresses)
			for address in addresses:
				memory[address] = value
	print(sum(memory.values()))



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