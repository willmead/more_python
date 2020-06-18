import sys
from noise import PerlinNoiseFactory


GRAVITY = 20
WALKING_SPEED = 5
FLYING_SPEED = 15
MAX_JUMP_HEIGHT = 1


def create_hill():
    pass


def create_flat_world(game, GRASS, STONE):
    size = 10
    y = 0
    for x in range(-size, size + 1):
        for z in range(-size, size + 1):
            game.add_block((x, y - 2, z), GRASS)
            game.add_block((x, y - 3, z), STONE)


def create_random_world2(game, GRASS, SAND):
    world = []
    size = 50
    freq = 10
    octaves = 1

    pnf = PerlinNoiseFactory(2, octaves=octaves)

    for row in range(size):
        world.append([])
        for column in range(size):
            height = int(pnf(row/ freq, column / freq) * 6 + 1)
            world[row].append(height)

    for x in range(-size // 2, size // 2):
        for z in range(-size // 2, size // 2):
            for y in range(-5, world[x][z]-1):
                game.add_block((x, y, z), GRASS)


def create_world(game, GRASS, STONE, BRICK, SAND):
    create_random_world2(game, GRASS, SAND)
    #create_flat_world(game, GRASS, STONE)


def get_blocks_label(current_block):
    return f'1: Brick, 2: Dirt, 3: Sand'

