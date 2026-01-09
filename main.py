import random
from tkinter import *

top_of_range = input("Enter a number: ")
if top_of_range.isdigit():
    top_of_range = int(top_of_range)

    if top_of_range <= 0:
        print("Please type a number greater than 0 next time")
        quit()
else:
    print("Please type a number less time")
    quit()

random_number = random.randint(0,top_of_range)
guesses = 0

while True:
    guesses += 1
    user_guess = input("Enter your guess: ")
    if user_guess.isdigit:
        user_guess = int(user_guess)
    else:
        print("Enter a number next time")
        continue

    if user_guess == random_number:
        print("Congratulations you got it correct!!")
        break
    else:
        if user_guess > random_number:
            print("Your guess is high, try again!! ")
        else:
            print("Your guess is low, try again!!")
    
print(f"You got it in {guesses} guesses")

window = Tk()

window.mainloop()
