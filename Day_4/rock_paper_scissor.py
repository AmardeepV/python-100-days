import random


def main():
    rock = '''
        _______
    ---'   ____)
        (_____)
        (_____)
        (____)
    ---.__(___)
    '''

    paper = '''
        _______
    ---'   ____)____
            ______)
            _______)
            _______)
    ---.__________)

    '''

    scissors = '''
        _______
    ---'   ____)____
            ______)
        __________)
        (____)
    ---.__(___)

    '''

    input_choice = int(input(
        "What do you choose? Type 0 for Rock, 1 for paper or 2 for scissors \n"))
    if 0 <= input_choice <= 2:
        if input_choice == 0:
            print(rock)
        if input_choice == 1:
            print(paper)
        if input_choice == 2:
            print(scissors)

        computer_chose = random.choice(['rock', 'paper', 'scissors'])
        print("Computer chose:")
        if computer_chose == 'rock':
            print(rock)
        if computer_chose == 'paper':
            print(paper)
        if computer_chose == 'scissors':
            print(scissors)

        # cases
        if (input_choice == 0 and computer_chose == 'paper') or (input_choice == 1 and computer_chose == 'scissors') or (input_choice == 2 and computer_chose == 'rock'):
            print("You lose")
        elif (input_choice == 0 and computer_chose == 'scissors') or (input_choice == 1 and computer_chose == 'rock') or (input_choice == 2 and computer_chose == 'paper'):
            print('You win')
        else:
            print("Draw")
    else:
        print("Please only enter a number from 0 to 2")


if __name__ == '__main__':
    main()
