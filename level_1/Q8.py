
def least_common_multiple(num1, num2):
    result = 0

    if num1 == 0 or num2 == 0:
        return 0

    if num1 > num2:
        greater = num1
    else:
        greater = num2

    while True:
        if (greater % num1 == 0) and (greater % num2 == 0):
            result = greater
            break

        greater += 1

    return result


if __name__ == "__main__":
    try:
        x = int(input())  # Or sys.stdin.readline().strip() for more robust input
        y = int(input())
        print(least_common_multiple(x, y))
    except ValueError:
        print("Invalid input. Please enter an integer.")
