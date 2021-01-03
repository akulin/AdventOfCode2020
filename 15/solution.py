import os
import re
import math
import collections
import string
import itertools




def main():
	start_numbers = [0,3,1,6,7,5]
	last_occurences = {value: (index + 1) for (index, value) in enumerate(start_numbers[:-1])}
	last_number = start_numbers[-1]
	for index in range(len(start_numbers), 30000000):
		if last_number in last_occurences:
			new_last_number = index - last_occurences[last_number]
			last_occurences[last_number] = index
			last_number = new_last_number
		else:
			last_occurences[last_number] = index
			last_number = 0
	print(last_number)



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