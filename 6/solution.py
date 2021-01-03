import os
import re
import math
import collections
import string

def main():
	content = read_full_input()
	ans = 0
	for part in content.split('\n\n'):
		s = set(string.ascii_lowercase)
		for token in part.split():
			s = s.intersection(set(token))
		ans += len(s)
	print(ans)


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