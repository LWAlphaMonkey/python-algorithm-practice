"""
Fizz buzz is a group word game for children to teach them about division.
"""

from __future__ import print_function

def fiz_buzz(num):
    """ Return every num with following rules:
        any number divisible by three is replaced by the word fizz and any divisible
        by five by the word buzz.
    """
    for idx in range(1, num+1):
        if idx % 15 == 0:
            print("Fizz Buzz")
        elif idx % 3 == 0:
            print("Fizz")
        elif idx % 5 == 0:
            print("Buzz")
        else:
            print(idx)

fiz_buzz(20)
