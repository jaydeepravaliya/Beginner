def string_length(user_input):
    try:
        temp_count = 0
        current_char = ""
        result = ""

        for i in user_input:
            if i == current_char:
                temp_count += 1
            else:
                if current_char != "":
                    result += f"{current_char}{temp_count}"

                current_char = i
                temp_count = 1

        result += f"{current_char}{temp_count}"  # Crucial for the last run

        return result

    except Exception as e:
        return f"An error occurred: {e}"


if __name__ == "__main__":
    user_input = input()
    print(string_length(user_input))
