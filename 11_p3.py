# Q4
# Write a class ‘Complex’ to represent complex numbers, along with overloaded
# operators ‘+’ and ‘*’ which adds and multiplies them.


class complex:


    def __init__(self,real,imaginary):
        self.real = real
        self.imaginary = imaginary

    def __add__(self,Complex_2):
        return complex(self.real+Complex_2.real,self.imaginary+Complex_2.imaginary)
        # return f" {self.real+Complex_2.real} + {self.imaginary+Complex_2.imaginary}i"

    def __mul__(self,Complex_2):
        return complex((self.real*Complex_2.real - self.imaginary*Complex_2.imaginary),(self.real*Complex_2.imaginary + self.imaginary*Complex_2.real))

    def __str__(self):
        return f"{self.real} + {self.imaginary}i"

c1 = complex(1,2)
c2 = complex(3,4)
c3 = c1.__add__(c2)
c4 = c1.__mul__(c2)
print(c3) # same comment as below
print(c4) # def __str__(self) use this  to print object i a way without this i will print i some main like content with this it will print in string-way



# Q5
# Write a class vector representing a vector of n dimensions. Overload the + and *
# operator which calculates the sum and the dot(.) product of them.

class _2D_vector_:
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def show(self):
        print("X Axis co-ordinates : ",self.x)
        print("Y Axis co-ordinates : ",self.y)

    def __add__(self,v2):
        return _2D_vector_(self.x + v2.x , self.y + v2.y )
    
    def __str__(self):
        return f"{self.x}x + {self.y}y "             # Q6 Answer

    def __mul__(self,v2):
        dot = (self.x*v2.x) + (self.y*v2.y)
        return f"dot product is => {dot}"

    def __len__(self):                               # Q7 Answer
        return 2


class _3D_vector_(_2D_vector_):
    def __init__(self,x,y,z):
        super().__init__(x,y)
        self.z = z

    def show(self):
        super().show()
        print("Z Axis co-ordinates : ",self.z)
    
    def __add__(self,v2):
        return _3D_vector_(self.x + v2.x , self.y + v2.y , self.z + v2.z )
    
    def __str__(self):
        return f"{self.x}x + {self.y}y + {self.z}z "    # Q6 Answer
    
    def __mul__(self,v2):
        dot = (self.x*v2.x) + (self.y*v2.y) + (self.z*v2.z)
        return f"dot product is => {dot}"

    def __len__(self):                                 # Q7 Answer
        return 3


ob1 = _2D_vector_(2,3)
ob2 = _2D_vector_(4,6)
ob3 = ob1.__add__(ob2)
print(ob3)
print(ob1.__mul__(ob2))
print("lenght of 2D-Vector is =>",len(ob3))
ob4 = _3D_vector_(2,3,4)
ob5 = _3D_vector_(4,6,4)
ob6 = ob4.__add__(ob5)
print(ob6)
print(ob4.__mul__(ob5))
print("lenght of 3D-Vector is =>",len(ob6))


# Q6
# Write __str__() method to print the vector as follows: 7x + 8y +10z Assume vector of dimension 3 for this problem.

# solve in Q5

# Q7
# Override the __len__() method on vector of problem 5 to display the dimension of thevector.

# solve in Q5