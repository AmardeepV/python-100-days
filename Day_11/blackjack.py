import random


def blackjack(counter):
    logo = '''
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \\/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \\  /|K /\\  |     | '_ \\| |/ _' |/ __| |/ / |/ _' |/ __| |/ /
|  \\/ | /  \\ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
'-----| \\  / |     |_.__/|_|\\__,_|\\___|_|\\_\\ |\\__,_|\\___|_|\\_\\
      |  \\/ K|                            _/ |                
      '------'                           |__/           
'''

    cards = {
        1: 1,
        2: 2,
        3: 3,
        4: 4,
        5: 5,
        6: 6,
        7: 7,
        8: 8,
        9: 9,
        10: 10,
        'J': 10,
        'Q': 10,
        'K': 10,
        'A': 11
    }
    player_card = []
    computer_card = []
    valid = True
    hit = True
    stand = True
    next_move = ''
    if counter == 0:
        print(logo)

    while valid:
        for i in range(2):
            player_card.append(random.choice(list(cards.keys())))
        computer_card.append(random.choice(list(cards.keys())))

        print_cards(player_card, computer_card, cards)
        computer_card.append(random.choice(list(cards.keys())))
        if player_total_score(player_card, cards) == 21:
            if computer_total_score(computer_card, cards) == 21:
                print("Draw")
                valid = False
                return
            else:
                print("Black Jack, User win")
                valid = False
                return

        while hit:
            next_move = next_move_check()
            if next_move == "hit":
                player_card.append(random.choice(list(cards.keys())))
                print(
                    f"Your cards: {player_card}, current score: {player_total_score(player_card,cards)}")

                if player_total_score(player_card, cards) > 21:
                    print("You went over. You lose")
                    hit = False
                    valid = False
                    return
            if next_move == "stand":
                hit = False
        while stand:
            if next_move == "stand":
                if (computer_total_score(computer_card, cards) > player_total_score(player_card, cards)) and computer_total_score(computer_card, cards) <= 21:
                    print(
                        f"Computer's cards: {computer_card}, current score: {computer_total_score(computer_card,cards)}")
                    print("You lost")
                    hit = False
                    valid = False
                    return
                elif computer_total_score(computer_card, cards) == player_total_score(player_card, cards) == 21:
                    print(
                        f"Computer's cards: {computer_card}, current score: {computer_total_score(computer_card,cards)}")
                    print("Draw")
                    hit = False
                    valid = False
                    return
                elif computer_total_score(computer_card, cards) > 21:
                    print(
                        f"Computer's cards: {computer_card}, current score: {computer_total_score(computer_card,cards)}")
                    print("computer score went over ")
                    print("You win")
                    hit = False
                    valid = False
                    return
                else:
                    print(
                        f"Computer's cards: {computer_card}, current score: {computer_total_score(computer_card,cards)}, pulling one more card")
                    computer_card.append(random.choice(list(cards.keys())))


def next_move_check():
    output = input(
        "Type \'Hit\' to get another card, type \'stand\' to pass: ").lower()
    return output


def print_cards(player_card, computer_card, cards):
    print(
        f"Your cards: {player_card}, current score: {player_total_score(player_card,cards)}")
    print(
        f"Computer's cards: {computer_card}, current score: {computer_total_score(computer_card,cards)}")


def player_total_score(player_card, cards):
    player_total_score = 0
    for i in player_card:
        player_total_score += cards[i]
    return player_total_score


def computer_total_score(computer_card, cards):
    computer_total_score = 0
    for i in computer_card:
        computer_total_score += cards[i]
    return computer_total_score


def main():
    play_game = True
    counter = 0
    while play_game:
        game = input(
            "Do you want to play a game of Blackjack? Type \'y\' or \'n\': ")
        if game == 'y':
            blackjack(counter)
            counter += 1
        else:
            play_game = False


if __name__ == '__main__':
    main()


# ToDo

# 3. Add the logic of A to swith from 1 to 11 and vice - versa
