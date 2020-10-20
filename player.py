from item import *

class Player(object):
    def __init__(self, name, position):
        self.name = name
        self.health = 5
        self.hunger = 5
        self.position = position
        self.inventory = [DiggingTool(name="Basic Shovel", durability=50, effectiveness=2), Item(""), Item(""), Item(""), Item("")]

    def move(self, amount, direction, world):
        x = self.position[0] % world.shape[0]
        y = self.position[1] % world.shape[1]


        if direction == "N":
            world.get_map((x-amount, y))
            for i in range(x-amount, x):
                if world.cellmap[i][y]:
                    return False
            self.position[0] -= amount
            return True
        elif direction == "E":
            world.get_map((x, y+amount))
            for i in range(y, y+amount+1):
                if world.cellmap[x][i]:
                    return False
            self.position[1] += amount
            return True
        elif direction == "S":
            world.get_map((x+amount, y))
            for i in range(x, x+amount+1):
                if world.cellmap[i][y]:
                    return False
            self.position[0] += amount
            return True
        elif direction == "W":
            world.get_map((x, y-amount))
            for i in range(y-amount, y):
                if world.cellmap[x][i]:
                    return False
            self.position[1] -= amount
            return True
