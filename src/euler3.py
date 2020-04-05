"""
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
"""

# Based on the hand drawn prime factorisation approach
def largest_prime_factor(number):
    left_num = 2
    right_num = number

    while left_num * left_num <= right_num:
        if right_num % left_num:
            left_num += 1
        else:
            right_num //= left_num

    return right_num

actual_number = 600_851_475_143
test_number = 13195

print(largest_prime_factor(actual_number))
