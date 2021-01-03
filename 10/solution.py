import os
import re
import math
import collections
import string


def main():
	numbers = sorted(read_numbers())
	differences = get_differences(numbers)
	print(differences.count(1) * differences.count(3))
	acc = [0, 0, 1]
	for diff in differences:
		res = sum(acc[diff - 1:])
		acc = acc[diff:] + [0] * diff
		acc[2] = res
	print(acc[2])


	
def get_differences(numbers):
	prev = 0
	result = []
	for item in numbers:
		result.append(item - prev)
		prev = item
	result.append(3)
	return result

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