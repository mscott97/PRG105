"""
    Complete all of the TODO directions
    The number next to the TODO represents the chapter
    and section that explain the required code
    Your file should compile error free
    Submit your completed file

    We are going to convert the coin class to a dice class
    The following code is based on the coin class from your book
"""

import random
# TODO change class name to Dice


class Dice:  # note class names are capitalized
    def __init__(self):
        # TODO change side_up to '1'
        self.one = '1'
        self.two = '2'
        self.three = '3'
        self.four = '4'
        self.five = '5'
        self.six = '6'

        # TODO change name to roll
    def roll(self):
        # TODO change to reflect 6 sides and assign the number
        if random.randint(0, 7) == 0:
            self.one = '1'
        elif random.randint(0, 7) == 1:
            self.two = '2'
        elif random.randint(0, 7) == 2:
            self.three = '3'
        elif random.randint(0, 7) == 3:
            self.four = '4'
        elif random.randint(0,7) == 4:
            self.five = '5'
        else:
            self.six = '6'

    def get_one(self):
        return self.one


def main():
    # TODO change my_coin to my_dice, my_dice_two and the appropriate class name throughout main
    my_dice = Dice()
    my_dice_two = Dice()
    print('This side is up, ', my_dice.get_one())
    print('This side is up, ', my_dice_two.get_one())

    print('I am rolling the dice...')
    my_dice.roll()
    my_dice_two.roll()
    print('This side is up, ', my_dice.get_one())
    print('This side is up, ', my_dice_two.get_one())



main()
