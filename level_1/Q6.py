"""
6. Write a Python program to check if a given number is a perfect
number.
A Perfect number is a positive integer that is equal to the sum of
its proper divisors. For instance, 6 has divisors 1, 2, and 3, and 1 + 2 +
3 = 6, so 6 is a perfect number.
Input: 5
Output: No
"""

def check_perfect_number(num):
    sum = 0
    for i in range(1, num):
        if num % i == 0:
            sum += i
        
    if sum == num:
        print("Yes")
    else:
        print("No")


if __name__ == "__main__":
    try:
        num = int(input())
        check_perfect_number(num)
    except ValueError:
        print("Invalid input. Please enter an integer.")
