"""
A palindromic number reads the same both ways. The largest palindrome
made from the product of two 2-digit numbers is 9009 = 91 x 99.

Find the largest palindrome made from the product of two 3-digit numbers.
"""
import itertools


def is_palindrome(number):
    string = str(number)
    return string == string[::-1]


def largest_palindrome_1():
    for i in range(100, 1000):
        for j in range(100, 1000):
            product = i * j
            if is_palindrome(product):
                largest_palindrome = product

    return largest_palindrome


def largest_palindrome_2():
    three_digit_nums = range(100, 1000)

    for x, y in itertools.product(three_digit_nums, three_digit_nums):
        product = x * y
        if is_palindrome(product):
            largest_palindrome = product

    return largest_palindrome


our_range = range(100, 1000)
palindromes = [x * y for x, y in itertools.product(our_range, our_range) if is_palindrome(x * y)]

print(largest_palindrome_2())
