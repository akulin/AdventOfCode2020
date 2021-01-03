import os
import re
import math
import collections
import string


MODULE = 20201227
SUBJECT_NUMBER = 7

def reverse_pow(x, result):
	value = x
	for p in range(MODULE):
		if value == result:
			return p + 1
		value = (x * value) % MODULE

def main():
	card_public_key = 8252394
	door_public_key = 6269621
	card_loop_size = reverse_pow(SUBJECT_NUMBER, card_public_key)
	door_loop_size = reverse_pow(SUBJECT_NUMBER, door_public_key)
	print(card_loop_size, door_loop_size)
	print(pow(door_public_key, card_loop_size, MODULE))


if __name__ == '__main__':
	main()
