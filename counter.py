"""
    counter.py - Count number of lines in a file.

    Author: Jorgen Holbrook (2021.01.06) adapted from Jed Yang (2021.01.01)

    To use this program:
    - Create a test file (called test.txt, for example) containing some long
      lines (more than 80 characters) and some shorter lines.
    - Put the test file in the same folder as this program (otherwise this
      program cannot find it).
    - Open this program in Thonny and run it.
    - Type in the file name (test.txt, or whatever name you chose) when asked.
"""

file_name = input("Please enter the name of the file to analyze: ")
num_total_lines = 0
num_long_lines = 0

for line in open(file_name):
    num_total_lines = num_total_lines + 1
    if len(line) > 80:
        num_long_lines = num_long_lines + 1

print(file_name, "has", num_total_lines, "lines in total.")
print(file_name, "has", num_long_lines, "long lines (> 80 characters).")