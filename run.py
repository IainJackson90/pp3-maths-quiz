import math
import random
import operator
import time,os,sys


def user_input():
    """
    Accepts a user input and converts it to a integer values
    If the value is not numerical value or not integer it will
    display a value error
    """
    try:
        user_x = int(input("Range start value:"))
        user_y = int(input("Range end value:"))
        print("How many rounds would you like to play:")
        n_rounds = int(input())
        print("\n")
    except ValueError:
        print("Invalid input. Please enter a valid integer.")
        not_integer = user_input()
        return not_integer
    return user_x, user_y, n_rounds


def data_validation(user_value_x, user_value_y, rounds_playing):
    """
    Validates the input from the user and making sure that the first
    value is not bigger than the second value
    """
    while True:
        try:
            x = user_value_x
            y = user_value_y
            if y < x:
                print("Range end value must be larger than range start value")
                print("pleas try again\n")
                y_biger_than_x = user_input()
                return y_biger_than_x
            else:
                number_of_rounds = rounds_playing
                return x, y, number_of_rounds
        except ValueError as e:
            print(f"invalid data: {e}, pleas try again")
    return True


def random_range_number(x, y):
    """
    Accepts a number range input between two numbers from the uses and
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
        no_devide_op = op.pop("/")
        no_devide_op = op
        randomes_no_devide = random.choice(list(no_devide_op.keys()))
        operater_op_no_devide = op.get(randomes_no_devide)
        return randomes_no_devide, operater_op_no_devide
    else:
        devide_op = op
        randomes_devide = random.choice(list(devide_op.keys()))
        operater_op_devide = op.get(randomes_devide)
        return randomes_devide, operater_op_devide


def math_question(x, y, rand_op_str, op_func):
    """
    Creates a Math equation and accepts a user input that
    evaluates whether the user answer is right or wrong
    """
    while True:
        try:
            print(f"what is the answer of = {y} {rand_op_str} {x}")
            user_answer = float(input("Your answer : "))
            answer = op_func(y, x)
            print(f"This is the answer: {answer}")
            if answer == user_answer:
                print("Corect!")
                break
            else:
                print("Incorrect!")
                break
        except ValueError:
            print("Invalid input. Please enter a valid value.")
            print("\n")
            continue
    return answer, user_answer
    

def type_writer(text):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.01)
    

def main():
    """
    This is the main function of that will run all the functions
    Keeps score of the quizz
    """
    type_writer(r"""
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
    """)
    print("\n")
    print(r"""How to play: 1. Select a start value for a range of values
             2. Slect a end value for the range of numbers
             3. Select how many games you want to play
             4. Test your math skils """)
    print("\n")
    user_input_x, user_input_y, rounds = user_input()
    x_range, y_range, n_of_rounds = data_validation(user_input_x,
                                                    user_input_y, rounds)
    main_score = 0
    for i in range(n_of_rounds):
        random_numb_x, random_numb_y = random_range_number(x_range, y_range)
        valuhate_x = int(random_numb_x)
        valuhate_y = int(random_numb_y)
        rand_op_str, op_func = random_opperator(valuhate_x)
        c_ans, u_ans = math_question(
            valuhate_x, valuhate_y, rand_op_str, op_func)
        if c_ans == u_ans:
            main_score += 1
            print(f"Your score is: {main_score} out of {n_of_rounds}")
            print("\n")
        else:
            print(f"Your score is: {main_score}  out of {n_of_rounds} ")
            print("\n")


main()
