    Complete all of the TODO directions
    The number next to the TODO represents the chapter
    and section that explain the required code
    Your file should compile error free
    Submit your completed file
"""

# TODO 11.1 Introduction to Inheritance
# You are going to create a Dwelling class based on the Automobile
# Sample from the chapter


# create the class Dwelling, the __init__ method should accept number_of_rooms, square_feet, floors
def_ _ init_ _ (self, number_of_rooms, square_feet, floors):
self. _ _ = number_of_rooms
self. _ _ = sqaure_feet
self. _ _ = floors

def set_number_of_rooms(self, set_number_of_rooms):
self._ _  number_of_rooms = number_of_rooms 
def set_sqaure_feet(self, sqaure_feet):
self._ _  sqaure_feet = sqaure_feet 
def set_floors(self, floors):
self._ _  floors = floors 

def get_number_of_rooms(self):
return self._ _ number_of_rooms
def get_sqaure_feet(self):
return self._ _ sqaure_feet
def get_floors(self):
return self._ _ floors





# add the mutators for all of the data attributes (number_of_rooms, square_feet, floors)


# add the accessors for all of  the data attributes


# Create the class Single_family_home as a sub class of Dwelling
# The __init__ method should accept number_of_rooms, square_feet, floors, garage_type, yard_size


def_ _ init_ _ (self, number_of_rooms, square_feet, floors):
self. _ _ = number_of_rooms
self. _ _ = sqaure_feet
self. _ _ = floors
self. _ _ = garage_type
self. _ _ = yard_size

def set_number_of_rooms(self, set_number_of_rooms):
self._ _  number_of_rooms = number_of_rooms 
def set_sqaure_feet(self, sqaure_feet):
self._ _  sqaure_feet = sqaure_feet 
def set_floors(self, floors):
self._ _  floors = floors 
def set_(self, garage_type):
self. _ _ garage_type = garage_type
def set_(self, yard_size):
self. _ _ yard_size = yard_size

def get_number_of_rooms(self):
return self._ _ number_of_rooms
def get_sqaure_feet(self):
return self._ _ sqaure_feet
def get_floors(self):
return self._ _ floors
def get_garage_type(self):
return self. _ _ garage_type
def get_yard_size(self):

# call the superclass of Dwelling and pass the required arguments, remember to include self

# initialize the garage_type and yard_size attributes

# create the mutator and accessor methods for the garage_type and yard_size attributes


# demonstrate the Single_family_home class, no need to import because you are in the same file
def main():
# create an object from the Single_family_home class with the following information:
# 6 rooms, 1200 square feet, 1 floor, single car garage, .25 acres
# Display the data using the accessor methods
Single_family_home = home. -home(6 rooms, 1200 square feet, 1 floor, single car garage, .25 acres)

print('number_of_rooms:', used_number_of_rooms())
print('square_feet:', used_square_feet())
print('floors:', used_floors())
print('garage_type:', used_garage_type())
print('yard_size:', used_yard_size())

# create the main function
main()
# call the main function


# TODO 11.2 Polymorphism
# Type in the mammal class from program 11-9    lines 1 - 22


# create a Mouse class as a sub class of the mammal class following the Dog example

class Mouse(Mammal):
def _ _ init _ _(self):
mammal._ _init_ _(self, 'Mouse')
def_make_sound(self):
print("squeak! squeak!")
# create a Bird class as a sub class of the mammal class following the Cat Example
class Bird(Mammal):
def _ _ init _ _(self):
mammal._ _init_ _(self, 'Bird')
def_make_sound(self):
print("chip! chip!")

# Follow the example in program 11-10 (no need to import, use main2 instead of main
# because there is already a main on this page) use the Mouse and Bird class that you created
