"""
1. Write a Python program to find the common elements between
two lists.
    Sample Input: l1 = [1, 2, 3, 4, 5] and l2 = [4, 5, 6, 7, 8]
    Sample output: [4, 5]
"""
import json

def common_elements_in_two_list(list1, list2):

    common_elements = []

    for element in list1:
        if element in list2:
            common_elements.append(element)

    return common_elements


if __name__ == "__main__":
    try:
        lst1_str = input()  # Or sys.stdin.readline().strip() for more robust input
        lst1 = json.loads(lst1_str)

        lst1_str = input()
        lst2 = json.loads(lst1_str)

        common = common_elements_in_two_list(lst1, lst2)
        print(common)

    except json.JSONDecodeError:
        print("Invalid input. Please enter a valid JSON list.")
    except Exception as e:
        print(f"An error occured: {e}")
