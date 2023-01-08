#!/usr/bin/env python3

# Created By: Kestrel Bryce
# Date: Dec. 20, 2022
# This program asks the user
# to input a sentence, and the
# program will display the
# individual words separately


def string_parser(user_input):
    # initializing list
    a_string_list = []
    # initializing word
    word = ""
    # initializing length_of_string
    length_of_string = len(user_input)
    # initializing counter
    counter = 0
    # starting loop
    while counter < length_of_string:
        # test code
        # print(user_input[counter])

        # assigning current_char
        current_char = user_input[counter]
        # checking if word is over
        if current_char == " ":
            # adding word to list
            a_string_list.append(word)
            # reassigning word
            word = ""
        elif counter == length_of_string - 1:
            # adding to word
            word = word + current_char
            # adding word to list
            a_string_list.append(word)
        else:
            # adding to word
            word = word + current_char
        # incrementing counter
        counter = counter + 1
    return a_string_list


def main():
    # introductory paragraph
    print("This program asks the user")
    print("to input a sentence, and the")
    print("program will display the")
    print("individual words separately")
    print("")

    # Getting user_input
    user_input = input("Enter a sentence: ")

    # calling function
    split_sentence = string_parser(user_input)

    words_num = len(split_sentence)

    counter = 0

    # starting loop
    while counter < words_num:
        # displaying results
        print(split_sentence[counter])
        # incrementing counter
        counter = counter + 1


if __name__ == "__main__":
    main()
