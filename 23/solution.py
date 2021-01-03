import os
import re
import math
import collections
import string
import itertools

PUZZLE_INPUT = '219748365'
# PUZZLE_INPUT = '389125467'

class Node(object):
    def __init__(self, value):
        self.value = value
        self.next = None

class СyclicСhain:
	def __init__(self, values):
		self.excluded_values = set()
		self.all_values = [None] * (len(values) + 1)
		self.current_node = Node(values[0])
		self.all_values[self.current_node.value] = self.current_node
		node = self.current_node
		for value in values[1:]:
			next_node = Node(value)
			self.all_values[next_node.value] = next_node
			node.next = next_node
			node = node.next
		node.next = self.current_node


	def find_value(self, value):
		if value in self.excluded_values:
			return None
		return self.all_values[value]

	def move_current_node(self):
		self.current_node = self.current_node.next

	def pull_out_range_after_current(self, length=3):
		range_end_node = self.current_node
		for _ in range(length):
			range_end_node = range_end_node.next
			self.excluded_values.add(range_end_node.value)
		new_next_node = range_end_node.next
		range_end_node.next = None
		result = self.current_node.next
		self.current_node.next = new_next_node
		return result

	def insert_after(self, destination, range_root):
		range_end_node = range_root
		while range_end_node.next is not None:
			range_end_node = range_end_node.next
		range_end_node.next = destination.next
		destination.next = range_root
		self.excluded_values = set()

	def to_list(self):
		result = [self.current_node.value]
		node = self.current_node.next
		while node != self.current_node:
			result.append(node.value)
			node = node.next
		return result

def decrement(value, max_value):
	return (value - 2 + max_value) % (max_value) + 1

def get_chain_after_game(numbers, step_counts):
	max_number = max(numbers)
	chain = СyclicСhain(numbers)
	for i in range(step_counts):
		sub_nodes = chain.pull_out_range_after_current()
		destination_value = decrement(chain.current_node.value, max_number)
		destination = chain.find_value(destination_value)
		while destination is None:
			destination_value = decrement(destination_value, max_number)
			destination = chain.find_value(destination_value)
		chain.insert_after(destination, sub_nodes)
		chain.move_current_node()
	return chain


def main():
	digits = list(map(int, PUZZLE_INPUT))
	chain = get_chain_after_game(digits, 100)
	result_digits = chain.to_list()
	result_digits = result_digits[result_digits.index(1):] + result_digits[:result_digits.index(1)]
	print(''.join(map(str, result_digits[1:])))


	digits = list(map(int, PUZZLE_INPUT))
	digits += list(range(max(digits) + 1, 10 ** 6 + 1))
	chain = get_chain_after_game(digits, 10000000)
	one_node = chain.find_value(1)
	result_digits = chain.to_list()
	print(result_digits[result_digits.index(1)-5:result_digits.index(1)+5])
	print(one_node.value, one_node.next.value, one_node.next.next.value)
	print(one_node.next.value * one_node.next.next.value)



if __name__ == '__main__':
	main()	
