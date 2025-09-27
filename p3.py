# Practice 1

#Q4
# Write a Python program to list all files in a directory in Python.
# Using os module
# for more details visit https://docs.python.org/3/library/os.html
import os 

directory_path ='/users/anshu/desktop/git-preactice/python-pick'

print_AS = os.listdir(directory_path)

print(print_AS)

for p1 in print_AS:
    print(p1)