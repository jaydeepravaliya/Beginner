def JtoI(filename="WORDS.txt"):
    try:
        with open(filename, "r") as file:
            lines = file.readlines()
            corrected_lines = ""

            for line in lines:
                corrected_line = line.replace("J", "I")
                corrected_lines += corrected_line

            return corrected_lines

    except FileNotFoundError:
        print(f"File {filename} not found.")
        return []
    except Exception as e:
        print(f"An error occured: {e}")
        return []


if __name__ == "__main__":
    print(JtoI())
