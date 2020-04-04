"""
If we list all the natural numbers below 10 that are multiples
of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.
"""
import timeit

def get_multiples_1():
    multiples = []

    for i in range(2, 1000):
        if i % 3 == 0:
            multiples.append(i)
        elif i % 5 == 0:
            multiples.append(i)

    return multiples


def get_multiples_2(factors, max):
    multiples = []

    for factor in factors:
        multiples.extend(range(factor, max, factor))

    return set(multiples)


# Method 1
total_1 = sum(get_multiples_1())
print(f"Method 1 Answer: {total_1}")

# Method 2
factors = [3, 5]
total_2 = sum(get_multiples_2(factors, 1000))
print(f"Method 2 Answer: {total_2}")

print()

########
# Timing
########
def wrapper(func, *args, **kwargs):
    def wrapped():
        return func(*args, **kwargs)
    return wrapped

def time_code():
    print("Timing the simple if/else function: ")
    time_taken = timeit.timeit(get_multiples_1, number=100_000)
    print(f"Function 1: {time_taken}")

    wrapped = wrapper(get_multiples_2, factors, 1000)
    print("Timing the improved function: ")
    time_taken = timeit.timeit(wrapped, number=100_000)
    print(f"Function 2: {time_taken}")

# time_code()
