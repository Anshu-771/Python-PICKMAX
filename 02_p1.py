

# variables are used to store values
# they can be used to refer to those values later in the program
# variable names can contain letters, numbers, and underscores
# they cannot start with a number
# variable names are case-sensitive
# variable names cannot be a reserved word in Python
# variable whitespace is not allowed
# variable names should be descriptive and meaningful
# variable can start with aletter or underscore

# types of  datatypes
# int, float, str, bool, list, tuple, dict, set , NoneType

# Practice 1

a = 10 #int
b = 21.45 #float
c = "hello it's me Anshu" #str
d = True #bool
e = None #NoneType

print(a)
print(b)
print(c)
print(d)
print(e)


# type() function is used to get the datatype of a variable
# it returns the datatype of the variable
# it can convert one datatype to another datatype
# it can be used to check the datatype of a variable

print(type(a))
print(type(b))
print(type(c))
print(type(d))
print(type(e))

f = str(a) # converting int to str
print(f)
print(type(f))


# input() function is used to take input from the user
# it always returns a string
# it can be converted to other datatypes using type conversion functions
# int(), float(), str(), bool()
# input() function can take a prompt as an argument

g = int(input("Enter a Number 1 : ")) # taking user input and converting it to int
h = int(input("Enter a Number 2 : ")) # taking user input and converting it to int

print ("The sum is : ", g + h) # printing the sum of two numbers

