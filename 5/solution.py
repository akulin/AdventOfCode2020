import os
import re
import math
import collections

def main():
	lines = read_lines()
	s = set()
	for line in lines:
		s.add(pass2id(line))

	for bp in range(min(s), max(s)):
		if bp not in s:
			print(bp)

def pass2id(boarding_pass):
	row_part, seat_part = boarding_pass[:7], boarding_pass[7:]
	row_number = int(row_part.replace('F', '0').replace('B', '1'), 2)
	seat_number = int(seat_part.replace('L', '0').replace('R', '1'), 2)
	return row_number * 8 + seat_number

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
os.