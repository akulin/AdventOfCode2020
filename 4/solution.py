import os
import re
import math
import collections

required_fields = ['ecl', 'pid', 'eyr', 'hcl', 'byr', 'iyr', 'hgt']
optional_fields = ['cid']

def main():
	content = read_full_input()
	parts = content.split('\n\n')
	ans = 0
	for part in parts:
		tokens = part.split()
		data = []
		for token in tokens:
			key, value = token.split(':')
			data.append((key, value))
		if check_fields(data):
			ans += 1
	print(ans)

def check_fields(data):
	keys = list(map(lambda x: x[0], data))
	if not check_keys(keys):
		return False
	result = True
	for key, value in data:
		if key == 'byr':
			result = result if 1920 <= int(value) <= 2002 else False
		elif key == 'iyr':
			result = result if 2010 <= int(value) <= 2020 else False
		elif key == 'eyr':
			result = result if 2020 <= int(value) <= 2030 else False
		elif key == 'hgt':
			result = result if check_hgt(value) else False
		elif key == 'hcl':
			result = result if  check_hcl(value)  else False
		elif key == 'ecl':
			result =  result if  value in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']  else False
		elif key == 'pid':
			result = result if  len(value) == 9 and value.isdigit()  else False


	return result

def check_hcl(hcl):
	return re.match('#[a-f0-9]{6}', hcl) is not None

def check_hgt(hgt):
	value, unit = hgt[:-2], hgt[-2:]
	if not value.isdigit():
		return False
	value = int(value)
	if unit == 'cm':
		return 150 <= value <= 193
	elif unit == 'in':
		return 59 <= value <= 76
	return False

def check_keys(keys):
	if (len(keys) > len(required_fields) + len(optional_fields)):
		return False
	expected = required_fields if len(keys) == len(required_fields) else required_fields + optional_fields
	return len(set(keys).intersection(expected)) == len(expected)


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