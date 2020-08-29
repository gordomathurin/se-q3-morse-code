from morse_dict import MORSE_2_ASCII


def decode_morse(morse):
    # your code here
    MORSE_2_ASCII[""] = " "
    vaule_match_holder = ""
    morse_list = morse.split(" ")
    print(morse_list)
    for elements in morse_list:
        vaule_match_holder += MORSE_2_ASCII[elements]
    print(vaule_match_holder)


decode_morse(".... . -.--   .--- ..- -.. .")
