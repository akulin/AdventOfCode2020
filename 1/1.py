import os
import re
import math
import sys

def main():
	numbers = set(read_numbers())
	for a in numbers:
		for b in numbers:
			if (2020 - a - b) in numbers:
				print(a * b * (2020 - a - b))
				return


def read_numbers():
	for line in sys.stdin:
		yield int(line)

if __name__ == '__main__':
	main()