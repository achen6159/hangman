#Hangman Game
#
#12/12/17
#Annie C.

import time
import random
import os

game_play = True
while game_play:
    name = input("Please enter your name")
    def show_start_screen():
        with open("Art/splash.txt" , 'r') as f:
            splash = f.read()
            print(splash)
            
        time.sleep(0.1)
        print("Let's play hangman!!" + str(name))

    def show_credits():
        time.sleep(0.2)
        print("********************************************")
        time.sleep(0.2)
        print("**This awesome game was created by Annie****")
        time.sleep(0.2)
        print("**This was completed on the 17 of November**")
        time.sleep(0.2)
        print("********************************************")
        
    def get_puzzle():
        path = "Puzzles"

        file_names = os.listdir(path)

        for i, f in enumerate(file_names):
            this_file = f
            with open(path + "/" + this_file, 'r') as f:
                beginning_lines = f.read().splitlines()
            category_name = beginning_lines[0]
            print(str(i + 1) + ") " + category_name)

        choice = input('pick one: ')
        choice = int(choice)

        file = path + "/" + file_names[choice - 1]

        with open(file, 'r') as f:
            lines = f.read().splitlines()
        this_word = lines[0]
        print(this_word)

        words = random.choice( lines[1: ] )
        return str.lower(words)

    def get_solved(puzzle, guesses):
        solved = ""

        for letter in puzzle:
            if letter in guesses:
                solved += letter
            elif letter == " ":
                solved += " "
            else:
                solved += "-"

        return solved

    def get_guess():
        while True:
            letter = input("Guess a letter " + str(name) + ":")

            if len(letter) == 1:
                return letter
            else:
                print("I don't understand " + str(name) + "." + "Enter a letter please.")
        
            
    def display_board(solved, strikes, right_guesses, wrong_guesses):
        print(solved)
        print("Strikes: " + str(strikes))
        print("Right guesses: " + str(right_guesses))
        print("Wrong guesses: " + str(wrong_guesses))
        
    def show_result(strikes):
        if strikes < limit:
            print("You win!!!! " + str(name))
        else:
            print("Your not good enough " + str(name) + ".")
            print("The word was " + str.lower(words))

    def play_again():
        while True:
            decision = input("Would you like to play again " + str(name) + "? (y/n) ")

            if decision == 'y' or decision == 'yes':
                return True
            elif decision == 'n' or decision == 'no':
                return False
            else:
                print("I don't understand " + str(name) + "." + "Please enter 'y' or 'n'.")
        
    def play(strikes, limit):
        puzzle = get_puzzle()
        guesses = ""
        right_guesses = ""
        wrong_guesses = ""
        solved = get_solved(puzzle, guesses)

        print(solved)

        while solved != puzzle:
            letter = get_guess()

            if letter not in puzzle:
                strikes += 1
                wrong_guesses += letter
                if strikes == limit:
                    break
            else:
                right_guesses += letter
                
            guesses += letter
            solved = get_solved(puzzle, guesses)
            display_board(solved, strikes, right_guesses, wrong_guesses)

        show_result(strikes)

    #Game starts running here
    show_start_screen()

    playing = True

    while playing:
        strikes = 0
        limit = 6

        print("You have " + str(limit) + " tries")
        play(strikes, limit)
        playing = play_again()

    show_credits()
                     

