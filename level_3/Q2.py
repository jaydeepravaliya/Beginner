def count_lines_in_file(filename="demo.txt"):
    try:
        with open(filename, "r") as file:
            lines = file.readlines()
            return len(lines)

    except FileNotFoundError:
        print(f"File {filename} not found.")
        return []
    except Exception as e:
        print(f"An error occured: {e}")
        return []


if __name__ == "__main__":
    print(count_lines_in_file())
