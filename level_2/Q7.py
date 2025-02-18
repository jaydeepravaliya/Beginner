"""
7. Write a Python function that finds the median of a list of
numbers.
    Sample Input: number_list = [7, 2, 5, 1, 9, 3]
"""

import json


def find_median(given_list: list):

    n = len(given_list)

    if n == 0:
        raise ValueError("Cannot calculate median of an empty list.")
    
    sorted_data = sorted(given_list)

    if n % 2 == 1:
        middle_index = n // 2
        median = sorted_data[middle_index]
    
    else:
        middle_index1 = (n // 2) - 1
        middle_index2 = n // 2

        median = (sorted_data[middle_index1] + sorted_data[middle_index2]) / 2

    return median

try:
    user_input = input()
    data = json.loads(user_input)

    result = find_median(data)
    print(f"Median of {data}: \n{result}")
except json.JSONDecodeError:
    print("")
