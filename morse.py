#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Morse Code Decoder

"Dot" – is 1 time unit long.
"Dash" – is 3 time units long.
Pause between dots and dashes in a character – is 1 time unit long.
Pause between characters inside a word – is 3 time units long.
Pause between words – is 7 time units long.
"""
__author__ = 'Gordon Mathurin'

from morse_dict import MORSE_2_ASCII


#     H = . . . . = 1010101 = 11001100110011 =
# 2x slower = 111000111000111000111 = 3x slower
# first part is figuring the frequency and then strip to be fastest way
# try to find a unique # to figure out frequency ---> Hint
def decode_bits(bits):
    # your code here
    # maybe for loop to go thru morse dict and BITS to to compare vaule
    # associted with BITS and then
    # assign them to the new variable when == ????

    return


def decode_morse(morse):
    # your code here
    MORSE_2_ASCII[""] = " "
    vaule_match_holder = ""
    morse_list = morse.split(" ")
    print(morse_list)
    for elements in morse_list:
        vaule_match_holder += MORSE_2_ASCII[elements]
    print(vaule_match_holder)
    return vaule_match_holder


if __name__ == '__main__':
    hey_jude_morse = ".... . -.--   .--- ..- -.. ."
    hey_jude_bits = "11001100110011000000110000001111110011001111110011111100000000000000000000011001111110011111100111111000000110011001111110000001111110011001100000011"  # noqa

    # Be sure to run all included unit tests, not just this one.
    print("Morse Code decoder test")
    print("Part A:")
    print(f"'{hey_jude_morse}' -> {decode_morse(hey_jude_morse)}")
    print()
    print("Part B:")
    print(f"'{hey_jude_bits}' -> {decode_morse(decode_bits(hey_jude_bits))}")

    print("\nCompleted.")
