# Q1
# Write a program to find the greatest of four number entered by users.

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
num3 = int(input("Enter third number: "))
num4 = int(input("Enter fourth number: "))

if (num1 >= num2) and (num1 >= num3) and (num1 >= num4):
    print(f"the first number you enter that is {num1} is the greater")
elif(num2 >= num3) and (num2 >= num4) and (num2 >= num1):
    print(f"the second number you enter that is {num2} is the greater")
elif(num3 >= num4) and (num3 >= num1) and (num3 >= num2):
    print(f"the third number you enter that is {num3} is the greater")
else:
    print(f"the fourth number you enter that is {num4} is the greater")


# Q2
# Write a program to find out whether a student has passed over failed if its requires a total of 40% and at least 33% of each subject 
# to pass. Assume three subjects and take marks as an input from the user.

sub1 = int(input("Enter marks of subject 1: "))
sub2 = int(input("Enter marks of subject 2: "))
sub3 = int(input("Enter marks of subject 3: "))

total_percentage = ((sub1 + sub2 + sub3) / 300) * 100

if (total_percentage >= 40 and sub1 >= 33 and sub2 >= 33 and sub3 >= 33):
    print("Congratulations you have passed")
else:
    print("Sorry you have failed")


# Q3
# A spam comment is defined as a text containing the following keywords: "make a lot of money", "buy now", "subscribe this", "click this".
# Write a program to detect these spams.

spamlist = ["make a lot of money", "buy now", "subscribe this", "click this", "aloo kaogya"]

comment = input("Enter your comment: ")

if (comment in spamlist):
    print("This is a spam comment")
else:
    print("This is not a spam comment")

# Q4
# Write a program to find whether a given username contains less than 10 characters or not.

username = input("enter your username: ")

if (len(username) < 10):
    print("username contains less than 10 characters")
else:
    print("username contains more than 10 characters")

# Q5
# Write a program to find out whether a given name is present in a list or not.

namelist = ["Anshu", "Ankita", "Rohit", "Sonal", "Aman"]

name = input("Enter your name: ")
if(name in namelist):
    print("Your name is present in the list you are allowed")
else:
    print("Your name is not present in the list you are not allowed")

# Q6
# Write a programme to calculate the grade of the student from his mark from the following schemes
# 90-100 => Ex
# 80-90 => A
# 70-80 => B
# 60-70 => C
# 50-60 => D
# <50 => F

marks = int(input("enter your marks: "))

if (marks >= 90) and (marks <= 100):
    print("your grade is Ex")
elif(marks >= 80) and (marks < 90):
    print("your grade is A")
elif(marks >= 70) and (marks < 80):
    print("your grade is B")
elif(marks >= 60) and (marks < 70):
    print("your grade is C")
elif(marks >= 50) and (marks < 60):
    print("your grade is D")
else:
    print("your grade is F")
 
# Q7
# Write a programme to find out whether a given post is talking about Anshu or not.

post = input("Enter your post: ")
if ("Anshu" in post):
    print("This post is talking about Anshu")
else:
    print("This post is not talking about Anshu")

