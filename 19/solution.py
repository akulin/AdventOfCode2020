import os
import re
import math
import collections
import string
import itertools


def parse_rule(line):
	number_part, rules_part = line.split(':')
	number = int(number_part)
	subrules = [[int(subrule) if subrule.isdigit() else subrule[1] for subrule in rule.split()] for rule in rules_part.split('|')]
	return number, subrules

def match(rules, rule_number, line, start):
	if start >= len(line):
		return
	for subrule in rules[rule_number]:
		if len(subrule) == 1 and type(subrule[0]) is str:
			if line[start] == subrule[0]:
				yield start + 1
		else:
			current_starts = set([start])	
			for subrule_number in subrule:
				new_starts = set()
				for current_start in current_starts:
					new_starts.update(match(rules, subrule_number, line, current_start))
				current_starts = new_starts
			for current_start in current_starts:
				yield current_start


def main():
	lines = read_lines()
	rules = dict()
	for line in lines:
		if not line:
			break
		number, subrules = parse_rule(line)
		rules[number] = subrules

	#part 2	
	rules[8].append((42, 8))
	rules[11].append((42, 11, 31))

	result = 0
	for line in lines:
		if list(match(rules, 0, line, 0)).count(len(line)) > 0:
			result += 1
	print(result)
	



def read_full_input():
	with open('input.txt', 'r') as f:
		return f.read()

def read_lines():
	with open('input.txt', 'r') as f:
		return map(lambda s: s.strip(), f.readlines())

def read_numbers():
	with open('input.txt', 'r') as f:
		return list(map(lambda s: int(s.strip()), f.readlines()))

if __name__ == '__main__':
	main()