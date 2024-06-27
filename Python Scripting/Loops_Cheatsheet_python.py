# BASIC

numsloop = [1, 2, 3, 4, 5]

for num in numsloop:
    print(num)

# Output:
# 1
# 2
# 3
# 4
# 5


### With BREAK ###
# used for STOPPING a loop when meeting a certain condition

numsloop = [1, 2, 3, 4, 5]

for num in numsloop:
    if num == 3:
        print('Found!')
        break
    print(num)

# Output:
# 1
# 2
# Found!



# With CONTINUE #
# use for SKIPPING a number

numsloop = [1, 2, 3, 4, 5]

for num in numsloop:
    if num == 3:
        print('Found!')
        continue
    print(num)

# Output:
# 1
# 2
# Found!
# 4
# 5


# Iterating through loops #
# this example gives you EVERY combination of those numbers and letters

numsloop = [1, 2, 3, 4, 5]

for num in numsloop:
    for letter in 'abc':
        print(num, letter)

# Output:

# 1 a
# 1 b
# 1 c
# 2 a
# 2 b
# 2 c
# 3 a
# 3 b
# 3 c
# 4 a
# 4 b
# 4 c
# 5 a
# 5 b
# 5 c


# For Loops with range()

six_steps = range(6)

# # six_steps is now a collection with 6 elements:
# # 0, 1, 2, 3, 4, 5

# #We can then use the range directly in our for loops as the collection to perform a six-step iteration:

for temp in range(6):
  print("Learning Loops!")


# Would output:

# Learning Loops!
# Learning Loops!
# Learning Loops!
# Learning Loops!
# Learning Loops!
# Learning Loops!




# Something to note is we are not using temp anywhere inside of the loop body.
# If we are curious about which loop iteration (step) we are on, we can use temp to track it.
# Since our range starts at 0, we will add + 1 to our temp to represent how many iterations (steps) our loop takes more accurately.

for temp in range(6):
  print("Loop is on iteration number " + str(temp + 1))

# Would output:

# Loop is on iteration number 1
# Loop is on iteration number 2
# Loop is on iteration number 3
# Loop is on iteration number 4
# Loop is on iteration number 5
# Loop is on iteration number 6




# # Use the range() function in a for loop to print() out the provided promise variable five times.
#
promise = "I will finish the python loops module!"

for temp in range(5):
  print(promise)

# Output:
# I will finish the python loops module!
# I will finish the python loops module!
# I will finish the python loops module!
# I will finish the python loops module!
# I will finish the python loops module!





# # While Loop Walkthrough # #

count = 0
print("Starting While Loop")
while count <= 3:
  Loop Body
  # Print if the condition is still true
  print("Loop Iteration - count <= 3 is still true")
  # Print the current value of count
  print("Count is currently " + str(count))
  # Increment count
  count += 1
  print(" ----- ")
print("While Loop ended")


# Output:
# Starting While Loop
# Loop Iteration - count <= 3 is still true
# Count is currently 0
#  -----
# Loop Iteration - count <= 3 is still true
# Count is currently 1
#  -----
# Loop Iteration - count <= 3 is still true
# Count is currently 2
#  -----
# Loop Iteration - count <= 3 is still true
# Count is currently 3
#  -----
# While Loop ended



# # To quickly comment out the code, use your cursor or mouse to highlight all the code
# # and press command ⌘ + / on a Mac or CTRL + / on a Windows machine.


# # Your code below:
# # Create a variable named countdown and set the value to 10.
countdown = 10

# # Define a while loop that will run while our countdown variable is greater than or equal to zero.

# # On each iteration:
# # We should print() the value of the countdown variable.
# # We should decrease the value of the countdown variable by 1

while countdown >= 0:
  print(countdown)
  countdown -= 1

# # Now that we have built our loop, let’s commemorate our success by printing "We have liftoff!" after the while loop.
# print("We have liftoff!")

# Output:
# 10
# 9
# 8
# 7
# 6
# 5
# 4
# 3
# 2
# 1
# 0
# We have liftoff!




#######################
python_topics = ["variables", "control flow", "loops", "modules", "classes"]
# #Your code below:
# # We are going to write a while loop to iterate over the provided list python_topics.

# # First, we will need a variable to represent the length of the list.
# # This will help us know how many times our while loop needs to iterate.

# # Create a variable length and set its value to be the length of the list of python_topics.
length = len(python_topics)


# # Next, we will require a variable to compare to our length variable to make sure we are able
# # to implement a condition that eventually allows the loop to stop.
#
# # Create a variable called index and initialize the value to be 0.
index = 0


