"""
    Write a Python program to find the sum of all odd numbers
    between two given numbers.
        Start = 1, stop = 10
        Sum of odd numbers: 25
"""

def sum_of_odd_numbers(start, stop):
    sum = 0
    for i in range(start, stop + 1):
        if i % 2 != 0:
            sum += i
    return sum



if __name__ == "__main__":
    try:
        start = int(input())
        stop = int(input())
        print(sum_of_odd_numbers(start, stop))
    except ValueError:
        print("Invalid input. Please enter an integer.")