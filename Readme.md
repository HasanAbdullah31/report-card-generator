# Title: Report Card Generator
### Author: Hasan Abdullah (<hasanabdullah31415@gmail.com>)

#### Description:
Given the files `students.csv`, `courses.csv`, `tests.csv`, and `marks.csv`
with appropriate headers (see example files attached), this script (`main.py`)
generates a text file `report.txt` containing the report cards of each student.
The script assumes that the information in the CSV files are valid (no empty
entries, no repeated entries, no conflicting entries, etc.), and throws errors
otherwise. Note that the order of the students in the report card is based on
student ID, and the order of the courses is based on course ID.

#### Instructions:
1. In the command line, run `python main.py` (assumes you are in this directory)
2. Assuming there are no errors, the report cards will be output to `report.txt`

*NOTES:* The Python version should be at least 2.7.16. Also, `report.txt` will
be overwritten after the script runs successfully, so be careful!
