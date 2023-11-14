import math
import random
import operator
import time
import os
import sys


def user_input():
    """
    Accepts a user input and converts it to a integer value
    If the value is not numerical value or not integer it will
    display a value error
    """
    try:
        user_x = int(input("Range start value:"))
        user_y = int(input("Range end value:"))
        n_rounds = int(input("How many rounds would you like to play:"))
        print("\n")
    except ValueError:
        print(text_colors.FAIL +
              "Invalid input. Please enter a valid integer."
              + text_colors.ENDC)
        not_integer = user_input()
        return not_integer
    return user_x, user_y, n_rounds


def data_validation(user_value_x, user_value_y, rounds_playing):
    """
    Validates the input from the user and making sure that the first
    value is not bigger than the second value
    Prompts the user how many rounds they would like to play
    """
    while True:
        try:
            x = user_value_x
            y = user_value_y
            if y < x:
                print(text_colors.FAIL +
                      "Range end value must be larger than range start value"
                      + text_colors.ENDC)
                print(text_colors.FAIL + "Please try again\n"
                      + text_colors.ENDC)
                y_biger_than_x = user_input()
                return y_biger_than_x
            else:
                number_of_rounds = rounds_playing
                return x, y, number_of_rounds
        except ValueError as e:
            print(f"invalid data: {e}, please try again")
    return True


def random_range_number(x, y):
    """
    Accepts a number range input between two numbers from the user and
    randomize them
    """
    random_x = (f"{random.randint(x, y)}")
    random_y = (f"{random.randint(x, y)}")
    return random_x, random_y


def random_opperator(x):
    """
    Creates a random operator and if the value of x
    is zero it will remove divide from the random choice
    """
    op = {"/": operator.truediv,
          "*": operator.mul,
          "-": operator.sub,
          "+": operator.add}
    if x == 0:
        no_divide_op = op.pop("/")
        no_divide_op = op
        randoms_no_divide = random.choice(list(no_divide_op.keys()))
        operater_op_no_divide = op.get(randoms_no_divide)
        return randoms_no_divide, operater_op_no_divide
    else:
        divide_op = op
        randoms_divide = random.choice(list(divide_op.keys()))
        operater_op_divide = op.get(randoms_divide)
        return randoms_divide, operater_op_divide


def math_question(x, y, rand_op_str, op_func):
    """
    Creates a Math equation and accepts a user input that
    evaluates whether the user answer is right or wrong
    """
    while True:
        try:
            print(f"What is the answer of: {y} {rand_op_str} {x}")
            user_answer = float(input("Your answer: "))
            answer = op_func(y, x)
            print(f"This is the answer: {answer}")
            if answer == user_answer:
                print(text_colors.OKGREEN + "Correct!" + text_colors.ENDC)
                break
            else:
                print(text_colors.WARNING + "Incorrect!" + text_colors.ENDC)
                break
        except ValueError:
            print(text_colors.FAIL +
                  "Invalid input. Please enter a valid value."
                  + text_colors.ENDC)
            print("\n")
            continue
    return answer, user_answer


def type_writer(text):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.02)


def restart():
    """
    Restart the game yes or no
    """
    print("Do you want to play again ?")
    replay_game = str(input("'y' for Yes, 'n' for No: ")).lower()
    print("\n")
    if replay_game == "y":
        main()
    elif replay_game == "n":
        type_writer(text_colors.OKBLUE + "Thank you for playing!"
                    + text_colors.ENDC)
        print("\n")
    else:
        print(text_colors.FAIL + "Invalid input" + text_colors.ENDC)
        retry_game = restart()
        return retry_game


class text_colors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


def main():
    """
    This is the main function that will run all the functions
    Keeps score of the quiz
    """
    type_writer(text_colors.OKBLUE + r"""
      __  __           _     _
     |  \/  |         | |   | |
     | \  / |   __ _  | |_  | |__
     | |\/| |  / _` | | __| | '_ \
     | |  | | | (_| | | |_  | | | |
     |_|  |_|  \__,_|  \__| |_| |_|

       ____            _           _
      / __ \          (_)         | |
     | |  | |  _   _   _   ____   | |
     | |  | | | | | | | | |_  /   | |
     | |__| | | |_| | | |  / /    |_|
      \___\_\  \__,_| |_| /___|   (_)
    """ + text_colors.ENDC)
    print("\n")
    print(r"""How to play: 1. Select a start value for a range of values
             2. Select a end value for the range of numbers
             3. Select how many games you want to play
             4. Test your math skills """)
    print("\n")
    user_input_x, user_input_y, rounds = user_input()
    x_range, y_range, n_of_rounds = data_validation(user_input_x,
                                                    user_input_y, rounds)
    main_score = 0
    for i in range(n_of_rounds):
        random_numb_x, random_numb_y = random_range_number(x_range, y_range)
        valuate_x = int(random_numb_x)
        valuate_y = int(random_numb_y)
        rand_op_str, op_func = random_opperator(valuate_x)
        c_ans, u_ans = math_question(
            valuate_x, valuate_y, rand_op_str, op_func)
        if c_ans == u_ans:
            main_score += 1
            type_writer(f"Your score is: {main_score} out of {n_of_rounds}")
            print("\n")
        else:
            type_writer(f"Your score is: {main_score} out of {n_of_rounds}")
            print("\n")
    restart()


main()
