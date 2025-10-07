import random 

def play_game(n,a):
    if(n<1 or n>500):
        print("Invalid Number Enter :  || Out Of Range ||")
        return False
    if(n == a):
        print("Matched!!!")
        return True
    if(n > a):
        print("you Number is \"Greater\" then the Then The Expected Value")
    if(n < a):
        print("you Number is \"Smaller\" then the Then The Expected Value")
    return False
    
    
i = False
auto_num = None

while(i != True ):
    num = int(input("Enter the Number [Between 1 to 500 ] : "))
    if(auto_num == None ):
        auto_num = random.randint(1,500)
    i = play_game(num,auto_num)
else:
    print("\nThanks For Playing....\nHave a Nice day....")
