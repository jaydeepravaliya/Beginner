"""
3. Given an array of N integers and an integer K, find the number of
pairs of elements in the array whose sum is equal to K.
    Sample Input: arr = [1, 2, 3, 4, 5], k = 6
    Sample Output: Pair count: 2

"""

import json


def count_pairs(arr, k):

    seen_elements = set()
    pair_count = 0

    for number in arr:
        x = k - number
        if x in seen_elements:
            pair_count += 1

        seen_elements.add(number)

    return pair_count


if __name__ == "__main__":
    try:
        lst_str = input()
        lst = json.loads(lst_str)

        k = int(input())

        print(count_pairs(lst, k))

    except json.JSONDecodeError:
        print("Invalid input. Please enter a valid JSON list.")
    except Exception as e:
        print("An error occured: {e}")
