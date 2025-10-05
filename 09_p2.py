
# Q6
# Write a program to mine a log file and find out whether it contains ‘python’.

with open("py.txt" , "r") as f:
    r = f.read()
    print(type(r))
   
if("python" in r):
    print("YES")
else:
    print("NO")

# Q7
# Write a program to find out the line number where python is present from ques 6.

with open("py.txt" , "r") as f:
    rr = f.readlines()
    print(type(r))

r_line = 1
for i in rr:
    if("python" in i):
        print("the python word is present at line : ",r_line)
        break
    r_line += 1
else:
    print("Not present so we cannot detect it....")
    

# Q8
# Write a program to make a copy of a text file “this. txt”

with open("this.txt","r") as f:
    q8_1 = f.read()
    with open("this_copy.txt","w") as ff:
        ff.write(q8_1)

# Q9
# Write a program to find out whether a file is identical & matches the content of another file.

with open("this.txt","r") as f:
    q9_1 = f.read()

with open("this_copy.txt","r") as f:
    q9_2 = f.read()

if(q9_1 == q9_2):
    print("same same")
else:
    print("same same but diffirent")

# Q10
# Write a program to wipe out the content of a file using python.

with open("file3.txt", "w") as f:
    f.write("")

# Q11
# Write a python program to rename a file to “renamed_by_ python.txt.