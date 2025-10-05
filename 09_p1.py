import random
# Q1
# Write a program to read the text from a given file "poems.txt" and find out whether it contains the word Anshu.

with open("poems.txt") as f:
    i = f.read()
    if("Anshu" in i):
        print("yes it's")
    else:
        print("No")
    
    
# Q2
# The game() function in a program lets a user play a game and returns the score
# as an integer. You need to read a file ‘Hi-score.txt’ which is either blank or
# contains the previous Hi-score. You need to write a program to update the Hiscore whenever the game() function breaks the Hi-score.

def game():
    return random.choice([1,2,3,4,5,6,7,8,9])


with open("Hi-score.txt") as j:
    i = j.read()
    user = str(game())
    if(user >= i or i == "" ):
        with open("Hi-score.txt" , "w") as k:
            k.write(user)
            print(" The high score value was greater From the value present in a file")
    else:
        print("High score value was smaller then value present in a file")


# Q3
# Write a program to generate multiplication tables from 2 to 20 and write it to the different files. Place these files in a folder for a 13 – year old.

def mm(T):
    ok = ""
    if(T == 21):
        return
    for i in range(1,10+1):
        ok += f"{T} X {i} = {T*i}\n"
    
    with open("table.txt","a") as f:     # with open(f"tables/table-{T}.txt","w") as f:   this will creat sperate folder with tables file of 2 to 20.
        f.write(ok)
        f.write("\n")
    mm(T+1)                              # if i put this line into file write table will be print in 20 to 2 reverse order (recursion)

mm(2)


# Q4
# A file contains a word “Donkey” multiple times. You need to write a program which replace this word with ##### by updating the same file.

with open("file1.txt") as f:
    r = f.read()
    with open("file1.txt" , "w") as j:
        j.write(r.replace("Donkey","#####"))

# Q5
# Repeat program 4 for a list of such words to be censored.

censord = ["Donkey","Monkey","Zabra"]

with open("file2.txt") as f:
    prv_r = f.read()
    
for i in censord:
    prv_r = prv_r.replace(i,"#"*len(i))

new_r = prv_r

with open("file2.txt","w") as f:
    f.write(new_r)