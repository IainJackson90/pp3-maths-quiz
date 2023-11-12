import math
import random
import operator


def user_input():
    """
    Accepts a usser input and converts it to a integer values 
    If the value is not numerical value ot integer it will 
    display a value error
    """
    try:
        user_x = int(input("Range start value:"))
        user_y = int(input("Range end value:"))
    except ValueError:
        print("Invalid input. Please enter a valid integer.")
        not_integer = user_input()
        return not_integer
    return user_x, user_y


def data_validation(user_value_x, user_value_y):
    """
    Validates the input from the user and making sure that the first
    value is not bigger thatn the second value
    """
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
    random_x = (f"{random.randint(x, y)}")
    print(f"Random x: {random_x}")
    random_y = (f"{random.randint(x, y)}")
    print(f"Random y: {random_y}")
    return random_x, random_y


def random_opperator(x):
    """
    Creates a random operator and if the value of x
    is zero it will remove devide from the random choice
    """
    op = {"/": operator.truediv,
          "*": operator.mul,
          "-": operator.sub,
          "+": operator.add}
    if x == 0:
        op_pop = op.pop("/")
        no_devide_op = op
        randomes_no_devide = random.choice(list(no_devide_op.keys()))
        operater_op_no_devide = op.get(randomes_no_devide)
        print(randomes_no_devide)
        # print(no_devide_op)
        # print(op_pop)
        return randomes_no_devide, operater_op_no_devide
    else:
        devide_op = op
        randomes_devide = random.choice(list(devide_op.keys()))
        operater_op_devide = op.get(randomes_devide)
        print(randomes_devide)
        # print(devide_op)
        return randomes_devide, operater_op_devide


def math_question(x, y, rand_op_str, op_func):
    """
    Creates a Math equation and accepts a user input that
    evaluates wheter the user answer is right or wrong
    """
    print(f"what is the answer of = {y} {rand_op_str} {x}")
    # user_answer = float(input(" Your answer : "))
    # answer = y op x
    # print(f"This is the answer: {answer}")


def main():
    """
    This is the main function of that will run all the functions
    """
    user_input_x, user_input_y = user_input()
    x_range, y_range = data_validation(user_input_x, user_input_y)
    random_numb_x, random_numb_y = random_range_number(x_range, y_range)
    # print(f"random_numb_x: {random_numb_x}")
    # print(f"random_numb_y: {random_numb_y}")
    valuhate_x = int(random_numb_x)
    valuhate_y = int(random_numb_y)
    rand_op_str, op_func = random_opperator(valuhate_x)
    math_question(valuhate_x, valuhate_y, rand_op_str, op_func)


main()
