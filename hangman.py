def start_screen():
    print("Welcome to the hangman game!")

def show_credits():

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
    letter = input("Guess a letter:")
    return letter

def display_board(solved):
    print(solved)

def show_result():
    print("You win!")

def play_again():
    while True:
        decision = input("Would you like to play again? (y/n) ")

        if decision == 'y' or decision == 'yes':
            return True
        elif decision == 'n' or decision == 'no':
            return False
        else:
            print("I don't understand. Please enter 'y' or 'n'.")
    
def play():
    puzzle = get_puzzle()
    guess = ""
    solved = get_solved(puzzle, guesses)
    display_board(solved)

    while solved != puzzle:
        guesses += get_guess()
        solved = get_solved(puzzle, guesses)
        display_board(solved)

    
#Game starts running here
show_start_screen()

playing = True

while playing:
    play()
    show_result()
    playing = play_again()

show_credits
