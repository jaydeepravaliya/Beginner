"""
9. Write a Python program to count the frequency of each element
in a list.
Input_list = [1, 2, 3, 2, 4, 1, 2, 4, 5]
Frequency count: {1: 2, 2: 3, 3: 1, 4: 2, 5: 1}
"""

import json


def count_frequency(lst1: list):

    freq_count = {}

    for element in lst1:

        freq_count[element] = freq_count.get(element, 0) + 1
    return freq_count


if __name__ == "__main__":
    try:
        lst1 = input()
        element_list = json.loads(lst1)

        print(count_frequency(element_list))

    except json.JSONDecodeError:
        print("Invalid JSON format for a list.")
