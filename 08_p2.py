# Q5
# Write a python function to print first nline of the following pattern:
# ***
# **
# *    for n = 3

def patt(number):
    for i in range(number,0,-1):
        print("*"*i,end="")
        print("")

p = int(input("Enter number : "))
patt(p)

# Q6
# Write a python function which convert inches to centimetres.


def I_to_C(ii):
    return ii*2.54

cc = I_to_C(2)
print(f"The given inches => {2}  in cm is => {cc}")

# Q7
# Write a python function to remove a given word from a list ad strip it at the same time.

l = [ "lion" , "Rohan" , "Shubham" , "anshu" , "aman" ]

def LF(l,word):
    n = []
    for i in l:
        if not(i==word):
            n.append(i.strip(word))
    return n

print(LF(l,"an"))


# Q8
# Write a python function to print multiplication table of a given number Advance using .

def table_of(T,i=1):
    if( i == 11):
        return
    print(f"{T} X {i} = {T*i}")
    i+=1
    table_of(T,i)

table_of(2)