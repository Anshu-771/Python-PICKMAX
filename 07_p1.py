# Q1
# Write a programme to print a multiplication table of given number using for loop.

table_of = int(input("Enter the number, Which you want a table for it: "))

for i in range(1,10+1):
    print(f"{table_of} X {i} = {table_of*i}")


# Q2
# Write a programme to Greet all the person name stored in a list L and W start with S.
# l = ["Anshu", "Sonal", "Rohit", "Sonal", "Aman", "Sakshi"]

l = ["Anshu", "Sonal", "Rohit", "Sana", "Aman", "Sakshi"]

for i in l:
    if(i.startswith("S")):
        print(f"Hello {i}, i am python program")

# Q3
# Attempt problem one using while loop.

i = 1
while(i<=10):
    print(f"{table_of} X {i} = {table_of*i}")
    i+=1

# Q4
# Write a programme to find whether a given number is prime or not.

num = int(input("Enter your number to find that it's prime or not: "))
for i in range(1,num+1):
    if(num%i==0 and i!=1 and i!=num):
        print(f"{num } is not a prime number.....")
        break
    if(i==num):
        print(f"{num} is a prime number.....")

for i in range(1,num+1):
    if(num%i==0 and i!=1 and i!=num):
        print(f"{num } is not a prime number.....")
        break
else:
    print(f"{num} is a prime number.....")


# Q5
# Write a programme to find the sum of first and natural number using while loop.

nutural_num = int(input("Enter a number: "))

i = 1
add = 0
while(i<=nutural_num):
    add+=i
    i+=1
print(f"The sum of natural number of => {nutural_num}  is => {add}")
