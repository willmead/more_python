import sys
from noise import snoise2

GRAVITY = 20
WALKING_SPEED = 5
FLYING_SPEED = 15
MAX_JUMP_HEIGHT = 1


def create_hill():
    pass
    # generate the hills randomly
    # o = n - 10
    # for _ in xrange(120):
    #     a = random.randint(-o, o)  # x position of the hill
    #     b = random.randint(-o, o)  # z position of the hill
    #     c = -1  # base of the hill
    #     h = random.randint(1, 6)  # height of the hill
    #     s = random.randint(4, 8)  # 2 * s is the side length of the hill
    #     d = 1  # how quickly to taper off the hills
    #     t = random.choice([GRASS, SAND, BRICK])
    #     for y in xrange(c, c + h):
    #         for x in xrange(a - s, a + s + 1):
    #             for z in xrange(b - s, b + s + 1):
    #                 if (x - a) ** 2 + (z - b) ** 2 > (s + 1) ** 2:
    #                     continue
    #                 if (x - 0) ** 2 + (z - 0) ** 2 < 5 ** 2:
    #                     continue
    #                 self.add_block((x, y, z), t, immediate=False)
    #         s -= d  # decrement side lenth so hills taper off


def create_flat_world(game, GRASS, STONE):
    size = 10
    y = 0
    for x in range(-size, size + 1):
        for z in range(-size, size + 1):
            game.add_block((x, y - 2, z), GRASS)
            game.add_block((x, y - 3, z), STONE)


def create_random_world(game, GRASS, SAND):
    world = []
    size = 20
    freq = 10  # Smoothness 1 = Crazy, 100 = Fairly Smooth
    octaves = 1  # Level of Detail (Doesn't seem to affect much)

    for row in range(size):
        world.append([])
        for column in range(20):
            height = int(snoise2(row / freq, column / freq, octaves) * 6 + 1)
            world[row].append(height)

    for x in range(-size // 2, size // 2):
        for z in range(-size // 2, size // 2):
            for y in range(-5, world[x][z]):
                if y > 7:
                    block = SAND
                else:
                    block = GRASS
                game.add_block((x, y, z), block)

    game.add_block((0, -1, 0), GRASS)


def create_world(game, GRASS, STONE, BRICK, SAND):
    create_random_world(game, GRASS, SAND)
    # create_flat_world(game, GRASS, STONE)


def get_blocks_label(current_block):
    return f'1: Brick, 2: Dirt, 3: Sand'

