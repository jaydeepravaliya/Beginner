"""
4. Given an array of size N. The task is to rotate array by D elements
towards right
Sample Input: arr = [1, 2, 3, 4, 5], D = 2
Sample Output: arr after rotation = [4, 5, 1, 2, 3]
"""

import json


def rotate_array(arr, rotation_amount):

    n = len(arr)

    rotation_amount = rotation_amount % n
    rotated_array = [0] * n

    for i in range(rotation_amount):
        rotated_array[i] = arr[n - rotation_amount + i]

    for i in range(n - rotation_amount):
        rotated_array[rotation_amount + i] = arr[i]

    return rotated_array


if __name__ == "__main__":
    try:
        lst_str = input()
        lst = json.loads(lst_str)

        k = int(input())

        print(rotate_array(lst, k))

    except json.JSONDecodeError:
        print("Invalid input. Please enter a valid JSON list.")
    except Exception as e:
        print("An error occured: {e}")
