#!/usr/bin/env python3

# Created By: Kestrel Bryce
# Date: Dec. 20, 2022
# This program asks the user
# to input a sentence, and the
# program will display the
# individual words separately

import math
import random
# import lists


def string_parser(grade_num_list):
    # initializing sum
    sum = 0
    for a_single_number in grade_num_list:
        # reassigning sum
        sum = sum + a_single_number
    # initializing num_amount
    num_amount = len(grade_num_list)
    # checking for errors
    if num_amount == 0:
        return -1
    # returning as normal
    else:
        final_sum = sum / num_amount
        return final_sum


def main():
    # introductory paragraph
    print("This program asks the user")
    print("to input a sentence, and the")
    print("program will display the")
    print("individual words separately")
    print("")

    # initializing list
    grade_num_list = []

    # Getting user_input
    user_input = input("Enter a sentence: ")

    # generating numbers
    while True:
        # initializing current_char
        current_char = user_input
        # checking to see if loop continues
        if user_input == "stop":
            break
        # checking valid input
        # what valid input is there to check???

        # checking if input is within range
        if user_input_int > 100 or user_input_int < 0:
            print("Please enter a grade between 1 and 100.")
            continue
        else:
            # adding input to list
            grade_num_list.append(user_input_int)

    # calling function
    true_sum = string_parser(grade_num_list)

    # checking results
    if true_sum == -1:
        # error message (not enough grades)
        print("Please enter two or more grades.")
    else:
        # displaying results
        print("The average grade is {}%.".format(true_sum))


if __name__ == "__main__":
    main()
