# Q6
# Write a programme to calculate the factorial of a given number using for loop.

num = int(input("Enter a number to find factorial: "))
fac = 1
for i in range(num,0,-1):
    if(i==1):
        fac = fac * 1
    else:
        fac = fac * (i*1) 

print(f"the factorial of {num} is {fac}")

# Q7
# Write a programme to print the following star pattern
#     *
#   * * *
# * * * * * for n = 3

star = int(input("Enter the number of rows: "))

for i in range(1,star+1):
    print(" "*(star-i),end=" ")
    print("*"*(2*i-1),end="")
    print("")


# Q8
# Write a programme to print following star pattern.
# *
# * *
# * * * for n = 3

for i in range(3):
    for j in range(i+1):
        print("*",end=" ")
    print("")

# another method..

for i in range(1,star+1):
    print("*"*i,end=" ")
    print(" ")


# Q9
# Write a programme to print the following star pattern
# * * *
# *   *
# * * * for n =3

for i in range(3):
    for j in range(3):
        if(j==1 and i==1):
            print(" ",end=" ")
            continue
        print("*",end=" ")
    print("")

# another method..

for i in range(1,star+1):
    if(i==1 or i==star):
        print("*"*star,end="")
    else:
        print("*",end="")
        print(" "*(star-2),end="")
        print("*",end="")
    print(" ")

# Q10
# Write a programme to print multiplication table of N using for loop in reverse order.

table = int(input("Enter the number, Which you want a table for it: "))

for i in range(10,0,-1):
    print(f"{table} X {i} = {table*i}")
