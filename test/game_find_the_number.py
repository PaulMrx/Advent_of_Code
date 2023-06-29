from getpass import getpass
from random import choices

def main():

    print()
    print("Player 1")
    number = get_number()
    guess = get_guess()
    print()
    print("Player 2")
    print(f"You have {guess} chances to find the Number")
    game(number, guess)

# Get "Number" from Player 1
def get_number():
    while True:
        try:
# Use getpass instead of input() to hide the user input
            n = int(getpass("Please choose a number (0 - 100):"))
            if 0 <= n <= 100:
                return n
            else:
                print("Please make sure the number is between 0 and a 100")
        except ValueError:
            print("Error: number has to be an integer")

# Get "Amount of chances" from Player 1         
def get_guess():
    while True:
        try:
# Use getpass instead of input() to hide the user input
            g = int(getpass("How many chances (5 - 20):"))
            if 5 <= g <= 20:
                return g
            else:
                print("Please make sure chances are between 5 and a 20")
        except ValueError:
            print("Error: chances has to be an integer")

    
# Game per se: Player has to find Player 1's number
def game(number, guess):
    
    for i in range(guess):
        n = int(input("What's the number: "))
# Player 1 wins
        if n != number and i == guess-1:
            print("You loose! :(")
            break
# Give a clue to help find the number
        elif n < number and i != guess:
            print("You're too low!")
            continue
        elif n > number and i != guess:
            print("You're too high!")
            continue
# Player 2 wins
        elif n == number:
            print("You win! :D")
            print()
            break


# Do you want to play, replay or quit?
while True:
    play = input("Do you want to play? [Y/N]  ").strip().upper()
    if play == "N":
        break
    else:
        main()


# Next step: Add a 1 player version with random inputs