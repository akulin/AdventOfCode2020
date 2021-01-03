import os
import re
import math
import collections
import string


def main():
	numbers = read_numbers()
	preambule_length = 25
	counts = collections.Counter(numbers[:preambule_length])
	first_wrong_number = None
	for i in range(preambule_length, len(numbers)):
		number = numbers[i]
		for j in range(i - preambule_length, i):
			preambule_number = numbers[j]
			if number == preambule_number * 2:
				continue
			if counts[number - preambule_number] > 0:
				break
		else:
			first_wrong_number = number
			break
		counts[numbers[i - preambule_length]] -= 1
		counts[numbers[i]] += 1

	left = 0
	right = 1
	s = numbers[0]
	while True:
		if s == first_wrong_number and right - left > 1:
			break
		if s > first_wrong_number:
			s -= numbers[left]
			left += 1
		else:
			if right == len(numbers):
				break
			s += numbers[right]
			right += 1
	print(min(numbers[left:right]) + max(numbers[left:right]))




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