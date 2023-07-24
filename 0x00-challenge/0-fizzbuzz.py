#!/usr/bin/python3
""" FizzBuzz
"""
import sys


def is_divisible_by_3(n):
    """
    Checks if a number is divisible by 3.
    """
    return n % 3 == 0


def is_divisible_by_5(n):
    """
    Checks if a number is divisible by 5.
    """
    return n % 5 == 0


def fizzbuzz(n):
    """
    FizzBuzz function prints numbers from 1 to n separated by a space.

    - For multiples of three print "Fizz" instead of the number and for
      multiples of five print "Buzz".
    - For numbers which are multiples of both three and five print "FizzBuzz".
    """
    if n < 1:
        return

    tmp_result = []
    for i in range(1, n + 1):
        if is_divisible_by_3(i) and is_divisible_by_5(i):
            tmp_result.append("FizzBuzz")
        elif is_divisible_by_3(i):
            tmp_result.append("Fizz")
        elif is_divisible_by_5(i):
            tmp_result.append("Buzz")
        else:
            tmp_result.append(str(i))
    print(" ".join(tmp_result))


if __name__ == '__main__':
    if len(sys.argv) <= 1:
        print("Missing number")
        print("Usage: ./0-fizzbuzz.py <number>")
        print("Example: ./0-fizzbuzz.py 89")
        sys.exit(1)

    number = int(sys.argv[1])
    fizzbuzz(number)

