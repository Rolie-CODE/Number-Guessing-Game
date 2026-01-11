import random

def computer_guess(x):
    low = 1
    high = x
    feedback = ''
    attempts = 0

    while feedback != 'c': 
        attempts += 1
        if low != high:
            guess = random.randint(low, high)
        else:
            guess = low # could also be high since low == high

        feedback = input(f'Is {guess} too high (H), too low (L), or correct (C)? ').lower()
        if feedback == 'h':
            high = guess - 1
        elif feedback == 'l':
            low = guess + 1
    print(f'Yay! The computer guessed your number {guess} in {attempts} attempts.')


def user_guess(x):
    number = random.randint(1, x)
    guess = 0
    attempts = 0

    while guess != number:
        guess = int(input(f'Guess a number between 1 and {x}: '))
        attempts += 1
        if guess < number:
            print('Too low!')
        elif guess > number:
            print('Too high!')

    print(f'Congratulations! You guessed the number {number} in {attempts} attempts.')



def main():
    print("Welcome to the Number Guessing Game!")
    print("-----------------------------------")
    print("Choose a mode: ")
    print("U: You guess the computer's number")
    print("C: Computer guesses your number")
    mode = input("").lower()
    x = int(input("Enter the upper limit for the number range (1 to x): "))

    if mode == 'u':
        user_guess(x)
    elif mode == 'c':
        computer_guess(x)
    else:
        print("Invalid option. Please choose 'U' or 'C'.")


if __name__ == "__main__":
    main()
