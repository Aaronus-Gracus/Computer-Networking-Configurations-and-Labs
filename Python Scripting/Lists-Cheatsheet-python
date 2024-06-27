# LISTS / TUPLES / SETS

# Lists can contain any data type in Python! For example,
# this list contains a string, integer, boolean, and float.
# mixed_list_common = ["Mia", 27, False, 0.5]


# Mutable
courses = ['History', 'Math', 'Physics', 'CompSci']

print(courses)              # Output: ['History', 'Math', 'Physics', 'CompSci']
print(len(courses))         # Output: 4  | 4 is how many variables are in list
print(courses[0])           # Prints first index in list | Output: History
print(courses[3])           # Prints 3rd index in list | Output: CompSci
print(courses[-1])          # Prints last index in list | Output: CompSci | more convenient

# Slicing:
print(courses[0:2])  | print(courses[:2])       # Prints index 0 to 2 | Output: ['History', 'Math']
print(courses[2:])                              # Output: ['Physics', 'CompSci']



# List Methods

# .append()
courses = ['History', 'Math', 'Physics', 'CompSci']

my_list = [5, 8]
my_list.append(16)
print(my_list)              #Output: [5, 8, 16]

courses.append('Art')       # .append('Art') adds Art to the course list
print(courses)              # Output: ['History', 'Math', 'Physics', 'CompSci', 'Art']


# .insert()
courses.insert(0, 'Art')        # .insert() takes two parameters: .insert(index_location, 'value')
print(courses)                 # Output: ['Art', 'History', 'Math', 'Physics', 'CompSci']
                                # Art added at index 0

#list.insert(i, x)
#Insert x into list before position i.

my_list3 = [5, 8]
my_list3.insert(1, 1.7)
print(my_list3)        #Output: [5, 1.7, 8]

# .insert() does NOT work when adding another list to the main courses list
# You have to use the below .extend() method

# .extend()
# courses = ['History', 'Math', 'Physics', 'CompSci']
# courses_2 = ['Art', 'Education']

# courses.extend(courses_2)
# print(courses)                  # Output: ['History', 'Math', 'Physics', 'CompSci', 'Art', 'Education']


my_list2 = [5, 8]
my_list2.extend([4, 12])
print(my_list2)      #Output: [5, 8, 4, 12]

# .remove()
# courses = ['History', 'Math', 'Physics', 'CompSci']

# courses.remove('Math')
# print(courses)              # Output: ['History', 'Physics', 'CompSci'] | Notice 'Math' is removed


# list.remove(x)
# Remove first item from list with value x.

my_list4 = [5, 8, 14]
my_list4.remove(8)
print(my_list4)      #Output: # [5, 14]


# .pop()
# Also removes the LAST item from list
courses = ['History', 'Math', 'Physics', 'CompSci']

courses.pop()       # By default, this removes the LAST value in list
print(courses)      # Output: ['History', 'Math', 'Physics']

# .pop() also returns/saves the variable it removed
popped = courses.pop()

print(popped)       # Output: CompSci
print(courses)      # Output: ['History', 'Math', 'Physics']


# list.pop()
# Remove and return last item in list.

my_list5 = [5, 8, 14]
val = my_list5.pop()

print(val)  #Output: [5, 8] | val is 14



# list.pop(i)
# Remove and return item at position i in list.

my_list6 = [5, 8, 14]
val2 = my_list6.pop(0)

print(val2)     #Output: [8, 14] | val is 5



# .reverse()
courses = ['History', 'Math', 'Physics', 'CompSci']

courses.reverse()       # reverses the list
print(courses)          # Output: ['CompSci', 'Physics', 'Math', 'History']


# .sort()
courses = ['History', 'Math', 'Physics', 'CompSci']

courses.sort()      # Sorts in alphabetical order
print(courses)      # Output: ['CompSci', 'History', 'Math', 'Physics']


# .sort() on lists w/ numbers are sorted in ascending order
numz = [1,5,2,4,3]
numz.sort()

print(numz)         # Output: [1, 2, 3, 4, 5]


# Sort a list in descending order
courses = ['History', 'Math', 'Physics', 'CompSci']
numz = [1,5,2,4,3]

courses.sort(reverse=True)
numz.sort(reverse=True)

