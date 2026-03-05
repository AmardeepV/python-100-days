import pandas
nato_data = pandas.read_csv('nato_phonetic_alphabet.csv')
nato_code = {word.letter: word.code for (ind, word) in nato_data.iterrows()}


def generate_phonotics():
    user_input = input("Enter a word: ").upper()
    try:
        word_for_letter = [nato_code[letter] for letter in user_input]
    except KeyError:
        print("Sorry, only letters in the alphabet please.")
        generate_phonotics()
    else:
        print(word_for_letter)


generate_phonotics()
