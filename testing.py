from morse_dict import MORSE_2_ASCII
from morse_dict import ASCII_2_MORSE


# def decode_morse(morse):
#     # your code here
#     MORSE_2_ASCII[""] = " "
#     vaule_match_holder = ""
#     morse_list = morse.split(" ")
#     print(morse_list)
#     for elements in morse_list:
#         vaule_match_holder += MORSE_2_ASCII[elements]
#     print(vaule_match_holder)


# decode_morse(".... . -.--   .--- ..- -.. .")

def decrypt(message):

    # extra space added at the end to access the
    # last morse code
    message += ' '

    decipher = ''
    citext = ''
    for letter in message:

        # checks for space
        if (letter != ' '):

            # counter to keep track of space
            i = 0
            # storing morse code of a single character
            citext += letter

        # in case of space
        else:
            # if i = 1 that indicates a new character
            i += 1

            # if i = 2 that indicates a new word
            if i == 2:

                # adding space to separate words
                decipher += ' '
            else:

                # accessing the keys using their values (reverse of encryption)
                decipher += list(MORSE_2_ASCII.keys()
                                 )[list(MORSE_2_ASCII.values()).index(citext)]
                citext = ''
            print(decipher)
            print(citext)
    return decipher


decrypt("11001100110011000000110000001111110011001111110011111100000000000000000000011001111110011111100111111000000110011001111110000001111110011001100000011")
