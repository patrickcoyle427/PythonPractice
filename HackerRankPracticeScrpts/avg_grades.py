#!usr/bin/python3

'''
You have a record of n students. Each record contains the student's name,
and their percent marks in Maths, Physics and Chemistry. The marks can be
floating values. The user enters some integer n followed by the names and
marks for students. You are required to save the record in a dictionary
data type. The user then enters a student's name. Output the average percentage
marks obtained by that student, correct to two decimal places.
'''

def grade_avg(names, scores):

    # names and scores are lists with the same len.
    # names is a list of strings, containing the names of students.
    # scores is a list containing lists of grades the student earned.

    comb_input = zip(names, scores)
    # zip combines two iterables into one

    student_marks = {}

    for i in comb_input:

        student_marks[i[0]] = i[1]

    print(student_marks.keys())

    query_name = input('Enter a student name to see their average grades: ')

    avg = sum(student_marks[query_name]) / len(student_marks[query_name])

    print('{:.2f}'.format(avg))

if __name__ == '__main__':

    students = ['Krishna', 'Arjun', 'Malika']
    grades = [[67, 68, 69,], [70, 98, 63], [52, 56, 60]]

    grade_avg(students, grades)
                      

