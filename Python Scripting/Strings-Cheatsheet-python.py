
# Print a String over multiple lines using """

message = """Bobby's World was a good 
cartoon in the 1990s"""

print(message)          # Output: Bobby's World was a good
                                # cartoon in the 1990s



# Find how many characters in a String using len()
message = 'Hello World'
print(len(message))         # Output: 11



# Using index to locate specific characters using []
message = 'Hello World'
print(message[0])           # Output: H



# String Slicing using :
# Remember everything AFTER the Colon : is cut off

# To grab the word Hello:
message = 'Hello World'
print(message[0:5])         # Output: Hello

print(message[:5])    # If starting at Zero index, you can leave out the 0 and get same result



# To grab the word World:

message = 'Hello World'
print(message[6:])         # Output: World




# Select the first letter of the variable my_name and save it to first_initial.

my_name = "Aaron"
first_initial = my_name[0]






# String Methods - .lower(), .upper(), .count(), .find()

message = 'Hello World'

print(message.lower())      # Output: hello world
                            # When adding the .lower() method; string is set to all lowercase

print(message.upper())      # Output: HELLO WORLD
                            # the .upper() method, changes the string to all uppercase

lower_strings = 'Concatenating Strings'
upper_strings = lower_strings.upper()
print(upper_strings)                    # Outputs: CONCATENATING STRINGS


print(message.count('Hello'))      # Outputs: 1 | the # of times the string 'Hello' is in 'Hello World'
print(message.count('l'))      # Outputs: 3 | the # of times the character 'l' is in 'Hello World'
print(message.find('World'))    # Outputs: 6 | which is the index number 'World' starts on (the W is index 6)



# The .replace() method:

message = 'Hello World'     # Original message
new_message = message.replace('World', 'Universe')  # Set a new variable = to message.replace('old_word', 'new_word')
print(new_message)  # print new variable





# CONCATENATING STRINGS

greeting = 'Hello'
name = 'Mike'

message = greeting + name   # Outputs: HelloMike | notice there is NO space between HelloMike

message = greeting + ', ' + name + '. Welcome!'
# Instead add a string ', ' | Which outputs: Hello, Mike. Welcome! |  Which can be alot of work with commas and spaces.

message = '{}, {}. Welcome!'.format(greeting, name) # You can use the .format() method with ease | Outputs: Same

message = f'{greeting}, {name.upper()}. Welcome!'
# The new f{} allows you to remove .format and add var to placeholders | Outputs Same: Hello, Mike. Welcome!

print(message)




# Using the dir() and help() method for help

greeting = 'my'
name = 'man!'

print(dir(name)) #Outputs: All available methods
# ['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__',
#  '__getattribute__', '__getitem__', '__getnewargs__', '__gt__', '__hash__', '__init__', '__init_subclass__',
#  '__iter__', '__le__', '__len__', '__lt__', '__mod__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__',
#  '__repr__', '__rmod__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'capitalize',
#  'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'format_map', 'index', 'isalnum',
#  'isalpha', 'isascii', 'isdecimal', 'isdigit', 'isidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace',
#  'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 'partition', 'removeprefix', 'removesuffix',
#  'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith',
#  'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']



# To get more info on specific string method:

print(help(str.lower))    # Output: Help on method_descriptor:
# lower(self, /)
#     Return a copy of the string converted to lowercase.


print(help(str))      # Outputs: All info about strings
# class str(object)
#  |  str(object='') -> str
#  |  str(bytes_or_buffer[, encoding[, errors]]) -> str
#
#  |  Methods defined here:
#  |
#  |  __add__(self, value, /)
#  |      Return self+value.
#  |
#  |  __contains__(self, key, /)
#  |      Return key in self.
#  |
#  |  __eq__(self, value, /)
#  |      Return self==value.
#
#  | Load More...




# Write a function called account_generator() that takes two inputs,
# first_name and last_name and concatenates the first three letters of each and then returns the new account name.

first_name = "Aaron"
last_name = "Guild"

def account_generator(first_name, last_name):
  account_name = first_name[0:3] + last_name[0:3]
  return account_name

# Test your function on the first_name and last_name provided in script.py and save it to the variable new_account.

new_account = account_generator(first_name, last_name)
print(new_account)                                      # Output: AarGui




########### Updating Above ##############

first_name = "Aaron"
last_name = "Guild"

# Copeland’s Corporate Company also wants to update how they generate temporary passwords for new employees.
# Write a function called password_generator() that takes two inputs, first_name and last_name, and then
# concatenates the last three letters of each and returns them as a string.

