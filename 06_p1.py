# Conditional Statements

# If-Else Statement
# if condition is true, execute the block of code under if
# else, execute the block of code under else
# If-Else can be used to execute one block of code among two options based on a condition.

# Else-If Ladder
# if condition1 is true, execute block of code under if
# else if condition2 is true, execute block of code under elif
# else, execute block of code under else
# Else-If Ladder can be used to execute one block of code among multiple options based on conditions.
# in Python, 'else if' is written as 'elif'
# there can be multiple elif statements
# last else is optional, if all conditions are false, then else block will be executed.

# Nested If-Else
# if condition1 is true, then check condition2
# if condition2 is true, execute block of code under inner if
# else, execute block of code under inner else


# example of conditional statements

num = int(input("Enter your age :  "))

if (num >= 18):
    if (num >= 60):
        print("you can vote and you are a senior citizen")
    else:
        print("you can vote")
elif (num <= 0):
    print("invalid age entered !!! ")
else:
    print("you cannot vote")

print("Thank you")

# (Ternary Operator)
# variable = value_if_true if condition else value_if_false
# Ternary Operator can be used to assign a value to a variable based on a condition in a single line.
a = 10
b = 20
max_value = a if a > b else b
print(f"The maximum value is: {max_value}")