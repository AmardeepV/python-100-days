import random


def main():
    print("Welcome to the number guessing game")
    print("I'm thinking of a number between 1 and 100.")
    computer_guess = random.randint(1, 100)
    # print(f"computer number is {computer_guess}")
    selected_level = input(
        "Choose a dificulty. Type \'easy\' or \'hard\': ").lower()

    difficulty_level = {
        "easy": 10,
        "hard": 5
    }

    attempt_remaining = 0
    valid = True

    for i in difficulty_level:
        if selected_level == i:
            attempt_remaining = difficulty_level[i]

    while valid:
        print(
            f"You have {attempt_remaining} attempt remaining to guess the number.")
        guessed_number = int(input("Make a guess: "))

        if attempt_remaining >= 1:
            if guessed_number > computer_guess:
                print("Too high.\nGuess again. ")
                attempt_remaining -= 1
            elif guessed_number < computer_guess:
                print("Too low.\nGuess again. ")
                attempt_remaining -= 1
            else:
                print(f"You got it! The answer was {computer_guess}")
                valid = False

        else:
            print("You have run out of guesses, you lose.")
            valid = False


if __name__ == '__main__':
    main()
