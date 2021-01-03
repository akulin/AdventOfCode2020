import os
import re
import math
import collections
import string
import itertools

def read_player_cards(lines):
	player_name = next(lines)
	cards = []
	for line in lines:
		if not line:
			break
		cards.append(int(line))
	return cards

def play_part1(player1_cards, player2_cards):
	player1_cards = collections.deque(player1_cards)
	player2_cards = collections.deque(player2_cards)

	while len(player2_cards) and len(player1_cards):
		card1, card2 = player1_cards.pop(), player2_cards.pop()
		if card1 > card2:
			player1_cards.appendleft(card1)
			player1_cards.appendleft(card2)
		else:
			player2_cards.appendleft(card2)
			player2_cards.appendleft(card1)

	return list(player1_cards if len(player1_cards) else player2_cards)

def is_first_player_winner(player1_cards, player2_cards, card1, card2):
	if card1 <= len(player1_cards) and card2 <= len(player2_cards):
		player1_sub_cards = list(player1_cards)[-card1:]
		player2_sub_cards = list(player2_cards)[-card2:]
		result, _ = play_part2(player1_sub_cards, player2_sub_cards)
		return result
	else:
		return card1 > card2

def update_players_cards(player1_cards, player2_cards):
	card1, card2 = player1_cards.pop(), player2_cards.pop()
	if is_first_player_winner(player1_cards, player2_cards, card1, card2):
		player1_cards.appendleft(card1)
		player1_cards.appendleft(card2)
	else:
		player2_cards.appendleft(card2)
		player2_cards.appendleft(card1)

def play_part2(player1_cards, player2_cards):
	player1_cards = collections.deque(player1_cards)
	player2_cards = collections.deque(player2_cards)
	player1_states = set()
	while len(player2_cards) and len(player1_cards):
		state = tuple(player1_cards)
		if state in player1_states:
			return True, list(player1_cards)
		player1_states.add(state)
		update_players_cards(player1_cards, player2_cards)
	if len(player1_cards):
		return True, list(player1_cards)
	return False, list(player2_cards)

def main():
	lines = read_lines()
	player1_cards = read_player_cards(lines)[::-1]
	player2_cards = read_player_cards(lines)[::-1]

	winner_deck = play_part1(player1_cards, player2_cards)[::-1]
	result = 0
	for i in range(len(winner_deck)):
		result += (len(winner_deck) - i) * winner_deck[i]
	print("part1: ", result)

	_, winner_deck = play_part2(player1_cards, player2_cards)
	winner_deck = winner_deck[::-1]
	result = 0
	for i in range(len(winner_deck)):
		result += (len(winner_deck) - i) * winner_deck[i]
	print("part2: ", result)

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