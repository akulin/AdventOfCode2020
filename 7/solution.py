import os
import re
import math
import collections
import string

def get_name(name_with_bag):
	return ' '.join(name_with_bag.split()[:2])

def get_number_of_bags(name, bag2content):
	counts = bag2content[name]
	ans = 1
	for content_name, count in counts.items():
		ans += count * get_number_of_bags(content_name, bag2content)
	return ans


def main():
	lines = read_lines()
	bag2content = dict()
	names = []
	for line in lines:
		name, content = line.split(' contain ')
		name = get_name(name)
		names.append(name)
		if name not in bag2content:
			bag2content[name] = dict()
		if content == 'no other bags.':
			continue
		for part in content.split(','):
			tokens = part.split()
			count, bag_name = tokens[0], ' '.join(tokens[1:])
			bag_name = get_name(bag_name)
			if bag_name[-1] == '.':
				bag_name = bag_name[:-1]
			bag2content[name][bag_name] = int(count)

	# result_set = set()
	# result_set.add('shiny gold')
	# while True:
	# 	old_length = len(result_set)
	# 	for bag_name, counts in bag2content.items():
	# 		if bag_name in result_set:
	# 			continue
	# 		for content_name, count in counts.items():
	# 			if content_name in result_set:
	# 				result_set.add(bag_name)
	# 	if old_length == len(result_set):
	# 		break
	# print(len(result_set) - 1)

	print(get_number_of_bags('shiny gold', bag2content) - 1)



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