# # Let’s now build our loop.
# # We want our loop to iterate over the list of python_topics and
# # on each iteration print "I am learning about <element from python_topics>".
# #
# # For this loop we will need the following components:

# # A condition for our while loop
# # A statement in the loop body to print from our condition
# # A statement in the loop body to increment our index forward.
# # The end result should output:

# # I am learning about variables
# # I am learning about control flow
# # I am learning about loops
# # I am learning about modules
# # I am learning about classes
# # If you notice the Run button spinning continuously or a “Lost connection to Codecademy” message in an exercise,
# # you may have an infinite loop!

# # If the stop condition for our loop is never met,
# # we will create an infinite loop which stops our program from running anything else.
# # To exit out of an infinite loop in an exercise, refresh the page — then fix the code for your loop.

while index < length:
    print("I am learning about " + python_topics[index])
index += 1


# Output:
# I am learning about variables
# I am learning about variables
# I am learning about variables
# I am learning about variables
# I am learning about variables
# I am learning about variables
# I am learning about variables
# I am learning about variables
# And it will KEEP going infinitely




  # Loop Control: Break
  # Loops in Python are very versatile.
  # Python provides a set of control statements that we can use to get even more control out of our loops.

  # Let’s take a look at a common scenario that we may encounter to see a use case for loop control statements.

  # Take the following list items_on_sale as our example:

  # items_on_sale = ["blue shirt", "striped socks", "knit dress", "red headband", "dinosaur onesie"]

  # It’s often the case that we want to search a list to check if a specific value exists.
  # What does our loop look like if we want to search for the value of "knit dress" and print out "Found it" if it did exist?

# It would look something like this:

  for item in items_on_sale:
    if item == "knit dress":
      print("Found it")

  # This code goes through each item in items_on_sale and checks for a match.
  # This is all fine and dandy but what’s the downside?
  #
  # Once "knit_dress" is found in the list items_on_sale, we don’t need to go through the rest of the items_on_sale list.
  # Unfortunately, our loop will keep running until we reach the end of the list.
  #
  # Since it’s only 5 elements long, iterating through the entire list is not a big deal in this case but
  # what if items_on_sale had 1000 items?
  # What if it had 100,000 items? This would be a huge waste of time for our program!
  #
  # Thankfully you can stop iteration from inside the loop by using break loop control statement.
  #
  # When the program hits a break statement it immediately terminates a loop. For example:

  # items_on_sale = ["blue shirt", "striped socks", "knit dress", "red headband", "dinosaur onesie"]
  #
  # print("Checking the sale list!")

  for item in items_on_sale:
      print(item)
      if item == "knit dress":
          break

  print("End of search!")

#   # This would produce the output:
#   #
#   # Checking the sale list!
#   # blue shirt
#   # striped socks
#   # knit dress
#   # End of search!
#
#   # When the loop entered the if statement and saw the break it immediately ended the loop.
#   # We didn’t need to check the elements of "red headband" or "dinosaur onesie" at all.
#
#   # Example:
#
#   # You have a list of dog breeds you can adopt, dog_breeds_available_for_adoption.
#
dog_breeds_available_for_adoption = ["french_bulldog", "dalmatian", "shihtzu", "poodle", "collie"]
dog_breed_I_want = "dalmatian"
#
#   # Using a for loop, iterate through the dog_breeds_available_for_adoption list and print() out each dog breed.
#
#   # Use the <temporary variable> name of dog_breed in your loop decleration.
#
for dog_breed in dog_breeds_available_for_adoption:
print(dog_breed)
#
#   # Inside your for loop, after you print each dog breed,
#   # check if the current element inside dog_breed is equal to dog_breed_I_want. If so, print "They have the dog I want!"
#
  for dog_breed in dog_breeds_available_for_adoption:
    print(dog_breed)
    if dog_breed == dog_breed_I_want:
      print("They have the dog I want!")
#
#   # Add a break statement when your loop has found dog_breed_I_want
#   # so that the rest of the list does not need to be checked once we have found our breed.
#
for dog_breed in dog_breeds_available_for_adoption:
    print(dog_breed)
    if dog_breed == dog_breed_I_want:
        print("They have the dog I want!")
        break

# Output:
# french_bulldog
# dalmatian
# They have the dog I want!




# # Loop Control: Continue # #
#
# # What if we only want to skip the current iteration of the loop?
#
# # Let’s take this list of integers as our example:
#
big_number_list = [1, 2, -1, 4, -5, 5, 2, -9]
# # What if we want to print out all of the numbers in a list, but only if they are positive integers. We can use another common loop control statement called continue.
#
for i in big_number_list:
  if i <= 0:
    continue
  print(i)
