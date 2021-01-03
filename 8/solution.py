import os
import re
import math
import collections
import string


def get_command(line):
	c, v = line.split()
	return c, int(v)

def play(commands):
	acc = 0
	cid = 0
	cids = set()
	while cid not in cids and cid < len(commands):
		# print(cid)
		cids.add(cid)
		command, value = commands[cid]
		if command == 'acc':
			acc += value
		elif command == 'jmp':
			cid += value
			continue
		cid += 1
	return acc, cid == len(commands)


def main():
	commands = list(map(get_command, read_lines()))
	for i in range(len(commands)):
		command, value = commands[i]
		if command == 'acc':
			continue
		if command == 'jmp':
			commands[i] = 'nop', value
		else:
			commands[i] = 'jmp', value
		acc, result = play(commands)
		commands[i] = command, value
		if result:
			print(acc)
			break






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