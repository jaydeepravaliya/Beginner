"""
8. Write a Python function that counts the number of vowels in a
given string.
    Sample Input: string = "Hello, World!"
    Sample Output: Number of vowels: 3
"""

def count_vowels(text: str):

    vowel_count = 0
    text = text.lower()

    for character in text:
        if character in "aeiou":
            vowel_count += 1
    
    return vowel_count


if __name__ == "__main__":
    try:
        user_input = input()

        result = count_vowels(user_input)
        print(f"Number of vowels: {result}")

    except Exception as e:
        print(f"An error occured: {e}")
