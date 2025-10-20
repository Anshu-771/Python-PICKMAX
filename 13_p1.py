from functools import reduce

# Q1 Virtual Environment

# Q2 format string out-dated

print("hello my name is {}, I score {} in my exams for more information contect on this : {}".format("Anshu",84.5,"999999999"))

# Q3 list have multiplication table of 7 convert in vertical way...

list1 =["7","14","21","28","35","42","49","56","63","70"]

result = "\n".join(list1)

print(result)

# Q4 fliter list of number divisible by 5

def D5(x):
    if(x%5==0):
        return x


list2 = [1,3,5,10,8,14,20]

R = list(filter(D5,list2))

print(R)

# Q5 find largest number from list2 using reduce

def large(z,y):
    if(z>y):
        return z
    else:
        return y
    
answer = reduce(large,list2)

print(answer)