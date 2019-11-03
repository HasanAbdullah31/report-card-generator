#!/usr/bin/python

from components import *

def main():
    students = {} # dict of the form { 'id': Student_object, ... }
    courses = {}  # dict of the form { 'id': Course_object, ... }
    students_info = read_csv_file('students', 'id,name')
    courses_info = read_csv_file('courses', 'id,name,teacher')
    tests_info = read_csv_file('tests', 'id,course_id,weight')
    marks_info = read_csv_file('marks', 'test_id,student_id,mark')

    for info in students_info:
        id = info[0]
        name = info[1]
        students[id] = Student(name, {})

    for info in courses_info:
        id = info[0]
        name = info[1]
        teacher = info[2]
        courses[id] = Course(name, teacher, {})

    tests = {} # dict of the form { 'test_id': 'course_id', ... }
    for info in tests_info:
        id = info[0]
        course_id = info[1]
        weight = int(info[2])
        courses[course_id].weights[id] = weight
        tests[id] = course_id

    # Make sure the sum of all the weights of all tests in each course is 100
    for course in courses.values():
        name = course.name
        total_weight = sum(course.weights.values())
        if total_weight != 100:
            raise Exception('The total test weight in '+name+' is not 100.')

    for info in marks_info:
        test_id = info[0]
        student_id = info[1]
        mark = int(info[2])
        course_id = tests[test_id]
        try:
            students[student_id].courses[course_id].append((test_id, mark))
        except KeyError:
            students[student_id].courses[course_id] = [(test_id, mark)]

    output_lines = []
    for student_id, student in sorted(students.items()):
        output_lines.append('Student Id: '+student_id+', name: '+student.name)
        total_mark = 0.0 # used to calculate the total average
        course_output = []
        # Make sure the student has taken all tests for each course they are in
        for course_id, tests in sorted(student.courses.items()):
            # tests is a list of the form [('test_id', mark), ...]
            course = courses[course_id]
            course_output.append('\tCourse: '+course.name+', Teacher: '+course.teacher)
            tests_needed = course.weights.keys()
            tests_taken = [test[0] for test in tests]
            if sorted(tests_taken) != sorted(tests_needed):
                raise Exception(name+' has not completed '+course.name+'.')

            course_average = 0.0
            for test in tests:
                test_id = test[0]
                mark = test[1]
                weight = course.weights[test_id]/100.0
                course_average += mark*weight

            mark_output = '%.2f' % round(course_average, 2)
            course_output.append('\tFinal Grade:\t'+mark_output+'%\n')
            total_mark += course_average

        average = 0.0
        num_courses = len(student.courses)
        if num_courses != 0: average = total_mark/num_courses
        mark_output = '%.2f' % round(average, 2)
        output_lines.append('Total Average:\t'+mark_output+'%\n')
        output_lines.extend(course_output)

    with open('report.txt', 'w') as f:
        for line in output_lines:
            f.write(line+'\n')

if __name__ == '__main__':
    main()
