# Object-Oriented Programming (OOP) in Python: Comprehensive Notes
# These comments provide a complete overview of OOP concepts in Python.

# 1. INTRODUCTION TO OOP
# OOP is a programming paradigm based on "objects" which can contain data (attributes) and code (methods).
# Key principles: Encapsulation, Inheritance, Polymorphism, Abstraction.
# Python supports OOP natively, allowing classes and objects to model real-world entities.
# Benefits: Modularity, reusability, maintainability, and easier debugging.

# 2. CLASSES AND OBJECTS
# A class is a blueprint for creating objects (instances).
# An object is an instance of a class with actual values.
# Syntax: Use 'class' keyword to define a class.

# Example: Defining a simple class
# class Dog:
#     pass  # Empty class (placeholder)

# Creating an object
# my_dog = Dog()  # Instance of Dog class

# 3. ATTRIBUTES (DATA MEMBERS)
# Attributes store data for objects. They can be class attributes (shared) or instance attributes (unique).
# Class attributes: Defined directly in the class body.
# Instance attributes: Defined in methods like __init__.

# Example: Class and instance attributes
# class Dog:
#     species = 'Canine'  # Class attribute (shared by all instances)
#
#     def __init__(self, name, age):  # Constructor method
#         self.name = name  # Instance attribute
#         self.age = age    # Instance attribute

# Accessing attributes
# my_dog = Dog('Buddy', 5)
# print(my_dog.name)          # Output: Buddy
# print(Dog.species)          # Output: Canine (class attribute)
# print(my_dog.species)       # Output: Canine (accessible via instance)

# 4. METHODS (FUNCTION MEMBERS)
# Methods are functions defined inside a class that operate on objects.
# The first parameter is always 'self' (refers to the instance).
# Special methods: Start and end with double underscores (dunder methods), e.g., __init__, __str__.

# Example: Defining methods
# class Dog:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def bark(self):  # Instance method
#         return f"{self.name} says Woof!"
#
#     @classmethod
#     def from_birth_year(cls, name, birth_year):  # Class method (uses 'cls')
#         age = 2023 - birth_year  # Assuming current year is 2023
#         return cls(name, age)
#
#     @staticmethod
#     def is_adult(age):  # Static method (no 'self' or 'cls')
#         return age > 1

# Using methods
# my_dog = Dog('Buddy', 5)
# print(my_dog.bark())                # Output: Buddy says Woof!
# new_dog = Dog.from_birth_year('Max', 2020)  # Using class method
# print(Dog.is_adult(2))              # Output: True (static method)

# 5. CONSTRUCTOR (__init__)
# __init__ is a special method called when an object is created.
# It initializes instance attributes.
# It's not mandatory but commonly used.

# Example: See above in section 3 and 4.

# 6. ENCAPSULATION
# Encapsulation hides internal details and exposes only necessary parts.
# In Python, use naming conventions:
# - Public: No underscore (e.g., attribute)
# - Protected: Single underscore (e.g., _attribute) – convention, not enforced
# - Private: Double underscore (e.g., __attribute) – Name mangling (e.g., _Class__attribute)

# Example: Encapsulation with private attributes
# class BankAccount:
#     def __init__(self, balance):
#         self.__balance = balance  # Private attribute
#
#     def deposit(self, amount):
#         if amount > 0:
#             self.__balance += amount
#
#     def get_balance(self):  # Getter method
#         return self.__balance

# Usage
# account = BankAccount(100)
# account.deposit(50)
# print(account.get_balance())  # Output: 150
# # print(account.__balance)    # AttributeError (private)

# 7. INHERITANCE
# Inheritance allows a class (child/subclass) to inherit attributes and methods from another class (parent/superclass).
# Promotes code reuse.
# Syntax: class Child(Parent):

# Types:
# - Single inheritance: One parent.
# - Multiple inheritance: Multiple parents (Python supports it).
# - Multilevel inheritance: Chain of inheritance.

# Example: Single inheritance
# class Animal:  # Parent class
#     def __init__(self, name):
#         self.name = name
#
#     def eat(self):
#         return f"{self.name} is eating."

# class Dog(Animal):  # Child class
#     def bark(self):
#         return f"{self.name} says Woof!"

# Usage
# my_dog = Dog('Buddy')
# print(my_dog.eat())   # Output: Buddy is eating. (inherited)
# print(my_dog.bark())  # Output: Buddy says Woof!

# Overriding methods
# class Dog(Animal):
#     def eat(self):  # Overrides parent's eat()
#         return f"{self.name} is eating bones."

# Using super() to call parent methods
# class Dog(Animal):
#     def __init__(self, name, breed):
#         super().__init__(name)  # Call parent's __init__
#         self.breed = breed

# 8. POLYMORPHISM
# Polymorphism allows objects of different classes to be treated as objects of a common superclass.
# Achieved through method overriding or operator overloading.
# Enables "one interface, multiple implementations."

# Example: Polymorphism with method overriding
# class Cat(Animal):
#     def eat(self):
#         return f"{self.name} is eating fish."

