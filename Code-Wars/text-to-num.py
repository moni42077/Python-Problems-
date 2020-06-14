# Given a string, replace every letter with its position in the alphabet.
# If anything in the text isn't a letter, ignore it and don't return it.


import string


def alphabet_position(text):
    alphabet = string.ascii_lowercase
    text = text.lower()
    converted = []
    for i in text:
        for num, letter in enumerate(alphabet):
            if i == letter:
                converted.append(num+1)

    for i, ii in enumerate(converted):
        converted[i] = str(ii)

    return ' '.join(converted)

# It can be done much faster and shorter like:
# def alphabet_position(text):
    # return ' '.join(str(ord(c) - 96) for c in text.lower() if c.isalpha())
# but this is isn't as fun
