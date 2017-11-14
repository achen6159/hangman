#Hangman Game
#
#Annie C.


def show_start_screen():
    print("Welcome to the hangman game!")

def show_credits():
    pass
def get_puzzle():
    return "hangman"

def get_solved(puzzle, guesses):
    solved = ""

    for letter in puzzle:
        if letter in guesses:
            solved += letter
        else:
            solved += "-"

    return solved

def get_guess():
    while True:
        letter = input("Guess a letter: ")

        if str(letter) == 1:
            return letter
        else:
            print("I don't understand. Enter a letter please.")
    
        
def display_board(solved, strikes):
    print(solved)
    print("Strikes: " + str(strikes))
    
def show_result(strikes):
    if strikes < limit:
        print("You winn!!!!")
    else:
        print("Your not good enough")

def play_again():
    while True:
        decision = input("Would you like to play again? (y/n) ")

        if decision == 'y' or decision == 'yes':
            return True
        elif decision == 'n' or decision == 'no':
            return False
        else:
            print("I don't understand. Please enter 'y' or 'n'.")
    
def play(strikes, limit):
    puzzle = get_puzzle()
    guesses = ""
    solved = get_solved(puzzle, guesses)
    display_board(solved, strikes)

    print(solved)

    while solved != puzzle:
        letter = get_guess()

        if letter not in puzzle:
            strikes += 1
            if strikes == limit:
                break
            
        guesses += letter
        solved = get_solved(puzzle, guesses)
        display_board(solved, strikes)

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
