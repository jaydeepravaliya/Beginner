

def get_even_length_strings(filename="doc.txt"):
    try:
        with open(filename, "r") as file:
            lines = file.readlines()
            even_length_strings = []

            for line in lines:
                words = line.split()
                for word in words:
                    if len(word) % 2 == 0:
                        even_length_strings.append(word)
            
            return even_length_strings
    
    except FileNotFoundError:
        print(f"File {filename} not found.")
        return []
    except Exception as e:
        print(f"An error occured: {e}")
        return []


if __name__ == "__main__":
    print(get_even_length_strings())
    