print(courses)          # Output: ['Physics', 'Math', 'History', 'CompSci']
print(numz)             # Output: [5, 4, 3, 2, 1]



# Check if something is in our list using the in

print('Art' in courses)     # Output: False | because Art is not in our courses list
print('Math' in courses)    # Output: True | because Math is in our courses list


# Sort short_names in reverse alphabetic order. Sample output from given program:
# ['Tod', 'Sam', 'Joe', 'Jan', 'Ann']


short_names = ['Jan', 'Sam', 'Ann', 'Joe', 'Tod']

short_names.sort()
short_names.reverse()

print(short_names)     # Outputs: ['Tod', 'Sam', 'Joe', 'Jan', 'Ann']



###Miscellaneous###
# list.index(x)
# Return index of first item in list with value x.

my_list9 = [5, 8, 14]
print(my_list9.index(14))     # Prints "2"



# list.count(x)
# Count the number of times value x is in list.

my_list10 = [5, 8, 5, 5, 14]
print(my_list10.count(5))     # Prints "3"




# LIST METHODS

# An example of a popular list method is .append(), which allows us to add an element to the end of a list.

append_example = ['This', 'is', 'an', 'example']
append_example.append('list')

print(append_example)   # Will output: ['This', 'is', 'an', 'example', 'list']



#### Growing a List: Append ####

# We can add a single element to a list using the .append() Python method.
# Suppose we have an empty list called garden:

garden = []

# We can add the element "Tomatoes" by using the .append() method:
garden.append("Tomatoes")

print(garden)     # Will output: ['Tomatoes']


# When we use .append() on a list that already has elements, our new element is added to the end of the list:

# Create a list
garden = ["Tomatoes", "Grapes", "Cauliflower"]

# Append a new element
garden.append("Green Beans")
print(garden)             # Will output: ['Tomatoes', 'Grapes', 'Cauliflower', 'Green Beans']




#### Growing a List: Plus (+) ####

# When we want to add multiple items to a list, we can use + to combine two lists
# (this is also known as concatenation).
# Below, we have a list of items sold at a bakery called items_sold:

items_sold = ["cake", "cookie", "bread"]

# Suppose the bakery wants to start selling "biscuit" and "tart":
items_sold_new = items_sold + ['biscuit', 'tart']

print(items_sold_new)         # Would output: ['cake', 'cookie', 'bread', 'biscuit', 'tart']

# In this example, we created a new variable, items_sold_new, which contained both the
# original items sold, and the new items.
# We can inspect the original items_sold and see that it did not change.

# We can only use + with other lists. If we type in this code:

my_list = [1, 2, 3]
my_list + 4

# we will get the following error:
# TypeError: can only concatenate list (not "int") to list

# If we want to add a single element using +, we have to put it into a list with brackets ([]):
# my_list + [4]

orders = ["daisy", "buttercup", "snapdragon", "gardenia", "lily"]
new_orders = ['lilac', 'iris']

orders_combined = orders + new_orders
print(orders_combined)
# Output: ['daisy', 'buttercup', 'snapdragon', 'gardenia', 'lily', 'lilac', 'iris']



#### Accessing List Elements ####

employees = ["Michael", "Dwight", "Jim", "Pam", "Ryan", "Andy", "Robert"]

# Python lists are zero-indexed. This means that the first element in a list has index 0, rather than 1.
# In this example, the element with index 2 is "Amare".

# Use square brackets ([ and ]) to select the 4th employee from the list employees.
# Save it to the variable employee_four.

employee_four = employees[3]
print(employee_four)        # Output: Pam
print(employees[6])         # Output: Robert



#### Accessing List Elements: Negative Index ####

shopping_list = ["eggs", "butter", "milk", "cucumbers", "juice", "cereal"]

# Create a called variable last_element.
# Assign the last element in shopping_list to the variable last_element using a negative index.

last_element = shopping_list[-1]

# Now select the element with index 5 and save it to the variable index5_element.
index5_element = "cereal"

# Use print to display both index5_element and last_element.
# Note that they are equal to "cereal"!

print(index5_element)       # Output: cereal
print(last_element)         # Output: cereal




#### Modifying List Elements ####

# Define a list called garden_waitlist and set the value to contain our customers (in order):
# "Jiho", "Adam", "Sonny", and "Alisha".

