"""
11. Write a Python program to calculate the sum of digits of a given
number until the sum becomes a single-digit number.
    - Sample Input: num = 987
    - Sample Output: Sum_of_digits = 24,
    - Again compute the sum of digits so that it can be reduced to
    on single digit.
    - Final Output: 6
"""


def sum_digits(n):

    s = 0
    while n > 0:
        s += n % 10
        n //= 10

    return s


def single_digit_sum(num):

    while num >= 10:
        num = sum_digits(num)
        if num >= 10:
            print(f"Sum_of_digits = {num}")

    return num


if __name__ == "__main__":
    try:
        num = int(input())

        if num < 0:
            raise ValueError("Input must be a non-negative integer.")

        final_sum = single_digit_sum(num)
        print(f"Final Output: {final_sum}")

    except ValueError as e:
        print(e)
    except Exception as e:
        print(f"An error occurred: {e}")
