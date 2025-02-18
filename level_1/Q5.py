"""
5. Write a Python program to find the factorial of a number using a
for loop.
Input: 5
Output: 120
"""

"""    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers")
    elif n == 0:
        return 1
    else:
        return n * find_factorial(n - 1)
"""


def find_factorial(n):

    if n == 0:
        return 1
    if n < 0:
        raise ValueError("Invalid input. Please enter a Positive Number.")

    result = n

    for i in range(n - 1, 1, -1):
        result = result * i

    return result


if __name__ == "__main__":
    try:
        n = int(input())
        print(find_factorial(n))

    except ValueError:
        print("Invalid input. Please enter an integer.")
