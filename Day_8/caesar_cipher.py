
alphabet = [
    "a",
    "b",
    "c",
    "d",
    "e",
    "f",
    "g",
    "h",
    "i",
    "j",
    "k",
    "l",
    "m",
    "n",
    "o",
    "p",
    "q",
    "r",
    "s",
    "t",
    "u",
    "v",
    "w",
    "x",
    "y",
    "z"
]


'''
################# Method 1 ################################

def encrypt(original_text, shift_amount):
    encrypt_text = ''
    for i in original_text:
        indx = alphabet.index(i)
        shifted_position = indx + shift_amount
        shifted_position = shifted_position % len(alphabet)
        encrypt_text += alphabet[shifted_position]
    print(encrypt_text)


def decode(original_text, shift_amount):
    decode_text = ''
    for i in original_text:
        indx = alphabet.index(i)
        shifted_pos = indx - shift_amount
        shifted_pos %= len(alphabet)
        decode_text += alphabet[shifted_pos]
    print(decode_text)
'''

################### Method 2 ###############################


def caesar(original_text, shift_amount, encode_or_decode, re_run):
    output_text = ''
    if encode_or_decode == 'decode':
        shift_amount *= -1

    for i in original_text:
        if i in alphabet:
            indx = alphabet.index(i)
            shifted_pos = indx + shift_amount
            shifted_pos %= len(alphabet)
            output_text += alphabet[shifted_pos]
        else:
            output_text += i
    print(f"Here is the {encode_or_decode} result: {output_text}")


def main():
    logo = '''    
    ,adPPYba, ,adPPYYba,  ,adPPYba, ,adPPYba, ,adPPYYba, 8b,dPPYba,  
    a8"     "" ""     'Y8 a8P_____88 I8[    "" ""     'Y8 88P'   "Y8  
    8b         ,adPPPPP88 8PP"""""""  '"Y8ba,  ,adPPPPP88 88          
    "8a,   ,aa 88,    ,88 "8b,   ,aa aa    ]8I 88,    ,88 88          
    '"Ybbd8"' '"8bbdP"Y8  '"Ybbd8"' '"YbbdP"' '"8bbdP"Y8 88   
                88             88                                 
            ""             88                                 
                            88                                 
    ,adPPYba, 88 8b,dPPYba,  88,dPPYba,   ,adPPYba, 8b,dPPYba,  
    a8"     "" 88 88P'    "8a 88P'    "8a a8P_____88 88P'   "Y8  
    8b         88 88       d8 88       88 8PP""""""" 88          
    "8a,   ,aa 88 88b,   ,a8" 88       88 "8b,   ,aa 88          
    '"Ybbd8"' 88 88'YbbdP"'  88       88  '"Ybbd8"' 88          
                88                                             
                88           
    '''
    print(logo)

    # if direction == 'encode':
    #     encrypt(text, shift)
    # elif direction == 'decode':
    #     decode(text, shift)
    # else:
    #     print("Wrong entry: enter encode to encode and decode to decode the message")
    re_run = True
    while re_run:
        direction = input(
            "Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
        text = input("Type your message: \n").lower()
        shift = int(input("Type the shift number: \n"))
        caesar(text, shift, direction, re_run)
        check_again = input(
            "Type \'yes\' if you want to go again. Otherwise type \'no\'.\n").lower()
        if check_again == 'no':
            re_run = False


if __name__ == '__main__':
    main()