# def animal_eat(animal):  # Polymorphic function
#     print(animal.eat())

# animal_eat(Dog('Buddy'))  # Output: Buddy is eating bones.
# animal_eat(Cat('Whiskers'))  # Output: Whiskers is eating fish.

# Operator overloading (using dunder methods)
# class Point:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#
#     def __add__(self, other):  # Overload + operator
#         return Point(self.x + other.x, self.y + other.y)

# p1 = Point(1, 2)
# p2 = Point(3, 4)
# p3 = p1 + p2  # Calls __add__

# 9. ABSTRACTION
# Abstraction hides complex implementation details and shows only essential features.
# Use abstract base classes (ABC) from abc module.
# Abstract methods must be implemented by subclasses.

# Example: Abstraction
# from abc import ABC, abstractmethod
#
# class Shape(ABC):  # Abstract base class
#     @abstractmethod
#     def area(self):  # Abstract method
#         pass
#
# class Rectangle(Shape):
#     def __init__(self, length, width):
#         self.length = length
#         self.width = width
#
#     def area(self):  # Implements abstract method
#         return self.length * self.width

# Usage
# rect = Rectangle(5, 3)
# print(rect.area())  # Output: 15
# # shape = Shape()   # TypeError: Can't instantiate abstract class

# 10. CLASS VARIABLES VS INSTANCE VARIABLES
# Class variables: Shared among all instances (defined outside methods).
# Instance variables: Unique to each instance (defined in __init__).

# Example: See section 3.

# 11. MAGIC METHODS (DUNDER METHODS)
# Special methods for customizing behavior:
# - __init__: Constructor
# - __str__: String representation (for print())
# - __repr__: Official string representation (for debugging)
# - __len__: For len() function
# - __getitem__: For indexing (e.g., obj[key])

# Example: __str__ and __repr__
# class Dog:
#     def __init__(self, name):
#         self.name = name
#
#     def __str__(self):
#         return f"Dog named {self.name}"
#
#     def __repr__(self):
#         return f"Dog('{self.name}')"

# my_dog = Dog('Buddy')
# print(my_dog)        # Output: Dog named Buddy (__str__)
# print(repr(my_dog))  # Output: Dog('Buddy') (__repr__)

# 12. PROPERTY DECORATORS
# Properties allow getter, setter, and deleter methods for attributes.
# Use @property for controlled access.

# Example: Properties
# class Circle:
#     def __init__(self, radius):
#         self._radius = radius
#
#     @property
#     def radius(self):  # Getter
#         return self._radius
#
#     @radius.setter
#     def radius(self, value):  # Setter
#         if value < 0:
#             raise ValueError("Radius cannot be negative")
#         self._radius = value
#
#     @property
#     def area(self):  # Computed property
#         return 3.14159 * self._radius ** 2

# circle = Circle(5)
# print(circle.area)  # Output: ~78.54
# circle.radius = 10  # Uses setter

# 13. MULTIPLE INHERITANCE AND MRO
# Python supports multiple inheritance.
# Method Resolution Order (MRO): Determines the order of method lookup (C3 linearization).
# Use __mro__ or mro() to view.

# Example: Multiple inheritance
# class A:
#     def method(self):
#         print("A method")
#
# class B:
#     def method(self):
#         print("B method")
#
# class C(A, B):  # Inherits from A and B
#     pass

# c = C()
# c.method()          # Output: A method (A before B in MRO)
# print(C.__mro__)    # Shows MRO: C -> A -> B -> object

# 14. ERROR HANDLING IN OOP
# Use exceptions in classes for robust code.
# Custom exceptions: Inherit from Exception or subclasses.

# Example: Custom exception
# class InvalidAgeError(Exception):
#     pass
#
# class Dog:
#     def __init__(self, age):
#         if age < 0:
#             raise InvalidAgeError("Age cannot be negative")
#         self.age = age

# 15. BEST PRACTICES
# - Follow PEP 8: Class names CamelCase, methods/attributes lowercase_with_underscores.
# - Use encapsulation to protect data.
# - Favor composition over inheritance (has-a vs is-a).
# - Keep classes small and focused (Single Responsibility Principle).
# - Use type hints for better readability (e.g., from typing import List).
# - Document classes/methods with docstrings.
# - Avoid overusing multiple inheritance to prevent complexity.

# 16. EXAMPLE: COMPLETE OOP WORKFLOW
# from abc import ABC, abstractmethod
#
# class Animal(ABC):
#     def __init__(self, name):
#         self.name = name
#
#     @abstractmethod
#     def make_sound(self):
#         pass
#
# class Dog(Animal):
#     def make_sound(self):
#         return f"{self.name} says Woof!"
#
# class Cat(Animal):
#     def make_sound(self):
#         return f"{self.name} says Meow!"
#
# # Usage
# animals = [Dog('Buddy'), Cat('Whiskers')]
# for animal in animals:
#     print(animal.make_sound())  # Polymorphism in action

# End of OOP Notes