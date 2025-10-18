# Q1

try:
    f1 = open("file1.txt")
    f2 = open("file2.txt")
    f4 = open("file4.txt")

except FileNotFoundError as e:
    print(e)

print("Ok thanks")


# Q2

l = [11,22,33,44,55,66,77]

for i,item in enumerate(l):
    if(i in [3-1,5-1,7-1]):
        print(f"position => {i+1} and element => {item}")

# Q3

user1 = int(input("Enter the number : "))

Multi = [user1*i for i in range(1,10+1)]

print(Multi)


# Q4

n1 = int(input("Enter the First Number : "))
n2 = int(input("Enter the Second Number : "))
try:
    r = n1/n2
    print(f"Answer => {r}")

except ZeroDivisionError:
    print("infinite")

print("Have a Nice Day...")

# if(n2 == 0):                                          # using raise keyword
#     raise ZeroDivisionError("infinite")
# else:
#      r = n1/n2
#      print(f"Answer => {r}")

# print("Have a Nice Day...")

# Q5

with open("t1.txt" , "w") as f:
    f.write(str(Multi))

