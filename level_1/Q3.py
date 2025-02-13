import json


def grade_calculation(marks):
    """
    Only take marks from 5 subjects
    """

    total_subjects = len(marks)
    if total_subjects != 5:
        print("Enter 5 subjet marks in list. \nNo more No Less!!!")
        return None

    percentage = sum(marks) / 5
    print(f"Percentage: {percentage}")

    if percentage >= 90 and percentage <= 100:
        print("Grade: A")
    elif percentage >= 80:
        print("Grade: B")
    elif percentage >= 70:
        print("Grade: C")
    elif percentage >= 60:
        print("Grade: D")
    elif percentage >= 40:
        print("Grade: E")
    elif percentage < 40:
        print("Grade: F")


if __name__ == "__main__":
    try:
        list_str = input()
        marks = json.loads(list_str)
        grade_calculation(marks)

    except json.JSONDecodeError:
        print("Invalid JSON format for a list.")
