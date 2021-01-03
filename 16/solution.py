import os
import re
import math
import collections
import string
import itertools


def parse_rules(rules):
	result = {}
	for line in rules.split('\n'):
		name, ranges = line.split(':')
		result[name] = []
		for str_range in map(str.strip, ranges.split('or')):
			start, end = map(int, str_range.split('-'))
			result[name].append((start, end))
	return result

def parse_ticket(line):
	return list(map(int, line.split(',')))

def check_rule(value, rules):
	for start, end in rules:
		if start <= value <= end:
			return True
	return False

def is_invalid_ticket(ticket, rules):
	for value in ticket:
		if not any(check_rule(value, rule) for rule in rules.values()):
			return False
	return True

def get_suitable_value_indexes(rule, tickets):
	indexes = []
	for value_index in range(len(tickets[0])):
		if all(check_rule(ticket[value_index], rule) for ticket in tickets):
			indexes.append(value_index)
	return indexes

def match(rules, tickets):
	result = {}
	rule_items = list(rules.items())
	suitable_value_indexes = [get_suitable_value_indexes(rule, tickets) for _, rule in rule_items]
	matched_indexes = set()
	while len(matched_indexes) != len(rule_items):
		for rule_number, indexes in enumerate(suitable_value_indexes):
			if len(indexes) == 1:
				matched_indexes.add(indexes[0])
				result[rule_items[rule_number][0]] = indexes[0]
		for rule_number, indexes in enumerate(suitable_value_indexes):
			suitable_value_indexes[rule_number] = [index for index in indexes if index not in matched_indexes]

	return result

def main():
	full_input = read_full_input()
	parts = full_input.split('\n\n')
	rules = parse_rules(parts[0])
	my_ticket = parse_ticket(parts[1].split('\n')[1])
	nearby_tickets = list(map(parse_ticket, filter(bool, parts[2].split('\n')[1:])))

	# part 1
	# result = 0
	# for ticket in nearby_tickets:
	# 	for value in ticket:
	# 		if not any(check_rule(value, rule) for rule in rules.values()):
	# 			result += value
	# print(result)

	valid_tickets = [ticket for ticket in nearby_tickets if is_invalid_ticket(ticket, rules)]
	rule_to_index = match(rules, valid_tickets)
	result = 1
	for name in rules:
		if name.startswith('departure'):
			result *= my_ticket[rule_to_index[name]]
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