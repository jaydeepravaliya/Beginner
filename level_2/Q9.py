"""
9. Write a Python program that executes an operation on a list and
handles an IndexError exception if the index is out of range.

"""

def list_operation(my_list: list, index: int):
    try:
        return my_list[index]
    except IndexError:
        return f"Index {index} is out of range for list of length {len(my_list)}."
    except Exception as e:
        return f"An unexpected error occurred: {e}"
    


if __name__ == "__main__":
    try:
        my_list = [1, 2, 3, 4, 5]
        index = int(input())
        result = list_operation(my_list, index)
        print(result)
    except Exception as e:
        print(f"An error occurred: {e}")
    
