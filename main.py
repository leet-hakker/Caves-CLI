from world import Map
from utils import *
from player import Player
import time
import os
import sys


def gen_ui(world, player):
	world_string = world_map.generate_world_string(player.position)
	# Gen ui
	ui_string = get_ui_string(day, player)
	# Combine world and master strings
	full_string = build_final_string(world_string, ui_string)

	# Clear terminal to make room for the map
	if os.name == 'nt':
		os.system('cls')
	else:
		os.system('clear')

	return full_string

# Begin play
name = input("Hello adventurer! Tell me your name and we shall begin our journey...\n")

# Gen world
day = 1
shape = (56, 56)
world_map = Map(shape)
world_map.get_map((0, 0))
x, y = find_start(world_map.cellmap, world_map.shape)

player = Player(name, [x, y])

time.sleep(0.3)
print(f"{player.name}, eh? Well then... let's begin.\n\n\n")
time.sleep(1)

game_loop = True
time_per_turn = 10
while game_loop:
	try:
		action, params = input(gen_ui(world_map, player)).split()
		action = int(action)
	except:
		try:
			action, params = last_action, last_params
		except:
			action = -1
	if action > 0:
		if action == 1:
			player.move(int(params[0:-1]), params[-1], world_map)
		last_action = action
		last_params = params
