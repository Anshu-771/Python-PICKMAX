# Q1
# Create a class (2-D vector) and use it to create another class representing a 3-D vector.


class _2D_vector_:
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def show(self):
        print("X Axis co-ordinates : ",self.x)
        print("Y Axis co-ordinates : ",self.y)


class _3D_vector_(_2D_vector_):
    def __init__(self,x,y,z):
        super().__init__(x,y)
        self.z = z

    def show(self):
        super().show()
        print("Z Axis co-ordinates : ",self.z)


obj1 = _2D_vector_(2,5)
obj1.show()
obj2 = _3D_vector_(6,8,7)
obj2.show()
    

# Q2
# Create a class ‘Pets’ from a class ‘Animals’ and further create a class ‘Dog’ from
# ‘Pets’. Add a method ‘bark’ to class ‘Dog’.


class Animal:
    
    def __init__(self):
        print("I am top level class, NOT DEPENDENT ")

class Pets(Animal):
    
    def __init__(self):
        super().__init__()
        print("I am middle level class, Derived from top-level-class, DEPENDENT ")

class Dog(Pets):
    
    def __init__(self):
        super().__init__()
        print("I am lower level class, Derived from middle-level-class, DEPENDENT ")

    def bark(self):
        print("bhuk-bhuk bhuk-bhuk!! ")

obj3 = Animal()
obj4 = Pets()
obj5 = Dog()
obj5.bark()

# Q3
# Create a class ‘Employee’ and add salary and increment properties to it.
# Write a method ‘salaryAfterIncrement’ method with a @property decorator with a setter
# which changes the value of increment based on the salary.

class Employee:

    def __init__(self,name,salary):
        self.name = name
        self.salary = salary
        self.increment = 0

    def show(self):
        print("Name : ",self.name)
        print("Total-Salary : ",self.salary)
        print("Increment : ",self.increment)

    @property
    def salaryAfterIncrement(self):
        print(f"before increment => {self.salary - self.increment} and After increment => {self.salary}")

    @salaryAfterIncrement.setter
    def salaryAfterIncrement(self,TS):
        self.increment = TS - self.salary
        self.salary = TS
        

e1 = Employee("Anshu",120000)
e1.show()
e1.salaryAfterIncrement = 180000 # # invokes the setter
e1.salaryAfterIncrement      # invokes the getter (no parentheses) or print(e1.salaryAfterIncrement) (Instead of printing inside the @property, you could return a string:)
e1.show()



# Q4
# Write a class ‘Complex’ to represent complex numbers, along with overloaded
# operators ‘+’ and ‘*’ which adds and multiplies them.



# Q5
# Write a class vector representing a vector of n dimensions. Overload the + and *
# operator which calculates the sum and the dot(.) product of them.
# Q6
# Write __str__() method to print the vector as follows: 7i + 8j +10k Assume vector of dimension 3 for this problem.
# Q7
# Override the __len__() method on vector of problem 5 to display the dimension of thevector.