"""
7. Write a Python program to check if a string is an anagram of
another string.
string1 = "listen", 
string2 = "silent"
Output: True
"""


def check_anagram(str1, str2):

    if len(str1) != len(str2):
        return False

    count_chars1 = {}
    count_chars2 = {}

    for char in str1:
        count_chars1[char] = count_chars1.get(char, 0) + 1

    for char in str2:
        count_chars2[char] = count_chars2.get(char, 0) + 1

    return count_chars1 == count_chars2


if __name__ == "__main__":
    try:
        string1 = str(input())
        string2 = str(input())
        print(check_anagram(string1, string2))
    except ValueError:
        print("Invalid input. Please enter a string.")
