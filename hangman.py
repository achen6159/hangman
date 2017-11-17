#Hangman Game
#
#11/13/17
#Annie C.

import time

game_play = True
while game_play:
    name = input("Please enter your name")
    print("Would you like to play in English or French?")
    language = input("If you want to play in English say Englsih or if you want to play in French, say French")

    if str.lower(language) == "english":

        def show_start_screen():
            print("______§§____________§§")
            print("_____§__§__________§__§")
            print("___§§____§_________§___§")
            print("__§___§___§_______§____§")
            print("_§____§____§_____§____§")
            print("_§___§_§____§___§____§")
            print("_§§§§___§___§§§§§___§")
            print("_________§_________§___§§_§§")
            print("________§___§§_§§___§_§§§c§§§")
            print("_______§_____________§_§d§§§")
            print("_______§______§______§__§§§")
            print("_______§____§___§____§___§")
            print("________§____§§§____§___§")
            print("_______§§§§§_____§§§§§_§")
            print("_§§§__§_____§§§§§_____§__§§§")
            print("§_§_§§____§_______§__§_§§_§_§")
            print("§____§_____§_____§__§__§____§")
            print("_§____§____§_____§_§__§____§")
            print("__§____§§§§_______§§§§____§")
            print("___§____§___________§____§")
            print("____§____§§§_____§§§____§")
            print("_____§§§§___§§§§§___§§§§")

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
            return "This is hangman"

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
                print("You winn!!!! " + str(name))
            else:
                print("Your not good enough " + str(name) + ".")

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
                         
    elif str.lower(language) == "french":
        def show_start_screen():

            print("______§§____________§§")
            print("_____§__§__________§__§")
            print("___§§____§_________§___§")
            print("__§___§___§_______§____§")
            print("_§____§____§_____§____§")
            print("_§___§_§____§___§____§")
            print("_§§§§___§___§§§§§___§")
            print("_________§_________§___§§_§§")
            print("________§___§§_§§___§_§§§c§§§")
            print("_______§_____________§_§d§§§")
            print("_______§______§______§__§§§")
            print("_______§____§___§____§___§")
            print("________§____§§§____§___§")
            print("_______§§§§§_____§§§§§_§")
            print("_§§§__§_____§§§§§_____§__§§§")
            print("§_§_§§____§_______§__§_§§_§_§")
            print("§____§_____§_____§__§__§____§")
            print("_§____§____§_____§_§__§____§")
            print("__§____§§§§_______§§§§____§")
            print("___§____§___________§____§")
            print("____§____§§§_____§§§____§")
            print("_____§§§§___§§§§§___§§§§")

            time.sleep(0.1)
            print("D'ac jouer au Hangman!!" + str(name))

        def show_credits():
            time.sleep(0.2)
            print("*******************************************")
            time.sleep(0.2)
            print("**Ce jeu génial a été créé par by Annie****")
            time.sleep(0.2)
            print("******Cela a été fait le 17 novembre*******")
            time.sleep(0.2)
            print("*******************************************")
            
        def get_puzzle():
            return "This is hangman."

        def get_solved(puzzle, guesses):
            solved = ""

            for letter in puzzle:
                if letter in guesses:
                    solved += letter
                elif letter == " ":
                    solved == " "
                else:
                    solved += "-"

            return solved

        def get_guess():
            while True:
                letter = input("Deviner une lettre "  + str(name) + ":")

                if len(letter) == 1:
                    return letter
                else:
                    print("Je ne comprends pas " + str(name) + "." + "Entrez une lettre s’il vous plaît.")
            
                
        def display_board(solved, strikes, right_guesses, wrong_guesses):
            print(solved)
            print("Grèves: " + str(strikes))
            print("Suppositions droite: " + str(right_guesses))
            print("Suppositions mal: " + str(wrong_guesses))
            
        def show_result(strikes):
            if strikes < limit:
                print("Vous gagnez!!!! " + str(name))
            else:
                print("Vous n’êtes pas assez bon " + str(name) + ".")

        def play_again():
            while True:
                decision = input("Vous souhaitez rejouer " + str(name) + "? (o/n) ")

                if decision == 'o' or decision == 'oui':
                    return True
                elif decision == 'n' or decision == 'non':
                    return False
                else:
                    print("Je ne comprends pas " + str(name) + "." + "S’il vous plaît entrer 'o' ou 'n'.")
            
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

            print("Vouz avez " + str(limit) + " d'essais")
            play(strikes, limit)
            playing = play_again()

        show_credits()
                         
else:
    print("Please say English or French.")