garden_waitlist = ["Jiho", "Adam", "Sonny", "Alisha"]

# Replace "Adam" with our other interested customer "Calla" using the index method.
# Print garden_waitlist to see the change!

garden_waitlist[1] = "Calla"

print(garden_waitlist)      # Output: ['Jiho', 'Calla', 'Sonny', 'Alisha']

# Replace Alisha with Alex using a negative index.
# Print garden_waitlist again to see the change!

garden_waitlist[-1] = "Alex"

print(garden_waitlist)        # Output: ['Jiho', 'Calla', 'Sonny', 'Alex']



### Shrinking a List: Remove ###

# Let’s create a list called order_list with the following values (in this particular order):
# "Celery", "Orange Juice", "Orange", "Flatbread"
# Print order_list to see the current list.

order_list = ["Celery", "Orange Juice", "Orange", "Flatbread"]

# We are in luck! We actually found a spare case of "Flatbread" in our back storage.
# We won’t need to order it anymore. Let’s remove it from order_list using the .remove() method.

# Print order_list to see the current list.

order_list.remove("Flatbread")

print(order_list)           # Output: ['Celery', 'Orange Juice', 'Orange']




# Create a new list called new_store_order_list and assign it the following values (in order):

# "Orange", "Apple", "Mango", "Broccoli", "Mango"
# Note: Our second store is going to need two orders of mangos so the value is duplicated.
# Print new_store_order_list to see the current list.

new_store_order_list = ["Orange", "Apple", "Mango", "Broccoli", "Mango"]

# We are in luck again! We actually found a spare case of "Mango" in our back storage.
# We won’t be needing to place two orders anymore.
# Let’s remove it from new_store_order_list using the .remove() method.
# Print new_store_order_list to see the current list.

new_store_order_list.remove("Mango")
print(new_store_order_list)         # Output: ['Orange', 'Apple', 'Broccoli', 'Mango']




# Calla ran to tell us some important news! She asked us to remove "Onions" from our new new_store_order_list.
# If we double-check our list, we will notice we don’t have "Onions" on our list.
# Let’s see what happens when we try to remove an item that does not exist.
# Call the .remove() method with the value of "Onions" on our new_store_order_list list.

new_store_order_list.remove("Onions")
# Output:
# Traceback (most recent call last):
#   File "./prog.py", line 5, in <module>
# ValueError: list.remove(x): x not in list




# LIST SLICING using :

# list[start:end:step]

my_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
#          0, 1, 2, 3, 4, 5, 6, 7, 8, 9
#        -10,-9,-8,-7,-6,-5,-4,-3,-2,-1


# Below is how we extract certain values from the list
print(my_list[0]) # Outputs: 0
print(my_list[5]) # Outputs: 5
print(my_list[-1]) # Outputs: 9
print(my_list[-10]) # Outputs: 0


# Below is how we extract a certain range from the list
# Say that I want values from my_list from index 0 to 5
print(my_list[0:5]) # Outputs: [0, 1, 2, 3, 4]  # It gets to the 5th index and stops...cutting out 5

# If I wanted to include 5:
print(my_list[0:6]) # Outputs: [0, 1, 2, 3, 4, 5]


# Another example: Get values 3 - 7:
my_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# #          0, 1, 2, 3, 4, 5, 6, 7, 8, 9
# #        -10,-9,-8,-7,-6,-5,-4,-3,-2,-1

print(my_list[3:8]) # Outputs: [3, 4, 5, 6, 7]


# You can also mix n match negative and positive indexes
print(my_list[-7:8])  # Output same: [3, 4, 5, 6, 7]


# Prints from index 1 all the way to the end
print(my_list[1:])  # Output: [1, 2, 3, 4, 5, 6, 7, 8, 9]


# Prints from index 1 all the way to the start
print(my_list[:-1])  # Output: [0, 1, 2, 3, 4, 5, 6, 7, 8]


# Prints a copy of the list
print(my_list[:])  # Output: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]




# Using Stride:  list[start:end:step]
# The step, allows you to skip numbers

my_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
#          0, 1, 2, 3, 4, 5, 6, 7, 8, 9
#        -10,-9,-8,-7,-6,-5,-4,-3,-2,-1


#Example: If I wanted to start at the value 2 and go to 8 and Skip by 2

