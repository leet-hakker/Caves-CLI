import noise
import numpy as np
import datetime


class Map(object):
    def __init__(self, shape):
        self.shape = shape
        self.chanceToStartAlive = 0.1
        self.scale = 10.0
        self.octaves = 10
        self.persistence = 0.5
        self.lacunarity = 2.0
        self.chunks = {}

    def initialise_map(self, coordinates):
        world = np.zeros(self.shape).tolist()
        x_counter = 0
        y_counter = 0
        for x in range(self.shape[0]):
            x_counter += 1
            for y in range(self.shape[1]):
                y_counter += 1
                world[x][y] = noise.snoise2((x+coordinates[0])/self.scale,
                                            (y+coordinates[1])/self.scale,
                                            octaves=self.octaves,
                                            persistence=self.persistence,
                                            lacunarity=self.lacunarity,
                                            base=0) < self.chanceToStartAlive/8
        self.chunks[f"{coordinates[0]}-{coordinates[1]}"] = world

    def count_alive_neighbours(self, world, x, y):
        count = 0
        for i in range(-1, 2):
            for j in range(-1, 2):
                neighbour_x = x+i
                neighbour_y = y+j
                if i == 0 and j == 0:
                    pass
                elif neighbour_x < 0 or neighbour_y < 0 or neighbour_x >= len(world) or neighbour_y >= len(world[0]):
                    count = count + 1
                elif world[neighbour_x][neighbour_y]:
                    count = count + 1
        return count

    def do_simulation_step(self, position):
        oldMap = self.chunks[f"{position[0]}-{position[1]}"]
        deathLimit = 2
        birthLimit = 5
        newMap = np.zeros(self.shape).tolist()
        for x in range(len(oldMap)):
            for y in range(len(oldMap[x])):
                nbs = self.count_alive_neighbours(oldMap, x, y)
                if oldMap[x][y]:
                    if nbs < deathLimit:
                        newMap[x][y] = False

                    else:
                        newMap[x][y] = True

                else:
                    if nbs > birthLimit:
                        newMap[x][y] = True

                    else:
                        newMap[x][y] = False

        self.chunks[f"{position[0]}-{position[1]}"] = newMap

    def smooth_terrain(self, position):
        cellmap = self.chunks[f"{position[0]}-{position[1]}"]
        for x in range(1, self.shape[0]-1):
            for y in range(1, self.shape[1]-1):
                alive = self.count_alive_neighbours(cellmap, x, y)
                if alive >= 5:
                    cellmap[x][y] = True

        self.chunks[f"{position[0]}-{position[1]}"] = cellmap

    def generate_map(self, position):
        # start = datetime.datetime.now()
        simulation_steps = 3
        smoothing_steps = 2
        self.initialise_map(position)
        for i in range(simulation_steps):
            self.do_simulation_step(position)
        for i in range(smoothing_steps):
            self.smooth_terrain(position)
        # print(datetime.datetime.now()-start)

    def generate_world_string(self, playerPos):
        playerPos[0] = playerPos[0] % self.shape[0]
        playerPos[1] = playerPos[1] % self.shape[1]
        world_string = ""
        for i in range(int(len(self.cellmap))):
            for j in range(int(len(self.cellmap[i]))):
                if i == playerPos[0] and j == playerPos[1]:
                    world_string += "┫┣"
                else:
                    if self.cellmap[i][j]:
                        world_string += "██"
                    else:
                        world_string += "  "
            world_string += "\n"
        return world_string

    def get_map(self, position):
        # position = position[::-1]
        if position[0] >= 0:
            nearest_x = int(round(position[0] / float(self.shape[0])) * self.shape[0])
        else:
            nearest_x = int(round(position[0] / float(self.shape[0]))
                            * self.shape[0]) - self.shape[0]
        if position[1] >= 0:
            nearest_y = int(round(position[1] / float(self.shape[1])) * self.shape[1])
        else:
            nearest_y = int(round(position[1] / float(self.shape[1]))
                            * self.shape[1]) - self.shape[1]
        nearest_x, nearest_y = nearest_y, nearest_x
        if f"{nearest_x}-{nearest_y}" in self.chunks.keys():
            self.cellmap = self.chunks[f"{nearest_x}-{nearest_y}"]
        else:
            self.generate_map((nearest_x, nearest_y))

            self.cellmap = self.chunks[f"{nearest_x}-{nearest_y}"]


if __name__ == "__main__":
    from utils import *
    import time
    shape = (56, 56)
    world = Map(shape)
    world.get_map((0, -1))
    x, y = find_start(world.cellmap, world.shape)
    world_string = world.generate_world_string([x, y])

    print(world_string)
    # time.sleep(0.1)
