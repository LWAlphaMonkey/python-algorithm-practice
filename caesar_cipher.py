""" Caesar cipher is a type of substitution cipher

    Each letter in the plaintext is replaced by a letter with some fixed number
    of positions down the alphabet.
"""
from __future__ import print_function
#import string

def caesar_cipher(plain, num):
    """Form a cipher

    keyword arguments:
    plain -- plain text
    num -- shift num of positions down the alphabet
    """
    num = num % 26
    lower_case_string = plain.lower()
    alphabet = list('abcdefghijklmnopqrstuvwxyz')
    # or alphabet = list(string.ascii_lowercase)
    # or alphabet = list(map(chr, range(97, 123)))
    # or alphabet = list(map(chr, range(ord('a'), ord('z')+1)))

    # reverse the string
    #   string.ascii_lowercase[::-1]

    new_string = ''

    for index, current_letter in enumerate(lower_case_string):
        if current_letter == ' ':
            new_string += current_letter
            continue
        current_index = alphabet.index(current_letter)
        new_index = current_index + num

        if new_index > 25:
            new_index = new_index - 26
        elif new_index < 0:
            new_index = new_index + 26

        if plain[index] == plain[index].upper():
            new_string += alphabet[new_index].upper()
        else:
            new_string += alphabet[new_index]

    return new_string

print('caesar_cipher(Zoo keeper, 2):', caesar_cipher('Zoo Keeper', 2), '(Bqq Mggrgy)')
print('caesar_cipher(Big Car, -16):', caesar_cipher('Big Car', -16), '(Lsq Mkb)')
print('caesar_cipher(Javascript, -900):', caesar_cipher('Javascript', -900), '(Tkfkcmbszd)')
