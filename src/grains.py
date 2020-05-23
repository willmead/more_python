def grains_on_square(square):
    if square < 0 or square > 63:
        print("Not a legal square")

    return 2**square


def total_grains():
    total_grains = 0
    for square in range(0, 64):
        total_grains += grains_on_square(square)
    return total_grains
