import sys
from noise import PerlinNoiseFactory
import random

GRAVITY = 20
WALKING_SPEED = 5
FLYING_SPEED = 15
MAX_JUMP_HEIGHT = 1


def create_stairs(x, z, STONE, game):
    y = -1
    for x_co in range(x, x+10):
        game.add_block((x_co, y, z), STONE)
        y += 1


def create_hill(x, z, STONE, game):
    height = 10
    side_length = 5
    taper = 1
    block = STONE

    for y_co in range(-1, 5):
        for x_co in range(x - side_length, x + side_length):
            for z_co in range(z - side_length, z + side_length):
                game.add_block((x_co, y_co, z_co), block)
        side_length -= 1


def create_flat_world(game, GRASS, STONE):
    size = 50
    y = 0
    for x in range(-size, size + 1):
        for z in range(-size, size + 1):
            game.add_block((x, y - 2, z), GRASS)
            game.add_block((x, y - 3, z), STONE)

    for i in range(10):
        x = random.randint(1, 50)
        z = random.randint(1, 50)
##        create_hill(x, z, STONE, game)
        create_stairs(x, z, STONE, game)
    
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
##    create_random_world2(game, GRASS, SAND)
    create_flat_world(game, GRASS, STONE)


def get_blocks_label(current_block):
    return f'1: Brick, 2: Dirt, 3: Sand'

