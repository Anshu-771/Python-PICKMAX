# Practice set 4 


# Q1
# Write a program to store 7 fruit in a list entered by the user.

fruits = []
for i in range(7):
    aa = input(f"Enter the name of fruit {i+1} : ")
    fruits.append(aa)
print(fruits)

# Q2
# write a program to accept marks of six students and display them in a sorted manner.

marks = []
for i in range(6):
    a = int(input(f"Enter marks of subject : {i+1} = "))
    marks.append(a)
marks.sort()
print("The marks in sorted  : \n",marks)

# Q3
# check that tuple type cannot be changed in a python.

# a = (1,2,3,4,5)
# a[0] = 45 # it will give error because tuple is immutable

# Q4
# Write a program to sum a list with 4 numbers.

list_1 = [1,2,3,4]
print("the sum of list is : ", list_1[0] + list_1[1] + list_1[2] + list_1[3])
print("the sum of list using sum() function is : ", sum(list_1))

# Q5
# Write a program to count the number of 0 in following tuple a = (7,0,8,0,0,9)

a = (7,0,8,0,0,9)
c = a.count(0)
print("the number of 0 in the tuple is :", c)