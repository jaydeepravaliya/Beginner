"""
7. Write a program to construct a dictionary from the two lists
    containing the names of students and their corresponding
    subjects. The dictionary should map the students with their
    respective subjects. Let’s see how to do this using for loops and
    dictionary comprehension.
        Input: [Sam, Alice, Mona] ,
               [Commerce, Science, Computer]

        Output: [Sam: Commerce, Alice: Science , Mona: Computer]

"""

def construct_dict(students, subjects):
    return {students[i]: subjects[i] for i in range(len(students))}

    # return {stu: sub for stu, sub in zip(students, subjects)}
