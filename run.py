import math
import random
import operator


def user_input():
    try:
        user_x = int(input("Range start value:"))
        user_y = int(input("Range end value:"))
    except ValueError:
        print("Invalid input. Please enter a valid integer.")
        not_integer = user_input()
        return not_integer
    return user_x, user_y


def data_validation(user_value_x, user_value_y):
    while True:
        try:
            x = user_value_x
            y = user_value_y
            if y < x:
                print("You need a number larger than your first value")
                print("pleas try again\n")
                y_biger_than_x = user_input()
                return y_biger_than_x
            else:
                return x, y
        except ValueError as e:
            print(f"invalid data: {e}, pleas try again")
            # invalid_data_type = user_input()
            # return invalid_data_type
    return True
    

def random_range_number(x, y):
    """
    Accepts a number range input between two numbers from the uses and
    randomize them
    """
    value_x = x
    value_y = y
    print("Random x:")
    random_x = print(f"{random.randint(value_x, value_y)}")
    print("Random y:")
    random_y = print(f"{random.randint(value_x, value_y)}")
    return random_x, random_y


def main():
    """
    This is the main function of that will run all the functions
    """
    user_input_x, user_input_y = user_input()
    x_range, y_range = data_validation(user_input_x, user_input_y)
    random_numb_x, random_numb_y = random_range_number(x_range, y_range)


main()
