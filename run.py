import math
import random
import operator


def user_input():
    user_x = int(input("Range start value:"))
    user_y = int(input("Range end value:"))
    return user_x, user_y


def random_range_number(x, y):
    """
    Accepts a number range input between two numbers from the uses and
    randomize them
    """
    while True:
        try:
            if y < x:
                print("You need a number larger than your first value")
                print("pleas try again\n")
            else:
                value_x = x
                value_y = y
                print("Random x:")
                random_x = print(f"{random.randint(value_x, value_y)}")
                print("Random y:")
                random_y = print(f"{random.randint(value_x, value_y)}")
                return random_x, random_y
        except ValueError as e:
            print(f"invalid data: {e}, pleas try again")
            return False
    return True


def main():
    """
    This is the main function of that will run all the functions
    """
    user_input_x, user_input_y = user_input()
    random_range_number(user_input_x, user_input_y)


main()
