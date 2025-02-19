"""
12. Create a login page backend to ask users to enter the username
and password. Make sure to ask for a Re-Type Password and if the
password is incorrect give a chance to enter it again but it should
not be more than 3 times.
"""


def check_password(username, password):

    attempts = 3

    while attempts > 0:
        re_entered_pass = input("Please re-enter password:\n")

        if password == re_entered_pass:
            print("Correct password")
            return True
        else:
            attempts -= 1
            if attempts > 0:
                print(f"Password doesn't match. Attempts left: {attempts}")
            else:
                print("Incorrect password. Too many attempts.")
                return False

    return False


if __name__ == "__main__":
    try:
        username = input("Enter username:\n")
        password = input("Enter password:\n")

        if check_password(username, password):
            print("Login successful.")
        else:
            print("Login failed.")
    except Exception as e:
        print(f"An error occurred: {e}")