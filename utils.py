def find_start(cellmap, shape):
    y = 0
    for x in range(shape[0]):
        if not cellmap[x][y]:
            return x, y
    y = shape[1]-1
    for x in range(shape[0]):
        if not cellmap[x][y]:
            return x, y
    x = 0
    for y in range(shape[1]):
        if not cellmap[x][y]:
            return x, y
    x = shape[0]-1
    for y in range(shape[1]):
        if not cellmap[x][y]:
            return x, y


def get_ui_string(day, player):
    base_ui_string = f"""
            Day {day} - {player.name}



        ┌───────────────┐               Health: {'♡ '*player.health}               Position:
        │   Inventory   │               Hunger: {'🍗'*player.hunger}                      X: {player.position[1]}
        │               │{len('                                          Hunger: '+'🍗'*player.hunger)*' '}Y: {player.position[0]}
        │1 {player.inventory[0].name + ' '*(12-len(player.inventory[0].name))} │
        │               │               Available actions:
        │2 {player.inventory[1].name + ' '*(12-len(player.inventory[1].name))} │               1 | Move
        │               │               2 | Use item
        │3 {player.inventory[2].name + ' '*(12-len(player.inventory[2].name))} │
        │               │
        │4 {player.inventory[3].name + ' '*(12-len(player.inventory[3].name))} │
        │               │
        │5 {player.inventory[4].name + ' '*(12-len(player.inventory[4].name))} │
        │               │
        └───────────────┘"""

    return base_ui_string

def build_final_string(world, ui):
    final = ""
    for i in range(len(world.split('\n'))-len(ui.split('\n'))-1):
        ui += """
"""
    for world_line, ui_line in zip(world.split('\n'), ui.split('\n')):
    	final += world_line + ui_line + '\n'
    return final
