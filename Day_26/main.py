import pandas

nato_data = pandas.read_csv('nato_phonetic_alphabet.csv')
nato_code = {word.letter: word.code for (ind, word) in nato_data.iterrows()}

user_input = input("Enter a word: ").upper()
# split_user_input = [n.upper() for n in user_input]

# word_for_letter = [value for letter in split_user_input for key,
#                    value in nato_code.items() if letter == key]

word_for_letter = [nato_code[letter] for letter in user_input]
print(word_for_letter)
