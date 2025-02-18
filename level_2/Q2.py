"""
2. Create a function that takes a list and returns a new list with
unique elements of the first list.
    Sample Input: list1 = [1, 2, 2, 3, 4, 4, 5, 5]
    Sample Output: list2 = [1, 2, 3, 4, 5]
"""
import json

def unique_elements_in_list(lst1):

    st1 = set(lst1)

    return list(st1)


if __name__ == "__main__":
    try:
        lst_str = input()
        lst = json.loads(lst_str)

        print(unique_elements_in_list(lst))
    
    except json.JSONDecodeError:
        print("Invalid input. Please enter a valid JSON list.")
    except Exception as e:
        print("An error occured: {e}")
