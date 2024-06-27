# Built-in Functions vs User Defined Functions

tshirt_price = 9.75
shorts_price = 15.50
mug_price = 5.99
poster_price = 2.00


# Write your code below:
# Create a variable called max_price and call the built-in function max() with the variables of prices to get the maximum price.
# Print max_price.

max_price = max(9.75, 15.50, 5.99, 2.00)
print(max_price)                            # Output: 15.5



# Using the same set of prices, create a new variable called min_price and use the built-in function min() with
# the variables of prices to get the minimum price.
# Print min_price.

min_price = min(9.75, 15.50, 5.99, 2.00)
print(min_price)                            # Output: 2


# Use the built-in function round() to round the price of the variable tshirt_price by one decimal place.
# Save the result to a variable called rounded_price and print it.

# Hint
# The round() built-in function takes in two arguments.
# The first argument is the number we want to round, followed by an argument on how many decimal places we want to round it.


# Here is an example:

# rounded_zero = round(10.54, 0)
# rounded_one = round(10.54, 1)

# print(rounded_zero)           # 11.00
# print(rounded_one)            # 10.5


rounded_price = round(tshirt_price, 1)
print(rounded_price)                    # Output: 9.8



# all(list)
# True if every element in list is True (!= 0), or if the list is empty.

print('all:')
print(all([1, 2, 3]))
print(all([0, 1, 2]))       # Output:
                            # True
                            # False



# any(list)
# True if any element in the list is True.

print('any:')
print(any([0, 2]))
print(any([0, 0]))      # Output:
                        # True
                        # False


# max(list)
# Get the maximum element in the list.

print('max:')
print(max([-3, 5, 25]))     # Output: 25


# min(list)
# Get the minimum element in the list.

print('min:')
print(min([-3, 5, 25]))        # Output: -3


# sum(list)
# Get the sum of all elements in the list.

print('sum:')
print(sum([-3, 5, 25]))     # Output: 27



# Examples:

my_list = [0, 5, 10, 15]

print(sum(my_list))     # 30
print(max(my_list))     # 15
print(any(my_list))     # True
print(all(my_list))     # False
print(min(my_list))     # 0




#Lebron James: Statistics for 2003/2004 - 2012/2013
games_played = [79, 80, 79, 78, 75, 81, 76, 79, 62, 76]
points = [1654, 2175, 2478, 2132, 2250, 2304, 2258, 2111, 1683, 2036]
assists = [460, 636, 814, 701, 771, 762, 773, 663, 502, 535]
rebounds = [432, 588, 556, 526, 592, 613, 554, 590, 492, 610]

# Print total points
print('Total Points:')
print(sum(points))

# Print Average PPG
print('Avg PPG:')
print(sum(points) / sum(games_played))


# Print best scoring year
print('Best Scoring Year:')
print(max(points))

# Print worst scoring year
print('Worst Scoring Year:')
print(min(points))
