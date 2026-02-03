import requests
import random

word_site = "https://www.mit.edu/~ecprice/wordlist.10000"


def fetch_word():

    response = requests.get(word_site)
    WORDS = response.content.splitlines()

    result = [
        word.decode("utf-8")
        for word in WORDS
        if 3 <= len(word.decode("utf-8")) <= 5
    ]

    words_list = []
    for i in range(0, 100):
        words_list.append(random.choice(result))

    print(words_list)
    print(len(words_list))


def pick_word():
    words_list = ['robin', 'photo', 'alex', 'news', 'grill', 'betty', 'offer', 'cake', 'mouth', 'words', 'dave',
                  'color', 'bear', 'dame', 'nat', 'bold', 'soma', 'usgs', 'joint', 'edges', 'knee', 'keep', 'awful',
                  'tight', 'drain', 'acm', 'agent', 'trunk', 'woman', 'rocky', 'pilot', 'mpegs', 'tiny', 'congo',
                  'alter', 'edgar', 'jon', 'lol', 'gauge', 'devon', 'rover', 'fell', 'male', 'cloud', 'plate', 'pct',
                  'tight', 'reset', 'feb', 'mrs', 'cup', 'lions', 'disk', 'pdt', 'por', 'gps', 'tamil', 'pearl', 'happy',
                  'firm', 'ways', 'rapid', 'mice', 'hood', 'ought', 'pain', 'and', 'rica', 'betty', 'piss', 'level', 'bbw',
                  'grain', 'promo', 'dock', 'hist', 'ali', 'tony', 'red', 'ati', 'shape', 'oclc', 'door', 'state', 'fox',
                  'cult', 'agree', 'ripe', 'keys', 'meat', 'seems', 'ugly', 'booth', 'clip', 'strap', 'basis', 'navy',
                  'taken', 'teeth', 'diane']

    return random.choice(words_list)


def main():

    STAGES = [
        '''
         +----+
         |    |
         O    |
        /|\   |
        / \   |
              |
        =========
        ''', '''
         +----+
         |    |
         O    |
        /|\   |
        /     |
              |
        =========
        ''', '''
         +----+
         |    |
         O    |
        /|\   |
              |
              |
        =========
        ''', '''
         +----+
         |    |
         O    |
        /|    |
              |
              |
        =========
        ''', '''
         +----+
         |    |
         O    |
         |    |
              |
              |
        =========
        ''', '''
         +----+
         |    |
         O    |
              |
              |
              |
        =========
        ''', '''
         +---+
         |   |
             |
             |
             |
             |
        =========
        ''']
    total_life = 6
    pick_one_word = pick_word()
    word_guessed = ''
    game_over = False

    print(f"word is {pick_one_word}")

    for i in pick_one_word:
        word_guessed += '_'
    print(word_guessed)

    while not game_over:
        enter_letter = input('Guess a letter: ').lower()

        if enter_letter in pick_one_word:
            if enter_letter not in word_guessed:
                for pos, letter in enumerate(pick_one_word):
                    if enter_letter == letter:
                        lis = list(word_guessed)
                        lis[pos] = enter_letter
                        word_guessed = ''.join(lis)
                print(word_guessed)
            else:
                print("You have already used that letter, try other.")
        else:
            total_life -= 1
            print(STAGES[total_life])
            if total_life == 0:
                print("Game Over")
                game_over = True
                print("You lost.")

        if '_' not in word_guessed:
            print("Game Over")
            game_over = True
            print("You win.")


if __name__ == '__main__':
    main()
    # fetch_word()
