# Q1
# Write a program using function to find great test of three numbers.

def gt(A,B,C):
    if A>B and A>C:
        print(f"the value you first enter is greater that is : {A}")
    elif B>A and B>C:
        print(f"the value you second enter is greater that is : {B}") 
    else:
         print(f"the value you third enter is greater that is : {C}")

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))
gt(a,b,c)

# Q2
# Write a program Using function to convert Celsius to Fahrenheit.

def CtoF(cell):
    fell = ((cell * 9)/5) + 32
    return fell

cc = float(input("Enter the temperature in Celsius : "))
ff = CtoF(cc)
print(f"The temperature you enter in Celsius => {cc} Will be in Fahrenheit is => {ff}")

# Q3
# How do you prevent a python print function to print a new line at the end.

print("A",end="") # using this end=""
print("N",end="")
print("S",end="")
print("H",end="")
print("U",end="")
print(" ")

# Q4
# Write a recursion function to calculate sum of first and natural numbers.

summ = 0
def ns(nut):
    if(nut<=0):
        print("invalid number!! ")
    elif(nut==1):
        return 1
    else:
        summ = nut + ns(nut-1)
        return summ

n = int(input("Enter a number: "))
st  = ns(n)
print(f"Sum of Nutural numbers from 1 to {n} is {st} ")