print(my_list[2:-1:2])  # Output: [2, 4, 6, 8]
print(my_list[2:-1:1])  # Output: [2, 3, 4, 5, 6, 7, 8] | which is like not using the Stride/Step at all
print(my_list[-1:2:-1])  # Output: [9, 8, 7, 6, 5, 4, 3]
                        # Going in Reverse: started at -1 index and going index 2,
print(my_list[::-1])    #Output: [9, 8, 7, 6, 5, 4, 3, 2, 1, 0] | Runs the list in reverse



# A slice, or sub-list of Python list elements can be selected from a list using a colon-separated
# starting and ending point.
# The syntax pattern is myList[START_NUMBER:END_NUMBER]. The slice will include the START_NUMBER index,
# and everything until but excluding the END_NUMBER item.
# When slicing a list, a new list is returned, so if the slice is saved and then altered,
# the original list remains the same.


tools = ['pen', 'hammer', 'lever', 'screw', 'drill']
tools_slice = tools[1:3]
tools_slice2 = tools[0:2]
tools_slice3 = tools[2:4]
tools_slice[0] = 'nail'

print(tools_slice)  # ['hammer', 'lever']
print(tools_slice2)  # ['pen', 'hammer']
print(tools_slice3)  # ['lever', 'screw']

# Original list is unaltered:
print(tools)  # ['pen', 'hammer', 'lever', 'screw', 'drill']




#### List Method .count() ####

# The .count() Python list method searches a list for whatever search term it receives as an argument,
# then returns the number of matching entries found.

backpack = ['pencil', 'pen', 'notebook', 'textbook', 'pen', 'highlighter', 'pen']
numPen = backpack.count('pen')

print(numPen)       # Output: 3



####List Method .sort()####
# The .sort() Python list method will sort the contents of whatever list it is called on.
# Numerical lists will be sorted in ascending order,
# and lists of Strings will be sorted into alphabetical order.
# It modifies the original list, and has no return value.

exampleList = [4, 2, 1, 3]
exampleList.sort()
print(exampleList)          # Output: [1, 2, 3, 4]



### sorted() Function ###
# The Python sorted() function accepts a list as an argument, and will return a new,
# sorted list containing the same elements as the original. Numerical lists will be sorted in ascending order,
# and lists of Strings will be sorted into alphabetical order. It does not modify the original, unsorted list.

unsortedList = [4, 2, 1, 3]
sortedList = sorted(unsortedList)

print(sortedList)       # Output: [1, 2, 3, 4]



# Turning a List into a String using .join()

courses = ['History', 'Math', 'Physics', 'CompSci']

# print courses list values into comma separated:
course_str = ', '.join(courses)
print(course_str)       # History, Math, Physics, CompSci

# print courses list values w/ hyphens separated:
course_str = ' - '.join(courses)
print(course_str)       # History - Math - Physics - CompSci


# Turn a String back to a List using .split()

course_str = ' - '.join(courses)

new_list = course_str.split(' - ')      # This is looking at all the ' - '
                                        # in courses = History - Math - Physics - CompSci
                                        # and saying make a new list w/ those values

print(new_list)                         # ['History', 'Math', 'Physics', 'CompSci']
                                        # We are now back to the courses list


# More on split()
# >>> '1,2,3'.split(',')
# ['1', '2', '3']
# >>> '1,2,3'.split(',', maxsplit=1)
# ['1', '2,3']
# >>> '1,2,,3,'.split(',')
# ['1', '2', '', '3', '']


user_input = input('1,2,3')
tokens = user_input.split()

print(tokens)       # Output: 1,2,3



### List Method .insert() ###
# The Python list method .insert() allows us to add an element to a specific index in a list.
# It takes in two inputs:
     # The index that you want to insert into.
     # The element that you want to insert at the specified index.

# Here is a list representing a line of people at a store
store_line = ["Karla", "Maxium", "Martim", "Isabella"]

# Here is how to insert "Vikor" after "Maxium" and before "Martim"
store_line.insert(2, "Vikor")

print(store_line)     # Output: ['Karla', 'Maxium', 'Vikor', 'Martim', 'Isabella']



### ADDING LIST ITEMS VIA INDICES
# Write a statement that prints the result of adding the second and fourth items of the list.
# Make sure to access the list by index!

numbers = [5, 6, 7, 8]

