class Course:
    def __init__(self, name, teacher, weights):
        self.name = name
        self.teacher = teacher
        self.weights = weights
        # dict of the form: { 'test_id': weight, ... }

class Student:
    def __init__(self, name, courses):
        self.name = name
        self.courses = courses
        # dict of the form: { 'course_id': [('test_id', mark), ...], ... }

# Given a CSV file called @filename.csv, returns a list of lists
# representing the values on each line after the first line (header).
# e.g. result_list[2][0] is the first value on the 3rd line (ignoring header)
# Throws an AssertionError if the first line of @filename.csv is not @header
def read_csv_file(filename, header):
    result_list = []
    with open(filename+'.csv') as f:
        line = f.readline().rstrip() # read header
        assert line == header, 'Invalid header.'
        line = f.readline().rstrip() # read line after header
        while line:
            values = line.split(',')
            result_list.append(values)
            line = f.readline().rstrip() # read next line
    return result_list
