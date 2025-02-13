
def count_letters_and_digits(s:str):

    alphabets = 0
    numbers = 0

    for character in s:
        if character.isalpha():
            alphabets += 1
        elif character.isnumeric():
            numbers += 1
        else:
            pass
    
    print(f"Alphabets: {alphabets} & Number : {numbers}")


if __name__ == "__main__":
    try:
        s = str(input())  # Or sys.stdin.readline().strip() for more robust input
        count_letters_and_digits(s)
    except ValueError:
        print("Invalid input. Please enter a string.")
