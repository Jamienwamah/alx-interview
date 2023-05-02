#!/usr/bin/python3
'''Minimum Operations python3 challenge'''


def minOperations(n):
    '''calculates the fewest number of
    operations needed to result in exactly n H
    characters in this file.
    Returns: Integer
        if n is impossible to achieve, return 0
    '''
    pasted_chars = 1  # how many chars in the file
    clipboard = 0  # how many H's copied
    counter = 0  # operations counter

    while pasted_chars < n:
        # if the clipboard is empty, copy all the characters in the file
        if clipboard == 0:
            # copyall
            clipboard = pasted_chars
            # increment the operations counter
            counter += 1

        # if nothing has been pasted yet
        if pasted_chars == 1:
            # paste
            pasted_chars += clipboard
            # increment the operations counter
            counter += 1
            # continue to the next loop
            continue

        remaining = n - pasted_chars  # remaining chars to Paste
        # check if is impossible by checking if the clipboard
        # has more than what is required to reach the number
        # which also means num of chars in file is equal
        # or more than in the clipboard.
        # in either situations, it's impossible to achieve n of chars
        if remaining < clipboard:
            return 0

        # if can't be devided
        if remaining % pasted_chars != 0:
            # paste current clipboard
            pasted_chars += clipboard
            # increment the operations counter
            counter += 1
        else:
            # copyall
            clipboard = pasted_chars
            # paste
            pasted_chars += clipboard
            # increment the operations counter
            counter += 2

    # if got the desired result
    if pasted_chars == n:
        return counter
    else:
        return 0
