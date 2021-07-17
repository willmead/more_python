"""
Grains
======

1) Write a function to calculate the number of grains
    on a specific square

    grains = 2 ** square

2) Write a loop to calculate the number of grains on the entire
    chess board. (63 squares, starting at square 0)

3) If a grain of rice is worth 1p, how much is the total rice worth?

4) How many grains of rice are on the 23rd square?

5) What if the board were 100 squares big? How many grains would
    it contain?
"""

def grains_on_square(square):
    grains = 2 ** square
    return grains

total_grains = 0

for square in range(0, 100):
    total_grains += grains_on_square(square)

print(grains_on_square(23))
print(f"{total_grains:,}")
