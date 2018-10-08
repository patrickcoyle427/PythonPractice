#!usr/bin/python3

'''
Given the names and grades for each student in a Physics class of n students,
store them in a nested list and print the name(s) of any student(s)
having the second lowest grade.

Print the name(s) of any student(s) having the second lowest grade in Physics;
if there are multiple students,order their names alphabetically and
print each one on a new line.
'''

def find_second_lowest(student_grades):

    by_grades = sorted(student_grades, key=lambda grade: grade[1])
    # sorts by student grades, lowest to highest.

    lowest_grade = by_grades[0][1]
    # The first position of the by_grades list is the lowest grade

    second_lowest = None

    for student in by_grades:

        grade = student[1]

        if grade > lowest_grade:

            second_lowest = grade
            break

    second_lowest_students = [student[0] for student in by_grades if student[1] == second_lowest]

    second_lowest_students.sort()

    for student in second_lowest_students:

        print(student)


if __name__ == '__main__':

    sample_input = [['Harry', 37.21], ['Berry', 37.21], ['Tina', 37.2],
                    ['Akriti', 41], ['Harsh', 39]]

    find_second_lowest(sample_input)