def password_generator(first_name, last_name):
  account_name = first_name[-3:] + last_name[-3:]
  return account_name

# Test your function on the provided first_name and last_name and save it to the variable temp_password.

temp_password = password_generator(first_name, last_name)
print(temp_password)                                      # Output: ronild





########Strings and Conditionals (Part One)#########

favorite_fruit = "blueberry"
counter = 0
for character in favorite_fruit:
  if character == "b":
    counter = counter + 1
print(counter)                  # Output: 2

# The above code will count the number of bs in the string “blueberry” (hint: it’s two).
# Let’s take a moment and break down what exactly this code is doing.
# First, we define our string, favorite_fruit, and a variable called counter, which we set equal to zero.
# Then the for loop will iterate through each character in favorite_fruit and compare it to the letter b.
# Each time a character equals b the code will increase the variable counter by one.
# Then, once all characters have been checked, the code will print the counter, telling us how many bs were in “blueberry”.
# This is a great example of how iterating through a string can be used to solve a specific application,
# in this case counting a certain letter in a word.




# Write a function called letter_check that takes two inputs, word and letter.

# This function should return True if the word contains the letter and False if it does not.


def letter_check(word, letter):
  for character in word:
    if character == letter:
      return True
  return False


letter_check("strawberry", "a")   # returns True because a is in strawberry
letter_check("strawberry", "z")   # returns False because z is not strawberry






###########Strings and Conditionals (Part Two)################

# There’s an even easier way than iterating through the entire string to determine if a character is in a string.
# We can do this type of check more efficiently using in. in checks if one string is part of another string.

# Here is what the syntax of in looks like: letter in word

# Here, letter in word is a boolean expression that is True if
# the string letter is in the string word. Here are some examples:

print("e" in "blueberry")   # => True
print("a" in "blueberry")   # => False


# In fact, this method is more powerful than the function you wrote in the last exercise
# because it not only works with letters, but with entire strings as well.

print("blue" in "blueberry")    # => True
print("blue" in "strawberry")   # => False



# Write a function called contains that takes two arguments,
# big_string and little_string and returns True if big_string contains little_string.
#
# For example contains("watermelon", "melon") should return True
# and contains("watermelon", "berry") should return False.

def contains(big_string, little_string):
    return little_string in big_string

contains("watermelon", "melon")   # Output: True
contains("watermelon", "berry")   # OUtput: False




# Write a function called common_letters that takes two arguments,
# string_one and string_two and then returns a list with all of the letters they have in common.

# The letters in the returned list should be unique. For example,
# common_letters("banana", "cream")
# should return ['a'].

def common_letters(string_one, string_two):
  common = []
  for letter in string_one:
    if (letter in string_two) and not (letter in common):
      common.append(letter)
  return common

print(common_letters('banana', 'cream'))    # Output: ['a']
print(common_letters('crepe', 'cream'))    # Output: ['c', 'r', 'e']

# returns a list with all of the letters they have in common








# String Slicing string[start:end:step]

sample_url = 'http://coreyms.com'
print(sample_url)                 # Outputs: http://coreyms.com

# Reverse the url
print(sample_url[::-1])           # Outputs String in Reverse: moc.smyeroc//:ptth

# # Get the top level domain
print(sample_url[-4:])            # Outputs: .com   | You start at -4 index and go to end | [-4:]

# # Print the url without the http://
print(sample_url[7:])                     # Output: coreyms.com

# # Print the url without the http:// or the top level domain
print(sample_url[7:-4])                                         # Output: coreyms




# More String Slicing

first_name = "Rodrigo"
last_name = "Villanueva"

# A new employee, Rodrigo Villanueva, is starting today and you need to create his account.
# His first_name and last_name are stored as strings in script.py.
# Create a variable new_account by slicing the first five letters of his last_name.

new_account = last_name[:5]
print(new_account)            # Output: Villa


# Temporary passwords for new employees are also generated from their last names.
# Create a variable called temp_password by creating a slice out of the third through sixth letters of last_name.
# Your string should have a total of 4 characters.

temp_password = last_name[2:6]
print(temp_password)            # Output: llan




############ Negative Indices ##############


company_motto = "Copeland's Corporate Company helps you capably cope with the constant cacophony of daily life"

# Use negative indices to find the second to last character in company_motto. Save this to the variable second_to_last.

second_to_last = company_motto[-2]
print(second_to_last)                 # Output: f


# Use negative indices to create a slice of the last 4 characters in company_motto. Save this to the variable final_word.

final_word = company_motto[-4:]
print(final_word)                 # Output: life
