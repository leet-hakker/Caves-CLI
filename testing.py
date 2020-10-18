import numpy as np
import noise

shape = (56, 56)
scale = 10.0
octaves = 6
persistence = 0.5
lacunarity = 2.0

chanceToStartAlive = 0.45

world = np.zeros(shape).tolist()
for i in range(shape[0]):
    for j in range(shape[1]):
        world[i][j] = noise.pnoise2(i/scale,
                                    j/scale,
                                    octaves=octaves,
                                    persistence=persistence,
                                    lacunarity=lacunarity,
                                    repeatx=shape[0],
                                    repeaty=shape[1],
                                    base=0) < chanceToStartAlive/7

def generateWorldString(cellmap, playerPos):
	world_string = ""
	for i in range(len(cellmap)):
		for j in range(len(cellmap[i])):
			if i == playerPos[0] and j == playerPos[1]:
				world_string += "┫┣"
			else:
				if cellmap[i][j]:
					world_string += "██"
				else:
					world_string += "  "
		world_string += "\n"
	return world_string

print(generateWorldString(world, (0,0)))
