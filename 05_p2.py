# Dictionary And sets in python


# Dictionary
# Dictionary is a collection of key value pair
# key must be unique and value can be duplicate
# Dictionary is mutable means we can change the value of a key
# Dictionary is unordered means the items are not in a defined order
# Dictionary is defined using curly braces {}
# Dictionary is dynamic in size means we can add or remove items after the dictionary has been created
# Dictionary support various methods for manipulation like keys(), values(), items(), get(), update(), pop(), popitem(), clear(), etc.
# Dictionary is iterable means we can loop through the items in a dictionary using loops like for and while
# Dictionary can be nested means we can have dictionary within dictionary
# Dictionary is indexed means we can access items in a dictionary using their key
# Dictionary can be concatenated means we can combine two or more dictionaries using the update() method
# Dictionary can be sliced means we can extract a portion of a dictionary using slicing syntax
# Dictionary can be copied means we can create a copy of a dictionary using the copy() method
# Dictionary can be created using the dict() function.

dict1 = {
    "name" : "anshu",
    "age" : 20,
    "city" : "delhi",
    "is_student" : True,
    "marks" : [45,67,89],
    "fav_tuple" : (1,2,3),
    1 : "one",
    2.5 : "two point five"
}
print(dict1)
print(type(dict1))
print(dict1["name"]) # accessing value using key 
print(dict1["marks"][1]) # accessing list inside dictionary
print(dict1["fav_tuple"][2]) # accessing tuple inside dictionary
print(dict1[1]) # accessing int key

# sets
# Set is a collection of unique items
# Set is mutable means we can change the value of a set
# Set is unordered means the items are not in a defined order
# Set is defined using curly braces {} or the set() function
# Set is dynamic in size means we can add or remove items after the set has been created
# Set support various methods for manipulation like add(), remove(), pop(), clear(), union(), intersection(), difference(), symmetric_difference(), issubset(), issuperset(), etc.
# Set is iterable means we can loop through the items in a set using loops like for and while
# Set can be nested means we can have set within set
# Set is not indexed means we cannot access items in a set using their index
# Set cannot be sliced means we cannot extract a portion of a set using slicing syntax
# Set cannot be concatenated means we cannot combine two or more sets using the + operator
# Set can be copied means we can create a copy of a set using the copy() method
# Set can be created using the set() function.
# Set cannot contain mutable data types like list, dictionary etc.
# Set can contain multiple data types like int, float, string, tuple etc.
# Set allow mathematical set operations like union, intersection, difference, symmetric difference etc.
# Set is faster than list and dictionary for membership testing because it uses hash table internally.
# Set is used to remove duplicate items from a list or tuple.

s = {1,2,3,4,5,5,4,3,2,1} # duplicate values will be removed
print(s)
print(type(s))
s.add(6) # adding new item to set
print(s)
s.remove(3) # removing item from set
print(s)