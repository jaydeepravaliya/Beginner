"""
13. Write a Python program to find if a given string starts with a
given character using Lambda.
    Sample input: input_string = "Hello, World!", given_char = "H"
    Sample Output: True
"""


def check_string(text: str, given_char: str):
    try:
        starts_with = lambda text, given_char: (
            True if text.startswith(given_char) else False
        )
        return starts_with(text, given_char)
    except Exception as e:
        return f"An error occurred: {e}"


if __name__ == "__main__":
    try:
        user_input = input()
        given_char = input()

        result = check_string(user_input, given_char)
        print(f"{result}")

    except Exception as e:
        print(f"An error occured: {e}")
