# Practice 3

# Q1
# Write a program display a name entered in an input box with Good afternoon.
name = input("Enter Your Name: ")
print("Good Afternoon", name)


# Q2
# Write a program To A latter template Using multiline Print like name, You are selected, date
name_1 = input("Enter the name for letter: ")
date_1 = input("Enter the date for letter: ")

print( f'''
Dear {name_1},
you are selected!
Date: {date_1}
''')

method = '''
hello (nm1),
i'am (nm2)...
'''

print(method.replace("(nm1)", "Rajuu").replace("(nm2)", "alian")) # Chaining of replace method variable 

# Q3
# Write a programme to detect double space in a string.

dubl =  "Hello World this is a Double  space"
print(dubl.find("  "))

# Q4
# Replace the double space from a with a single space.
print(dubl.replace("  ", " "))
# Q5
# Write a program to format the following letter using escape sequence characters.

name_2 = "hello Rajuu,\n\tMai aapka dost \"Babu Ram\"....\n\tMai aapko 5 rupaye dunga.\n\tThankuu for reading"
print(name_2)
