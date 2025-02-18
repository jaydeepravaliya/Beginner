def is_power_of_2(n: int):

    if n <= 0:
        return False
    if n == 1:
        return True
    if n % 2 != 0:
        return False

    return is_power_of_2(n // 2)


if __name__ == "__main__":
    try:
        num = int(input())
        print(is_power_of_2(num))
    except ValueError:
        print("Invalid input. Please enter an integer.")
    except RecursionError:
        print("Input too large. Please enter smaller number")
    except Exception as e:
        print(f"An error occurred: {e}")