print("Adding the numbers at indices 0 and 2...")
print(numbers[2] + numbers[3])
print("Adding the numbers at indices 1 and 3...")
# # Your code here!
print(numbers[1] + numbers[3])

# Output: Adding the numbers at indices 0 and 2...
# 15
# Adding the numbers at indices 1 and 3...
# 14



# Write an assignment statement that will replace the item that currently holds
# the value "tiger" with another animal (as a string). It can be any animal you like.

zoo_animals = ["pangolin", "cassowary", "sloth", "tiger"]
# Last night our zoo's sloth brutally attacked
# the poor tiger and ate it whole.

# The ferocious sloth has been replaced by a friendly hyena.
zoo_animals[2] = "hyena"

# What shall fill the void left by our dear departed tiger?
# Your code here!
zoo_animals[-1] = "lion"

print(zoo_animals)        # Output: ['pangolin', 'cassowary', 'hyena', 'lion']



### list(iter) ###

# Creates a list.

my_list = list('123')
print(my_list)          # Output: ['1', '2', '3']





#### TUPLES / SETS ####

# Tuples

# Lists are Mutable
list_1 = ['History', 'Math', 'Physics', 'CompSci']
list_2 = list_1

print(list_1)   # ['History', 'Math', 'Physics', 'CompSci']
print(list_2)   # ['History', 'Math', 'Physics', 'CompSci']

list_1[0] = 'Art'

print(list_1)   # ['Art', 'Math', 'Physics', 'CompSci']
print(list_2)   # ['Art', 'Math', 'Physics', 'CompSci']





# Tuples are Immutable

# TUPLES ARE JUST LIKE LISTS BUT THEY USE THE () INSTEAD OF []

tuple_1 = ('History', 'Math', 'Physics', 'CompSci')
tuple_2 = tuple_1

print(tuple_1)  # ('History', 'Math', 'Physics', 'CompSci')
print(tuple_2)  # ('History', 'Math', 'Physics', 'CompSci')


tuple_1[0] = 'Art'

print(tuple_1)
print(tuple_2)  # TypeError: 'tuple' object does not support item assignment
                # Tuples are Immutable, meaning they cannot be changed
                # So there are much less methods for Tuples



# Sets
# Sets are unordered and throw away or have NO duplicates

cs_courses = {'History', 'Math', 'Physics', 'CompSci'}

print(cs_courses)   # {'Physics', 'Math', 'History', 'CompSci'}
                    # Notice it is out of order from orig list

# Sets throwing out duplicates:
# If I add another Math course to end of set:

cs_courses = {'History', 'Math', 'Physics', 'CompSci', 'Math'}

print(cs_courses)   # {'History', 'Math', 'CompSci', 'Physics'}
                    # Notice we still only have 4 courses.
                    # It got rid of the duplicate Math we added


# Sets are used to check if a value is part of the set (membership test)"

cs_courses = {'History', 'Math', 'Physics', 'CompSci', 'Math'}

print('Math' in cs_courses)     # Outputs: True



# Sets are also optimized to see similarities and differences
# Below, we are seeing what values cs_courses and art_courses have in common using the .intersection()

cs_courses = {'History', 'Math', 'Physics', 'CompSci'}
art_courses = {'History', 'Art', 'Design', 'Math'}

print(cs_courses.intersection(art_courses))     # Outputs: {'Math', 'History'}



# Below, we are seeing what values cs_courses and art_courses do NOT have in common using the .difference()

cs_courses = {'History', 'Math', 'Physics', 'CompSci'}
art_courses = {'History', 'Art', 'Design', 'Math'}

print(cs_courses.difference(art_courses))     # Outputs: {'Physics', 'CompSci'}


# If we wanted to see ALL courses in both sets, use the .union():

cs_courses = {'History', 'Math', 'Physics', 'CompSci'}
art_courses = {'History', 'Art', 'Design', 'Math'}

print(cs_courses.union(art_courses))        # {'Physics', 'History', 'Math', 'Art', 'Design', 'CompSci'}



# When creating an empty set, you cannot do like Lists and Tuples:

# Empty Lists
empty_list = []
empty_list = list()

# Empty Tuples
empty_tuple = ()
empty_tuple = tuple()

# Empty Sets
empty_set = {} # This isn't right! It's a dict
empty_set = set()
