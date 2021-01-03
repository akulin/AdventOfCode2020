import os
import re
import math
import collections
import string
import itertools


def main():
	ingredients_counter = collections.Counter()
	potential_ingredients = dict()
	for line in read_lines():
		ingredients, allergens = line[:-1].split('(contains ')
		ingredients = ingredients.split()
		allergens = allergens.replace(',', '').split()
		ingredients_counter.update(ingredients)
		for allergen in allergens:
			if allergen in potential_ingredients:
				potential_ingredients[allergen].intersection_update(ingredients)
			else:
				potential_ingredients[allergen] = set(ingredients)

	# all_allergens = set()
	# for allergen, ingredients in potential_ingredients.items():
	# 	all_allergens.update(ingredients)
	# result = 0
	# for ingredient, count in ingredients_counter.items():
	# 	if ingredient not in all_allergens:
	# 		result += count
	# print(result)

	all_allergens = dict()
	while True:
		ingredients_to_remove = []
		for allergen, ingredients in potential_ingredients.items():
			if len(ingredients) == 1:
				ingredient = ingredients.pop()
				ingredients_to_remove.append(ingredient)
				all_allergens[allergen] = ingredient
		if not ingredients_to_remove:
			break
		for allergen, ingredients in potential_ingredients.items():
			for ingredient in ingredients_to_remove:
				ingredients.discard(ingredient)

	part1_result = 0
	dangerous_ingredients = set(all_allergens.values())
	for ingredient, count in ingredients_counter.items():
		if ingredient not in dangerous_ingredients:
			part1_result += count
	print('part1:', part1_result)


	part2_result = ','.join([ingredient for allergen, ingredient in sorted(all_allergens.items())])
	print("part2:", part2_result)


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