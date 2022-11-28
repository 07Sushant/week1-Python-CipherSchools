# Excersie, number Guessing Game
# Make a variab;le, like winning_number and assign any number to it.
# Ask user to guess a number.
# if user guessed correct print "Win"

winning_number = 27
user_input = input("Guess a number b/w 1 and 100: ")
user_input = int(user_input)
if user_input == winning_number:
    print("YOU WIN !!!")
else:
    if user_input < winning_number:
        print("Too low")
    else:
        print("Too High")
