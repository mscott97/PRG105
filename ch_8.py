Complete all of the TODO directions
    The number next to the TODO represents the chapter
    and section that explain the required code
    Your file should compile error free
    Submit your completed file
"""

# TODO 8.1 Basic string Operation
# Print all the characters from the name variable by accessing one character at a time

name = "John Jacob Jingleheimer Schmidt"
for ch in name:
    print(ch)

# Use the index to access and print the capital s in Schmidt from the variable name

my_string = 'John Jacob Jingleheimer Schmidt'
print(my_string[24])

# Use the index with negative numbers to print the letters from the last name "Schmidt" in the
# name variable
my_string = 'John Jacob Jingleheimer Schmidt'
print(my_string[2], my_string[4], my_string[7])

# TODO 8.2 String slicing
# use string slicing to assign the middle name "Jacob" from name to the variable middle, replace the ""
full_name = 'John Jacob Jingleheimer Schmidt'
middle_name = full_name[4:9]

# TODO 8.3 Testing, Searching, and manipulating strings
string1 = 'john Jacob Jingleheimer Schmidt'
if 'Jacob' in string1:
    print('The string ' "jacob" ' was found' )
else:
    print()
# test to see if the string "Jacob" is in name

# test to see if the string "Michael" is in name
string1 = 'john Jacob Jingleheimer Schmidt'
if 'micheal' in string1:
    print('the string ' "micheal" ' was fround')
else:
    print('the string ' "Micheal" ' was not found')
# Test to see if name is a number

string1 = 'john Jacob Jingleheimer Schmidt'
if string1.isdigit():
    print(string1, 'does not have any numbers')
else:
    print(string1, 'does have numbers')
# Test to see if number is a number

number = 42
if number.isdigit():
    print(number, 'does have a number')
else:
    print(number, 'does not have a number')
# Search for "J" in name, replace with "j" (lower case)
letters = 'John Jacob Jingleheimer Schmidt'
if 'j' in letters:
    print(letters, letters.lower())
else:(0)

# split the string name into the variable name_list, replace the ""
name_list = my_string.spilt()
print(name_list)
