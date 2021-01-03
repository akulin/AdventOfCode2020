import os
import re
import math
import collections



def main():
	lines = read_lines()
	ans = 0
	for line in lines:
		rule, password = line.split(': ')
		counts, letter = rule.split()
		left, right = map(int, counts.split('-'))
		left -= 1
		right -= 1
		letters_counter = collections.Counter(password)
		if ((password[left] == letter) + (password[right] == letter)) == 1:
			ans += 1
	print(ans)


def read_lines():
	with open('input.txt', 'r') as f:
		return list(map(lambda s: s.strip(), f.readlines()))

def read_numbers():
	with open('input.txt', 'r') as f:
		return list(map(lambda s: int(s.strip()), f.readlines()))

if __name__ == '__main__':
	main()