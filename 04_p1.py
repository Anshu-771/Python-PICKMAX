# Lists and Tuples

# lists
# Lists are mutable, means you can change their content.
# Lists are defined using square brackets [].
# Lists can contain elements of different data types.
# List are ordered, meaning the items have a defined order, and that order will not change.
# lists allow duplicate values.
# Lists are dynamic in size, meaning you can add or remove items after the list has been created.
# List support various methods for manipulation like append(), remove(), pop(), sort(), reverse(), etc. 
# Lists are iterable, meaning you can loop through the items in a list using loops like for and while.
# Lists can be nested, meaning you can have lists within lists.
# Lists are indexed, meaning you can access items in a list using their index position.
# Lists can be sliced, meaning you can extract a portion of a list using slicing syntax.
# Lists can be concatenated, meaning you can combine two or more lists using the + operator.

li = [1 ,"anshu",3.4,"apple",True,"babu ram",8,False]
print(li)
print(type(li))
print(li[1])
print(li[len(li)-1])
print(li[0])
print(li[1:3]) # slicing
print(li[::2]) # slicing and jumping

lii =[45,9056,12,0,23,19,78]

lii.sort() # sorting, it will arrange in ascending order
print(lii)
lii.reverse() # reversing the list
print(lii)
li.append("i'am new!!") # adding new element at the end of the list
print(li)
li.insert(2,"aman") # adding new element at specfic index
print(li)
li_5 = li.pop(4) # removing element at specific index and also return the removed element
print(li_5)
li.remove("babu ram") # removing specific element
print(li)


# tuples
# Tuples are immutable, means you cannot change their content after creation.
# Tuples are defined using parentheses ().
# Tuples can contain elements of different data types.
# Tuples are ordered, meaning the items have a defined order, and that order will not change.
# Tuples allow duplicate values.
# Tuples are dynamic in size, meaning you can create tuples of different sizes.
# Tuples support various methods for manipulation like count(), index(), etc.
# Tuples are iterable, meaning you can loop through the items in a tuple using loops like for and while.

tu = (1,2,3,"anshu",4.5,True,"apple",False)

print(tu)
print(type(tu))
print(tu[1])
print(tu[len(li)-1])
print(tu[0])
print(tu[1:3]) # slicing
print(tu[::2])

tu2 = tu.count(77) # it will return the count of the element in the tuple
print(tu2)
tu3 = tu.index("anshu") # it will return the index of the first occurence of the element
print(tu3)