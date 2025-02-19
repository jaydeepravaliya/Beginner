
def decode_string(user_input):

    try:
        string_list = user_input.split("0")

        filtered_list = list(filter(None, string_list))  # Remove empty strings

        if len(string_list) == 0:
            return "Invalid Input"
        
        first_name = filtered_list[0]
        last_name = filtered_list[1]
        id_number = filtered_list[2]


        if not id_number.isdigit():
            return "Invalid Input. ID number must be a number"
        
        return {
            "first_name": first_name,
            "last_name": last_name,
            "id": id_number
        }    
    
    except Exception as e:
        return f"An error occurred: {e}"



if __name__ == "__main__":
    user_input = input()
    print(decode_string(user_input))