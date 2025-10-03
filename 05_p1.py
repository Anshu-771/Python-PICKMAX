# Q1
# Write a program to create a dictionary of Hindi word with the value as their English translation provide user with an option to look it up.

hindi_dic ={
    "ladka" : "boy",
    "ladki" : "girl",
    "paani" : "water",
    "aag" : "fire"
}
a = input("Enter the hindi word : ")
print("the hindi word will be : ",hindi_dic[a])
print("the hindi word will be : ",hindi_dic.get(a))

# Q2
# Write a program to input eight number from the user and display all the unique number once 

numbers = set()
for i in range(8):
    b = int(input("Enter the number : "))
    numbers.add(b)

print("the unique number are : ", numbers)

# Q3
# Can we have a set with 18 int as 18 string as value in it?

sss = {18, "18"}
print(sss)     # yes we can have a set with 18 int as 18 string as value in it because set can store multiple data types

# Q4
# What will be the length of following set s 

s = set()      # sample question to solve.....
s.add(20)
s.add(20.0)
s.add("20") 

print(len(s)) # it will be 2 because 20 and 20.0 are considered same in set but "20" is different I can convert automatically Int to float and visa-versa.
print(s)

# Q5
# s = {} What is the type of s?

ss = {}

print(type(ss)) # it is dictionary not set because set is created using set() function

# Q6
# Create an empty dictionary allow 4 friend to enter their favourite languages as the value and use key as their name. Assume that the name are unique.

ff ={
    "rahul" : "python",
    "anshu" : "c++",
    "rohan" : "java"
}
print(ff) # print the dictionary

# Q7
# If the name of two friend are same what will happen to a program In question 6

ff_1 ={
    "anshu" : "python",
    "anshu" : "c++",
    "anshu" : "java"
}
print(ff_1)  # if the name of two friend are same then the last value will be considered and previous value will be overwritten

# Q8
# If languages of two friends are same what will happen to the program in Question 6

ff ={
    "rahul" : "python",
    "anshu" : "c++",
    "rohan" : "c++ "
}
print(ff)  # if languages of two friends are same then it will not create any problem because key are different

# Q9
# Can you change the value inside a list Which it contained in a set s,  s = {8,7,12,"anshu",[1,2]}

# s = {8,7,12,"anshu",[1,2]}  # it will give error because set cannot contain mutable data types like list, dictionary etc.
s = {8,7,12,"anshu",(1,2)}  # we can use tuple instead of list because tuple is immutable
print(s)