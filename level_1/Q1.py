"""
1.Write a program in Python to perform the following operation:
    - If a number is divisible by 3 it should print “Consultadd” as a
    string
    - If a number is divisible by 5 it should print “Python Training” as
    a string
    - If a number is divisible by both 3 and 5 it should print
    “Consultadd - Python Training” as a string
"""


def check_divisibility(num):

    if num % 3 == 0 and num % 5 == 0:
        print("Consultadd - Python Training")
    elif num % 3 == 0:
        print("Consultadd")
    elif num % 5 == 0:
        print("Python Training")
    else:
        pass


if __name__ == "__main__":
    try:
        num = int(input())  # Or sys.stdin.readline().strip() for more robust input
        check_divisibility(num)
    except ValueError:
        print("Invalid input. Please enter an integer.")
