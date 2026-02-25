# TODO: Create a letter using starting_letter.txt
# for each name in invited_names.txt
# Replace the [name] placeholder with the actual name.
# Save the letters in the folder "ReadyToSend".

# Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
# Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
# Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

NAME = "./Input/Names/invited_names.txt"
LETTER = "./Input/Letters/starting_letter.txt"
OUTPUT_FILE = "./Output/ReadyToSend/"

modified_name_list = []

with open(NAME) as data:
    original_name_list = data.readlines()

for name in original_name_list:
    modified_name_list.append(name.strip('\n'))

for name in modified_name_list:
    with open(LETTER) as l:
        txt = l.read()
        replaced_txt = txt.replace("[name]", name)
        file_name = f"letter for {name}.txt"
        with open(OUTPUT_FILE + file_name, 'w') as file:
            file.write(replaced_txt)
