# strings

# String is a datatype is presented in sequence of character enclosed in quotes
# String is immutable means you can't change the string once it is created.
# you can represent in 3 way 

a = 'Anshu'
b = "Anshu"
c = '''Anshu'''

print(a,b,c)


# string slice is nothing It's like extracting some Of string (0 to length-1)
# If you count the string(start) it starts from 0 index When you count string(back) it will start from -1 index
# Find a length used count from 1, +1 add based on indexing.
# You can extract A part from a given string based on their index value.

name = 'Anshu'
ixt = name[0:3]  # First index include , last index not include If you not define the first index it will assume it is 0 And if you not define the last index it will assume its length.
print(ixt)
ext = name[0::2] # First index include , last index not include , And the last one skip character If you define it will not skip that(like 2 at this position will print)
print(ext)

print(len(name)) # len() function to fin a length
print(name.endswith('u')) # endswith() function to check the last character
print(name.startswith('a')) # startswith() function to check the first character

name_1 = "aman is Aman"
print(name_1.count('m')) # Count how many times a character is present in a string
print(name_1.find('m')) # find() function to find the index of a character If character not found it will return -1
r = name_1.capitalize() # capitalize() function to convert first character to uppercase
print(r.replace("aman","anshu")) # replace() function to replace a character with another character

print("hello \nI\"amm \t Anshu\\PICKMAN")