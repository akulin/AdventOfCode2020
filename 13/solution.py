import os
import re
import math
import collections
import string
import itertools



def main():
	lines = read_lines()
	time = int(lines[0])
	bus_ids = list(map(int, filter(str.isdigit, lines[1].split(','))))
	minimum_waiting_time = 0
	best_bus_id = -1
	for bus_id in bus_ids:
		waiting_time = bus_id - (time % bus_id)
		if best_bus_id == -1 or minimum_waiting_time > waiting_time:
			best_bus_id = bus_id
			minimum_waiting_time = waiting_time
	print(minimum_waiting_time)
	print(best_bus_id)
	print(minimum_waiting_time * best_bus_id)



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