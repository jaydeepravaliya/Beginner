def reverse_words(sentence: str):

    words = sentence.split(" ")

    lst2 = words[::-1]

    output_sentence = " ".join(lst2)

    return output_sentence


if __name__ == "__main__":
    try:
        str1 = input()
        print(reverse_words(str1))

    except EOFError:
        print("No input provided.")
    except Exception as e:
        print(f"An error occurred: {e}")
