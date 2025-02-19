"""
11. Write a Python program to create a list of given strings
individually of the list using the Python map function.
    Eg. Input:
    ['Red', 'Blue', 'Black', 'White', 'Pink']
    Output:
    [['R', 'e', 'd'], ['B', 'l', 'u', 'e'], ['B', 'l', 'a', 'c', 'k'], ['W', 'h', 'i', 't', 'e'], ['P', 'i',
    'n', 'k']]
"""

import json


def split_strings(string_list: list):

    return list(map(list, string_list))


if __name__ == "__main__":
    try:
        lst_str = input()
        lst = json.loads(lst_str)

        print(split_strings(lst))

    except json.JSONDecodeError:
        print("Invalid input. Please enter a valid JSON list.")
    except Exception as e:
        print("An error occured: {e}")
