import math 

# Q1
# Create a class “Programmer” for storing information of few programmers
# working at Microsoft.

class Microsoft:
    name = ""
    position = ""
    salary = None

    def __init__(self,name,position,salary):
        self.name = name
        self.position = position
        self.salary = salary

    
    def display(self):
        print(f"hello!!!, my name is {self.name} i'work in microsoft at {self.position} level and i got salary approx to this => {self.salary}")


anshu = Microsoft("Anshu Kumar","Top","12000")
anshu.display() 



# Q2
# Write a class “Calculator” capable of finding square, cube and square root of a
# number.


class calculator:
    number = None

    def __init__(self):
        n = int(input("Enter the number : "))
        self.number = n

    def sn(self):
        return (self.number**2)

    def cn(self):
        return (self.number**3)
    
    def srn(self):
        return math.sqrt(self.number) 
    
    @staticmethod
    def outer():
        print("\n\n\t Nice to meet you, i am Calculator Class \n\n")

obj1 = calculator()

print(f"Square of a Number => {obj1.sn()}")
print(f"Cube of a Number => {obj1.cn()}")
print(f"Square Root of a Number => {obj1.srn():.2f}")


# Q3
# Create a class with a class attribute a; create an object from it and set ‘a’
# directly using ‘object.a = 0’. Does this change the class attribute?

class o:
    a = 4
# If instance variable and class variable are same the higher priority give to the instance variable
obj2 = o()
print(obj2.a) # Display class attribute because it Instance Attribute is not present a=4
obj2.a = 10 # Instance attribute is set
print(obj2.a) # display the instance attribute because instance attribute is present a=10
obj3 = o() 
print(obj3.a) # Same for this we have not defined the instance attribute So it displays the class attribute a=4

# Q4
# Add a static method in problem 2, to greet the user with hello.

obj1.outer()
# Q5
# Write a Class ‘Train’ which has methods to book a ticket, get status (no of seats)
# and get fare information of train running under Indian Railways.

class train:
    seats = 450
    status = False
    number_of_seat_alot = None
    book_by = ""

    def book_a_ticket(self):
        name = input("Enter you Name : ")
        s = int(input("Number of seat you want to book : "))
        train.seats = train.seats - s
        self.book_by = name
        self.number_of_seat_alot = s 
        if(train.seats>=0):
            self.status = True
        else:
            train.seats = train.seats + s

    def get_status(self):
        if(self.status == True):
            print("seat is aloted ....")
            print("Number seat aloted is => ",self.number_of_seat_alot)
            print("By Name => ",self.book_by)
        else:
            print("seat was not aloted !!!! ")

    @staticmethod
    def seat_left():
        print("seats are left is => ",train.seats)


user1 = train()
user2 = train()
user1.book_a_ticket()
train.seat_left()
user2.book_a_ticket()
train.seat_left()
user1.get_status()
user2.get_status()



# Q6
# Can you change the self-parameter inside a class to something else (say
# “harry”). Try changing self to “slf” or “harry” and see the effects.

# Ans| We can change It to anything But we not prefer Because it is easy to identify Where we have calling using Our object in class .