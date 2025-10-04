import random

game_list = ["snake","gun","water"]

def SWG(data , user_data):
    computer_data = random.choice(data)
    if not(user_data in data):
        print("\t\tInvalid choice....")
        return -1
    if(user_data == computer_data):
        print("\t\tDraw!!!, same choice you noob...." )
        return -1
    else:
        if(user_data=="snake" and computer_data=="water") or (user_data=="water" and computer_data=="gun") or (user_data=="gun" and computer_data=="snake"):
            print(f"\t\tuser-win~  || user choice => {user_data} ||  computer choice => {computer_data} ||")
            return 0
        else:
            print(f"\t\tcomputer-win~ || user choice => {user_data} ||  computer choice => {computer_data} ||")
            return 1
    


isWin = False
c=0
u=0
 
while(isWin == False):
    user = input(f"Enter the value from this list =>{game_list} ==== ")

    response = SWG(game_list,user.lower())

    if(response == 1):
        c+=1
    elif(response == 0):
        u+=1
    
    if(u==5 or c==5):
        isWin = True

if(u==5):
    print(f"\n\n\tUser win the game, Congratulation....\n\t|| U -> {u} || C -> {c} ||")
else:
    print(f"\n\n\tcomputer win the game, Better luck next time....\n\t|| U -> {u} || C -> {c} ||")