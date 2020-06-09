"""
2520 is the smallest number that can be divided by each of
the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible
by all of the numbers from 1 to 20?
"""

def divisible_1(number, max):
    for test_factor in range(max, 0, -1):
        if number % test_factor: # the result has a remainder
            return False
    return True


def divisible_2(number, max):
    for test_factor in range(1, max+1):
        if number % test_factor: # the result has a remainder
            return False
    return True


searching = True
max = 20
current_num = max

while searching:
    if current_num % 1_000_000 == 0:
        print(current_num)
    if divisible_2(current_num, max):
        searching = False
        print(current_num)
    else:
        current_num += max