#
# # This would produce the output:
# # 1
# # 2
# # 4
# # 5
# # 2
#
# # Notice a few things:
#
# # Similar to when we were using the break control statement,
# # our continue control statement is usually paired with some form of a conditional (if/elif/else).
# # When our loop first encountered an element (-1) that met the conditions of the if statement,
# # it checked the code inside the block and saw the continue. When the loop then encounters a continue statement
# # it immediately skips the current iteration and moves onto the next element in the list (4).
# # The output of the list only printed positive integers in the list because every time our loop entered the if statement
# # and saw the continue statement it simply moved to the next iteration of the list and thus never reached the print statement.
#
#
ages = [12, 38, 34, 26, 21, 19, 67, 41, 17]
#
# # Your computer is the doorman at a bar in a country where the drinking age is 21.
#
# # Loop through the ages list. If an entry is less than 21, skip it and move to the next entry. Otherwise, print() the age.
#
for i in ages:
  if i < 21:
    continue
  print(i)
#
# Output:
# 38
# 34
# 26
# 21
# 67
# 41
#
#
#
#
# # Nested Loops
# # Loops can be nested in Python, as they can with other programming languages. We will find certain situations that require nested loops.
# #
# # Suppose we are in charge of a science class, that is split into three project teams:
#
project_teams = [["Ava", "Samantha", "James"], ["Lucille", "Zed"], ["Edgar", "Gabriel"]]
#
# # Using a for or while loop can be useful here to get each team:
#
for team in project_teams:
  print(team)
#
# # Would output:
# #
# # ["Ava", "Samantha", "James"]
# # ["Lucille", "Zed"]
# # ["Edgar", "Gabriel"]


# # But what if we wanted to print each individual student?
# # In this case we would actually need to nest our loops to be able loop through each sub-list.
# # Here is what it would look like:

# # Loop through each sublist

project_teams = [["Ava", "Samantha", "James"], ["Lucille", "Zed"], ["Edgar", "Gabriel"]]

for team in project_teams:
#   # Loop elements in each sublist
  for student in team:
    print(student)
#
# # This would output:
#
# # Ava
# # Samantha
# # James
# # Lucille
# # Zed
# # Edgar
# # Gabriel


# # Let’s practice wiriting a nested loop!
#
# # We have provided the list sales_data that shows the
# # numbers of different flavors of ice cream sold at
# # three different locations: Scoopcademy, Gilberts Creamery, and Manny’s Scoop Shop.

# # We want to sum up the total number of scoops sold.
# # Start by defining a variable scoops_sold and set it to zero.


sales_data = [[12, 17, 22], [2, 10, 3], [5, 12, 13]]

scoops_sold = 0

# # Loop through the sales_data list using the following guidelines:

# # 1) For our temporary variable of the for loop, call it location.
# # 2) print() out each location list.


# # Within our sales_data loop,
# # nest a secondary loop to go through each location sublist element and add the element value to scoops_sold.

# # By the end, you should have the sum of every number in the sales_data nested list.

# # Print out the value of scoops_sold outside of the nested loop.

for location in sales_data:
    print(location)
    for element in location:
        scoops_sold += element

print(scoops_sold)
#
#
# Output:
# [12, 17, 22]
# [2, 10, 3]
# [5, 12, 13]
# 96


# # Let’s write our own list comprehensions with conditionals!


heights = [161, 164, 156, 144, 158, 170, 163, 163, 157]

can_ride_coaster = []


for num in heights:
    if num > 161:
        can_ride_coaster.append(num)

print(can_ride_coaster)


# # I just settled on the "Traditional Way" of writing for loops.
# # Don't overcomplicate!




# # Review

# # Directions
#
# # 1. Create a list called single_digits that consists of the numbers 0-9 (inclusive).
# # 2. Create a for loop that goes through single_digits and prints out each one.
# # 3. Before the loop, create a list called squares. Assign it to be an empty list to begin with.
# # 4. Inside the loop that iterates through single_digits,
# # append the squared value of each element of single_digits to the list squares.
# # You can do this before or after printing the element.
# # 5. After the for loop, print out squares.

single_digits = range(0, 10)

squares = []

for num in single_digits:
  squares.append(num**2)

print(squares)


# # 6. Create the list cubes using a list comprehension on the single_digits list.
# # Each element of cubes should be an element of single_digits taken to the third power.
# # 7. Print cubes

cubes = [num**3 for num in single_digits]
print(cubes)


# Output:
# [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
# [0, 1, 8, 27, 64, 125, 216, 343, 512, 729]
