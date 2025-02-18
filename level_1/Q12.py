"""
12. Write a Python program to reverse a number using a while
loop.
    Sample Input: num = 12345
    Sample Output: revnum = 54321

"""

def reverse_number(num):

    if num == 0:
        return 0

    result_str = ""

    while num > 0:
        last_digit = num % 10
        result_str += str(last_digit)

        num = num // 10

    return int(result_str)


if __name__ == "__main__":
    try:
        num = int(input())

        if num < 0:
            raise ValueError("Input must be a non-negative integer.")

        reversed_num = reverse_number(num)
        print(f"Reversed Num: {reversed_num}")

    except ValueError as e:
        print(e)
    except Exception as e:
        print(f"An error occurred: {e}")
