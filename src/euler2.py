"""
Each new term in the Fibonacci sequence is generated by
adding the previous two terms. By starting with 1 and 2,
the first 10 terms will be:

1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

By considering the terms in the Fibonacci sequence whose
values do not exceed four million, find the sum of the
even-valued terms.
"""
import timeit

def fibonacci_1():
    sequence = [1, 1, 2]
    x = 2
    y = 1
    z = 1

    while x < max:
        z = x
        x = x + y
        y = z
        sequence.append(x)
    return sequence


def fibonacci_2():
    sequence = [1, 1]
    while(sequence[-1]) < max:
        sequence.append(sequence[-1] + sequence[-2])
    return sequence


def time_code():
    # Remove max parameters from functions
    time_taken = timeit.timeit(fibonacci_1, number=1_000_000)
    print(time_taken)
    time_taken = timeit.timeit(fibonacci_2, number=1_000_000)
    print(time_taken)


max = 4_000_000
even_fibonacci = [term for term in fibonacci_1() if term % 2 == 0]
print(f"Sum of all even fibonacci terms smallers than {max}: {sum(even_fibonacci)}")
