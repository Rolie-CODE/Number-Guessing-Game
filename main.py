import random

from tkinter import *


top_of_range = 100
random_number = random.randint(1,top_of_range)
guesses = 0
def main():
        global guesses
        guesses += 1
        user_guess = window.user_guess.get()
        if user_guess.isdigit():
            user_guess = int(user_guess)
        else:
            result_label.config(text="Enter a number next time")
            return

        if user_guess == random_number:
            result_label.config(text="Congratulations you got it correct!!")
            return
        else:
            if user_guess > random_number:
                result_label.config(text="Your guess is high, try again!! ")
            else:
                result_label.config(text="Your guess is low, try again!!")
        number_of_guesses_label.config(text=f"Number of guesses: {guesses}")
        window.user_guess.delete(0, END)





window = Tk()

window.title("Number Guessing Game")

window.geometry("400x300")


window.label = Label(window, text="Welcome to the Number Guessing Game!", font=("Arial", 16))

window.label.pack(pady=20)

window.instructions = Label(window, text="Guess a number between 1 and 100", font=("Arial", 12))

window.instructions.pack(pady=10)

window.user_guess = Entry(window, width=20)

window.user_guess.pack(pady=10)

Label(window, text="Enter your guess above and press Submit", font=("Arial", 10)).pack(pady=5)

Button(window, text="Submit", command=main).pack(pady=20)

result_label = Label(window, text="", font=("Arial", 12))

result_label.pack(pady=10)

number_of_guesses_label = Label(window, text= f"Number of guesses: {guesses}", font=("Arial", 10))

number_of_guesses_label.pack(pady=5)


window.mainloop()
